"""
========================
Django Example: Admin Panel & Superuser Setup (Training Notes)
========================

• This document explains:
    1. Django Admin Panel
    2. Superuser Creation
    3. Migrations
    4. Login Flow
    5. Backend Working

• Format: Code + Explanation style for interns
"""

# --------------------------------------------------
# 1. INTRODUCTION (THEORY)
# --------------------------------------------------

"""
Django Admin Panel:
-------------------
• Built-in web interface provided by Django
• Used to manage database without SQL
• Supports CRUD operations:
    - Create
    - Read
    - Update
    - Delete

Superuser:
----------
• Highest privileged user in Django
• Can access admin panel
• Can manage all database data

Migrations:
-----------
• Converts models → database tables
• Required before using admin system
"""

# --------------------------------------------------
# 2. PROJECT SETUP COMMANDS
# --------------------------------------------------

"""
STEP 1: Create Project
----------------------
django-admin startproject portfolio

STEP 2: Create App
------------------
python manage.py startapp core

STEP 3: Run Server
------------------
python manage.py runserver
"""

# --------------------------------------------------
# 3. DATABASE SETUP (MIGRATIONS)
# --------------------------------------------------

"""
Why migrations are needed?
--------------------------
• Django has built-in apps like:
    - auth (users)
    - admin
    - sessions

• These require database tables

Command:
--------
python manage.py migrate
"""

# --------------------------------------------------
# 4. CREATE SUPERUSER
# --------------------------------------------------

"""
Command:
--------
python manage.py createsuperuser

Inputs:
-------
• Username
• Email
• Password

Rules:
------
• Minimum 8 characters
• Should not be common password
• Should not be fully numeric

Testing mode:
------------
• Django may ask:
    "Bypass password validation? (y/n)"
"""

# --------------------------------------------------
# 5. ADMIN PANEL ACCESS
# --------------------------------------------------

"""
URL:
----
http://127.0.0.1:8000/admin/

Login using:
-----------
• Superuser username
• Password

After login:
-----------
• You will see Django Admin Dashboard
"""

# --------------------------------------------------
# 6. INTERNAL WORKING FLOW
# --------------------------------------------------

"""
Flow of Admin System:

Database
   ↓
Django Models
   ↓
Migrations
   ↓
Admin Site
   ↓
Superuser Login
   ↓
Admin Dashboard
"""

# --------------------------------------------------
# 7. SETTINGS CONFIGURATION
# --------------------------------------------------

"""
INSTALLED_APPS (must include):

"""
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

"""
Explanation:
-----------
• admin → admin panel UI
• auth → user authentication system
• sessions → login session handling
"""

# --------------------------------------------------
# 8. ADMIN PANEL FEATURES
# --------------------------------------------------

"""
Inside Django Admin:

✔ User Management
    - Add user
    - Edit user
    - Delete user

✔ Password Management
    - Secure hashed storage

✔ Group Management
    - Role-based access (advanced)

✔ Data Management
    - Any model can be managed here
"""

# --------------------------------------------------
# 9. SECURITY CONCEPT
# --------------------------------------------------

"""
Important:
----------
• Django NEVER stores plain password
• Passwords are HASHED
• Even admin cannot view real password
"""

# --------------------------------------------------
# 10. COMMAND SUMMARY
# --------------------------------------------------

"""
Commands Used:

1. Create project:
   django-admin startproject portfolio

2. Create app:
   python manage.py startapp core

3. Run server:
   python manage.py runserver

4. Migrate database:
   python manage.py migrate

5. Create superuser:
   python manage.py createsuperuser
"""

# --------------------------------------------------
# 11. PRACTICE TASKS FOR INTERNS
# --------------------------------------------------

"""
TASK 1:
-------
Create Django project and run server

TASK 2:
-------
Run migrate and check database setup

TASK 3:
-------
Create superuser and login to admin

TASK 4:
-------
Create 3 users from admin panel

TASK 5:
-------
Try changing password and observe security behavior
"""

# --------------------------------------------------
# 12. FINAL SUMMARY
# --------------------------------------------------

"""
• Django Admin = Ready-made backend panel
• Superuser = Full access user
• Migrations = Create database structure
• Admin supports full CRUD operations
• Passwords are always encrypted

This is the foundation of Django backend system.
"""