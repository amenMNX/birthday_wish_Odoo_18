# 🎂 Anniversaires Employés Smart — Odoo 18

> **Module Odoo Enterprise pour la gestion intelligente et automatisée des anniversaires des employés.**

---

## 🇫🇷 Français

### 📋 Présentation

**Anniversaires Employés Smart** est un module Odoo 18 conçu pour gérer, automatiser et centraliser la gestion des anniversaires des employés dans un environnement **multi-sociétés**.

Le module permet de suivre les prochains anniversaires, de synchroniser automatiquement les événements avec le calendrier Odoo, d'afficher des alertes sur les fiches employés et d'envoyer automatiquement des vœux personnalisés par **email** et via **Discuss**.

Il offre également des outils de configuration et de sécurité permettant de contrôler l'affichage de l'âge des employés.

<img width="6240" height="5127" alt="diagram (2)" src="https://github.com/user-attachments/assets/80b50dd9-bf9c-439a-bb91-33d97a2e2e62" />

---

## ✨ Fonctionnalités principales

### 📅 Tableau de bord et suivi des anniversaires

* Visualisation des anniversaires :

  * 🎂 Aujourd'hui
  * 📆 Cette semaine
  * 🗓️ Ce mois
* Calcul automatique du prochain anniversaire.
* Compte à rebours jusqu'au prochain anniversaire.
* Identification automatique des anniversaires du jour.

### 🧮 Informations calculées sur les employés

Le module étend le modèle `hr.employee` avec plusieurs champs calculés :

* `next_birthday` — Date du prochain anniversaire
* `birthday_age` — Âge atteint lors du prochain anniversaire
* `days_until_next_birthday` — Nombre de jours restants
* `is_birthday_today` — Indique si l'anniversaire est aujourd'hui

Le champ `is_birthday_today` dispose également d'une méthode de recherche dédiée.

### 📆 Synchronisation avec le calendrier

Les anniversaires sont automatiquement synchronisés avec `calendar.event`.

Le système crée ou met à jour les événements lorsque les informations suivantes changent :

* Date de naissance
* Nom de l'employé
* Département

Les événements d'anniversaire disposent d'un indicateur spécifique :

* `is_birthday`

Une vue calendrier dédiée permet de filtrer facilement les événements liés aux anniversaires.

### 🎉 Gestion des célébrations

Le module permet de suivre les informations liées aux célébrations :

* 🎁 Cadeaux
* 💰 Budget
* 📝 Notes
* 📊 Statut de célébration

### 🤖 Notifications automatiques

Un **cron quotidien** centralise l'automatisation du module.

Il permet de :

1. Actualiser les événements d'anniversaire du calendrier.
2. Identifier les anniversaires du jour.
3. Envoyer des vœux personnalisés par email.
4. Publier des notifications dans les canaux **Discuss** appropriés.
5. Gérer les notifications selon la société concernée.

Les canaux Discuss peuvent être créés dynamiquement selon le contexte de chaque société.

### ✉️ Emails personnalisés

Le module fournit un modèle d'email dédié :

> **« Joyeux Anniversaire … »**

Les utilisateurs peuvent sélectionner le modèle d'email depuis les paramètres du module.

### 🏢 Multi-sociétés

Le module est conçu pour les environnements **multi-company** Odoo.

Les emails, notifications et canaux Discuss utilisent le contexte de la société concernée afin d'éviter les mélanges entre différentes filiales.

### 🔐 Sécurité et confidentialité

L'affichage de l'âge des employés est contrôlé par les permissions.

Une **groupe de sécurité dédié** permet de déterminer quels utilisateurs peuvent consulter l'âge des employés.

### ⚙️ Configuration

Une page de configuration est disponible dans :

**Paramètres → RH → Anniversaires**

Les options permettent notamment de :

* Choisir le modèle d'email.
* Activer ou désactiver l'affichage de l'âge.
* Configurer les options liées aux anniversaires.

### 🎂 Cas particulier du 29 février

Le module prend en charge le cas particulier des employés nés le **29 février**, afin que leur anniversaire soit correctement géré lors des années non bissextiles.

---

## 🖥️ Interface

Le module ajoute plusieurs éléments à l'interface Odoo :

### Fiche employé

La fiche `hr.employee` contient :

* 🎂 Une alerte/ruban lorsqu'il s'agit de l'anniversaire de l'employé.
* Une page dédiée **« Anniversaire »**.
* Un bouton statistique affichant le compte à rebours jusqu'au prochain anniversaire.

### 📅 Calendrier

Une vue calendrier dédiée permet d'afficher et de filtrer les événements d'anniversaire.

### 📋 Menus RH

Des menus dédiés sont disponibles dans le module **Ressources Humaines**.

