{
    'name': 'Birthday Wish',
    'version': '18.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Automatically send birthday wishes to employees',
    'description': """
        This module automatically sends birthday wishes to employees via email on their birthdays.
        It includes cron jobs to check birthdays daily and send wishes.
    """,
    'author': 'DAKOTA',
   'depends': ['mail', 'hr'],
    'data': [   
        'security/ir.model.access.csv',
        'data/mail_templates.xml',
        'data/schedule_actions.xml',
        'views/birthday_wish_views.xml',
        'views/hr_employee_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}