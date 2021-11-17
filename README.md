# Django Polls Application

A polls application written in Python using the Django framework. The app allows users to view polls and vote in them. It also allows one to add, change, and delete polls via an admin site.

The following skills are demonstrated in this project:
* Python
* HTML, CSS, JavaScript
* Django framework
* Dependency management using pip
* Model View Template (MVT) pattern
* Databases - SQLite
* Database migrations
* HTTP response status codes
* Automated testing
* Git

## Installation and setup

1. Install Python3 in your system. For example, in debian-based systems:
   ```sh
   $ sudo apt get install python3.8 python3.8-venv
   ```


## How to run

The code in this project has been tested and run using Python 3.8.x and Django 3.2.

To run the project follow the steps below:

1. Clone the repository.
   ```sh
   $ git clone git@github.com:stevie-nomad/polls_app.git
   ```

2. Create a virtual environment
   ```sh
   $ python3 -m venv venv
   ```
3. Activate the virtual environment
   ```sh
   $ source venv/bin/activate
   ```
4. Install the dependencies in the virtual environment
   ```sh
   $ pip install -r requirements.txt

5. From the polls_apps root folder run the server
   ```sh
   $ python manage.py runserver
   ```
   You can now access the app from your browser at http://127.0.0.1:8000/


## Acknowledgments

* [Djangoproject documentation](https://docs.djangoproject.com/en/3.2/)
