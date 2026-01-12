from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date
import logging

_logger = logging.getLogger(__name__)


class BirthdayWish(models.Model):
    _name = 'birthday.wish'
    _description = 'Birthday Wish'
    _rec_name = 'employee_id'
    _order = 'birthday_date desc'

    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        ondelete='cascade'
    )

    email = fields.Char(
        string='Email',
        related='employee_id.work_email',
        readonly=True,
        store=True
    )

    birthday_date = fields.Date(
        string='Birthday',
        related='employee_id.birthday',
        store=True,
        readonly=True
    )

    wish_sent = fields.Boolean(
        string='Wish Sent',
        default=False,
        readonly=True
    )
    
    sent_date = fields.Date(
        string='Sent Date',
        readonly=True
    )

    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company
    )

    active = fields.Boolean(
        string='Active',
        default=True
    )

    # =========================
    # CREATE PROTECTION
    # =========================
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('employee_id'):
                today = date.today()
                existing = self.search([
                    ('employee_id', '=', vals['employee_id']),
                    ('sent_date', '>=', date(today.year, 1, 1)),
                ], limit=1)

                if existing:
                    raise ValidationError(
                        _('A birthday wish already exists for this employee this year.')
                    )

        return super().create(vals_list)

    # =========================
    # SEND EMAIL
    # =========================
    def send_birthday_wish(self):
        """Send birthday wish email to employee"""
        self.ensure_one()

        if not self.email:
            _logger.warning(
                "No email found for employee %s", 
                self.employee_id.name
            )
            return False

        template = self.env.ref(
            'birthday_wish.birthday_wish_email_template',
            raise_if_not_found=False
        )

        if not template:
            raise ValidationError(_('Email template not found.'))

        try:
            template.send_mail(self.id, force_send=True)

            self.write({
                'wish_sent': True,
                'sent_date': date.today(),
            })

            _logger.info(
                "Birthday wish sent to %s (%s)", 
                self.employee_id.name,
                self.email
            )
            return True

        except Exception as e:
            _logger.exception("Failed to send birthday email to %s", self.employee_id.name)
            raise ValidationError(_('Failed to send email: %s') % str(e))

    # =========================
    # CRON JOB
    # =========================
    @api.model
    def cron_send_birthday_wishes(self):
        """Daily cron job to send birthday wishes"""
        today = date.today()
        _logger.info("Birthday Wish cron started for date: %s", today)

        # Find all active employees with email and birthday
        employees = self.env['hr.employee'].search([
            ('active', '=', True),
            ('work_email', '!=', False),
            ('birthday', '!=', False),
        ])

        sent_count = 0
        for emp in employees:
            bday = emp.birthday

            # Check if today is their birthday
            if bday.month != today.month or bday.day != today.day:
                continue

            # Check if wish already sent this year
            already_sent = self.search([
                ('employee_id', '=', emp.id),
                ('sent_date', '>=', date(today.year, 1, 1)),
            ], limit=1)

            if already_sent:
                _logger.info(
                    "Birthday wish already sent to %s this year", 
                    emp.name
                )
                continue

            try:
                # Create birthday wish record
                wish = self.create({
                    'employee_id': emp.id,
                })

                # Send the wish
                wish.send_birthday_wish()
                sent_count += 1

            except Exception as e:
                _logger.exception(
                    "Failed to send birthday wish to %s: %s", 
                    emp.name, 
                    str(e)
                )
                continue

        _logger.info(
            "Birthday Wish cron finished. Sent %d wishes.", 
            sent_count
        )
        return True


# ======================================================
# HR EMPLOYEE EXTENSION
# ======================================================
class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    birthday_wish_ids = fields.One2many(
        'birthday.wish',
        'employee_id',
        string='Birthday Wishes'
    )

    birthday_wish_count = fields.Integer(
        string='Birthday Wishes Count',
        compute='_compute_birthday_wish_count',
        store=False
    )

    def _compute_birthday_wish_count(self):
        """Compute the number of birthday wishes sent"""
        for emp in self:
            emp.birthday_wish_count = len(emp.birthday_wish_ids)

    def action_view_birthday_wishes(self):
        """Open birthday wishes for this employee"""
        self.ensure_one()
        return {
            'name': _('Birthday Wishes'),
            'type': 'ir.actions.act_window',
            'res_model': 'birthday.wish',
            'view_mode': 'tree,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {
                'default_employee_id': self.id,
            },
        }