### ⚙️ Paramètres

Une page de configuration est disponible dans la configuration RH.

---

## 🏗️ Architecture technique

### Modèles

#### `hr.employee`

Modèle principal étendu pour gérer :

* Les champs calculés.
* La logique des anniversaires.
* La synchronisation avec le calendrier.
* Le traitement quotidien du cron.

#### `calendar.event`

Extension du modèle calendrier avec :

* `is_birthday`
* Méthodes de synchronisation des événements d'anniversaire.

#### `res.config.settings`

Gère les paramètres du module :

* Modèle d'email.
* Affichage de l'âge.
* Options liées aux anniversaires.

---

## 📦 Dépendances

Le module dépend des modules Odoo suivants :

```text
hr
calendar
mail
```

---

## 📁 Structure du module

```text
birthday_wish_18/
│
├── __init__.py
├── __manifest__.py
│
├── data/
│   ├── cron_data.xml
│   ├── mail_channel_data.xml
│   └── mail_template_data.xml
│
├── models/
│   ├── __init__.py
│   ├── calendar_event.py
│   ├── hr_employee.py
│   └── res_config_settings.py
│
├── security/
│   ├── birthdays_security.xml
│   └── ir.model.access.csv
│
└── views/
    ├── calendar_views.xml
    ├── hr_employee_views.xml
    ├── menus.xml
    └── res_config_settings_views.xml
```

---

## 🚀 Installation

### Méthode 1 — Installation depuis les Apps Odoo

1. Copier le dossier `birthday_wish_18` dans le répertoire `addons` d'Odoo.
2. Redémarrer le serveur Odoo.
3. Activer le **mode développeur**.
4. Aller dans **Applications**.
5. Mettre à jour la liste des applications.
6. Rechercher **Anniversaires Employés Smart**.
7. Cliquer sur **Installer**.

### Configuration

Après l'installation :

**Paramètres → RH → Anniversaires**

Configurez :

* Le modèle d'email.
* La visibilité de l'âge.
* Les options de notification.

Le cron quotidien prendra ensuite automatiquement en charge les anniversaires.

---

## 🔄 Fonctionnement automatique

Le flux quotidien du module peut être résumé ainsi :

```text
                 ┌─────────────────────┐
                 │   Cron quotidien    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Vérification des    │
                 │ anniversaires       │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ Mise à jour du  │   │ Anniversaire    │
        │ calendrier      │   │ du jour ?       │
        └─────────────────┘   └────────┬────────┘
                                       │
                              ┌────────┴────────┐
                              ▼                 ▼
                       ┌─────────────┐   ┌─────────────┐
                       │ Email       │   │ Discuss     │
                       │ personnalisé│   │ notification│
                       └─────────────┘   └─────────────┘
```

---

## 📌 Informations techniques

* **Version Odoo :** 18.0
* **Version du module :** `18.0.2.0.0`
* **Type :** Module Odoo Enterprise
* **Licence :** LGPL-3
* **Multi-company :** ✅
* **Automatisation Cron :** ✅
* **Email notifications :** ✅
* **Discuss notifications :** ✅
* **Calendar synchronization :** ✅
* **Access control :** ✅
* **Leap-year support :** ✅

---

# 🇬🇧 English

### 📋 Overview

**Smart Employee Birthdays** is an Odoo 18 module designed to manage, automate, and centralize employee birthday management in **multi-company Odoo environments**.

The module tracks upcoming birthdays, automatically synchronizes birthday events with the Odoo Calendar, displays birthday alerts on employee forms, and sends personalized birthday wishes through **email** and **Discuss**.

It also provides configuration and security features to control employee age visibility.

---

## ✨ Key Features

### 📅 Birthday Dashboard & Tracking

* Birthday overview for:

  * 🎂 Today
  * 📆 This week
  * 🗓️ This month
* Automatic calculation of the next birthday.
* Countdown to the next birthday.
* Automatic identification of birthdays occurring today.

### 🧮 Computed Employee Fields

The module extends `hr.employee` with several computed fields:

* `next_birthday` — Next birthday date
* `birthday_age` — Age reached on the next birthday
* `days_until_next_birthday` — Number of days remaining
* `is_birthday_today` — Indicates whether today is the employee's birthday

The `is_birthday_today` field also provides a dedicated search method.

### 📆 Calendar Synchronization

Employee birthdays are automatically synchronized with `calendar.event`.

Calendar events are created or updated whenever relevant employee information changes, including:

* Birthday
* Employee name
* Department

Birthday events include a dedicated:

* `is_birthday`

flag.

A dedicated calendar view makes it easy to filter and display birthday events.

### 🎉 Celebration Management

The module provides tools to track birthday celebrations, including:

