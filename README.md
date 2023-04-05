![Logo](static/logo.png) 

# Newspaper Agency Tracker

Project for managing the publishing process of a newspaper agency by tracking the work of editors assigned to newspapers published by the agency

## Check it out 
[Newspaper agency tracker project deployed to Render](https://newspaper-agency-tracker.onrender.com/)

- **_login_**: user
- **_password_**: u$er@123

## Installation
Python3 must be already installed

```shell
git clone https://github.com/SergiiMachulin/newspaper-agency-tracker
cd newspaper
python -m venv venv
source venv/bin/activate (on Linux/maOS)
venv\Scripts\activate (on Windows)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```
For deployment next environment variables to store API keys and other configuration values and secrets were used:
- DATABASE_URL
- DJANGO_DEBUG
- DJANGO_SECRET_KEY
- PYTHON_VERSION
- WEB_CONCURRENCY

## Features
* Authentication functionality for Editor/User
* Managing topics newspapers & editors directly from website interface
* Powerful admin panel for advanced managing

## Demo
![Website interface](demo.png)
