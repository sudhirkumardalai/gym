# Gym Website

This repository contains the source code for a fully functional gym management website built with Django. The project provides features such as user authentication, member management, and basic CRUD (Create, Read, Update, Delete) operations for gym members.

## Features

- **User Authentication:** Secure user registration, login, and logout.
- **Member Management:** Add, update, and delete gym members.
- **Protected Views:** Certain views are protected and require user authentication.
- **Responsive Design:** Mobile-friendly design for a seamless user experience.

## Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (with Django templates)
- **Database:** SQLite (or other Django-supported databases)

## Installation

To run this project locally, follow these steps:

### Prerequisites

- Python 3.12.0 installed
- Django installed

### Clone the Repository

```bash
git clone https://github.com/yourusername/gym-website.git
cd gym-website
***Install Dependencies:
pip install -r requirements.txt

## Apply Migrations:
python manage.py migrate
## Create a Superuser:
python manage.py createsuperuser
## Run the Development Server:
python manage.py runserver

The development server will start on http://127.0.0.1:8000/.

### Usages

##User Registration and Login:
Register a new account at http://127.0.0.1:8000/register.
Log in with existing credentials at http://127.0.0.1:8000/log.

## Home Page:
After logging in, manage gym members on the home page (http://127.0.0.1:8000/home).
Add new members by filling out the form and submitting it.
View the list of all gym members.

## Update Member:
Update a member's information by navigating to http://127.0.0.1:8000/update/<id>.

## Delete Member:
Delete a member by navigating to http://127.0.0.1:8000/delete/<id>.

## Logout:
Log out from the application by navigating to http://127.0.0.1:8000/logo.

## Project Structure:

web/
├── service/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── log.html
│   │   ├── register.html
│   │   ├── update.html
│   │   ├── test.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── web/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md

### API Endpoints

Home Page: GET /home and POST /home
Delete Member: GET /delete/<id>
Update Member: GET /update/<id> and POST /update/<id>
Login: GET /log and POST /log
Logout: GET /logo
Register: GET /register and POST /register
Test Page: GET /test

### Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### Acknowledgements
Django
Python
HTML

This `README.md` file provides a comprehensive guide for anyone looking to understand, install, and contribute to your gym website project. Adjust the sections as necessary to better reflect your project's specifics and any additional information you might want to include.