* 🎁 Gifts
* 💰 Budget
* 📝 Notes
* 📊 Celebration status

### 🤖 Automated Notifications

A **daily cron job** serves as the main automation entry point.

It automatically:

1. Refreshes birthday calendar events.
2. Detects employees whose birthday is today.
3. Sends personalized birthday emails.
4. Posts notifications to appropriate **Discuss** channels.
5. Handles notifications according to the relevant company.

Discuss channels can be created dynamically for each company.

### ✉️ Personalized Emails

The module includes a dedicated birthday email template:

> **"Happy Birthday …"**

Administrators can select the email template from the module settings.

### 🏢 Multi-Company Support

The module is designed for **multi-company Odoo environments**.

Emails, notifications, and Discuss channels use the appropriate company context, preventing communication between unrelated subsidiaries.

### 🔐 Security & Privacy

Employee age visibility is permission-controlled.

A dedicated **security group** determines which users are allowed to view employee ages.

### ⚙️ Configuration

The module provides a configuration page under:

**Settings → HR → Birthdays**

Administrators can:

* Select the birthday email template.
* Enable or disable age visibility.
* Configure birthday-related options.

### 🎂 February 29 Support

The module handles the special case of employees born on **February 29**, ensuring birthdays continue to be managed correctly during non-leap years.

---

## 🖥️ User Interface

### Employee Form

The `hr.employee` form includes:

* 🎂 A birthday ribbon/alert when it is the employee's birthday.
* A dedicated **"Birthday"** notebook page.
* A statistical button showing the countdown to the next birthday.

### 📅 Calendar

A dedicated calendar view displays and filters birthday events.

### 📋 HR Menus

Birthday-related menus are available under the **Human Resources** section.

### ⚙️ Settings

A dedicated configuration page is available under HR settings.

---

## 🏗️ Technical Architecture

### Models

#### `hr.employee`

The main model extension responsible for:

* Computed birthday fields.
* Birthday business logic.
* Calendar synchronization.
* Daily cron processing.

#### `calendar.event`

Extends the calendar event model with:

* `is_birthday`
* Birthday synchronization helper methods.

#### `res.config.settings`

Handles module configuration, including:

* Email template selection.
* Age visibility.
* Birthday-related settings.

---

## 📦 Dependencies

The module depends on the following Odoo modules:

```text
hr
calendar
mail
```

---

## 📁 Module Structure

```text
birthday_wish_18/
│
├── __init__.py
├── __manifest__.py
│
├── data/
│   ├── cron_data.xml
│   ├── mail_channel_data.xml
│   └── mail_template_data.xml
│
├── models/
│   ├── __init__.py
│   ├── calendar_event.py
│   ├── hr_employee.py
│   └── res_config_settings.py
│
├── security/
│   ├── birthdays_security.xml
│   └── ir.model.access.csv
│
└── views/
    ├── calendar_views.xml
    ├── hr_employee_views.xml
    ├── menus.xml
    └── res_config_settings_views.xml
```

---

## 🚀 Installation

### Method 1 — Install through Odoo Apps

1. Copy the `birthday_wish_18` folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Enable **Developer Mode**.
4. Open **Apps**.
5. Update the Apps list.
6. Search for **Smart Employee Birthdays**.
7. Click **Install**.

### Configuration

After installation, go to:

**Settings → HR → Birthdays**

Configure:

* Email template.
* Age visibility.
* Notification options.

The daily cron job will then automatically handle birthday processing.

---

## 🔄 Automated Workflow

The module's daily workflow can be summarized as follows:

```text
                 ┌─────────────────────┐
                 │    Daily Cron       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Check employee      │
                 │ birthdays           │
                 └──────────┬──────────┘
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
        ┌─────────────────┐   ┌─────────────────┐
        │ Refresh calendar│   │ Birthday today? │
        │ events          │   │                 │
        └─────────────────┘   └────────┬────────┘
                                       │
                              ┌────────┴────────┐
                              ▼                 ▼
                       ┌─────────────┐   ┌─────────────┐
                       │ Personalized│   │ Discuss     │
                       │ Email       │   │ Notification│
                       └─────────────┘   └─────────────┘
```

---

## 📌 Technical Information

* **Odoo Version:** 18.0
* **Module Version:** `18.0.2.0.0`
* **Type:** Odoo Enterprise Module
* **License:** LGPL-3
* **Multi-Company:** ✅
* **Cron Automation:** ✅
* **Email Notifications:** ✅
* **Discuss Notifications:** ✅
* **Calendar Synchronization:** ✅
* **Access Control:** ✅
* **Leap-Year Support:** ✅

---

## 📄 License

This module is released under the **LGPL-3** license.
