# trailtracker
A Django based hike tracking app.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for running and testing purposes. 

### Prerequisites

Requirements for the software and other tools to build, run and deploy
- [Python 3.11](https://www.python.org/)

### Installing

To install dependencies for this service run the following commands:

```
    # setup virtual environment
    python -m venv venv
    # activate virtual environment
    .\venv\Scripts\activate
    # install dependencies
    pip install -r requirements.txt
```

To setup the Django Admin super user and run migrations run the following commands:

```
    python manage.py createsuperuser
    python manage.py makemigrations 
    python manage.py migrate
```

### Running the service

To run this service run the following command:

```
    python manage.py runserver 
```

The app can be accessed at http://127.0.0.1:8000/.

## Usage

Register a user then login and start tracking hikes.

A demo user has been created to demonstrate the different functionalities of the app
- user: demo
- pass: demo1337

## License

This project is licensed under the [MIT License](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details