# jd-django-drf-challenge
Django and DRF challenge as part of the Jungle Devs' recruitment process Aug/21.

# Start here:

## Development mode:

 - Simply clone this repo then on your terminal/console:
    $ git clone...
 - Make sure the first line or block of code below # **LOCAL** are UNCOMMENTED and that the first line or block of code below # **PRODUCTION** are COMMENTED ON settings.py module.
 - Make sure your docker-machine is running and accessible:
    $ docker ps
 - Build the image:
    $ docker-compose build
 - Run the image:
    $ docker-compose up

------------------------------------------------------------------------
## Production mode:

 - Simply clone this repo then on your terminal/console:
    $ git clone...
 - Make sure the first line or block of code below '# **PRODUCTION**' are UNCOMMENTED and that the first line or block of code below '# **LOCAL**' are COMMENTED ON settings.py module.
 - Make sure your docker-machine is running and accessible:
    $ docker ps
 - Build the image:
    $ docker-compose build
 - Run the image:
    $ docker-compose up
 - For Deployment onto AWS follow this link below:
    https://londonappdeveloper.com/deploying-django-with-docker-compose/
------------------------------------------------------------------------
## Link for the API documentation:

 - Installation
Install using pip...

$ pip install drf-spectacular
then add drf-spectacular to installed apps in settings.py

INSTALLED_APPS = [
    # ALL YOUR APPS
    'drf_spectacular',
]
and finally register our spectacular AutoSchema with DRF.

REST_FRAMEWORK = {
    # YOUR SETTINGS
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
drf-spectacular ships with sane default settings that should work reasonably well out of the box. It is not necessary to specify any settings, but we recommend to specify at least some metadata.

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}

------------------------------------------------------------------------
## Endpoints for testing the app:

 - /api/login
 - /api/signup
 - /api/authors
 - /api/category
 - /api/articles
 - /api/articles/id
------------------------------------------------------------------------

