English Words Game
==================

Submit the longest English word known to you (and to the application).

Submission requires registration, but it's easy and straighforward.

Setup Instructions
------------------

Launch development version of application using Docker Compose:

```shell
docker-compose up
```

It will:
* download NLTK wordnet dataset
* prepare sqlite3 database
* launch Django application with runserver

Open http://localhost:8000/.

Social authentication is implemented with http://django-allauth.readthedocs.org/en/latest/installation.html

Please follow a [provider specific documentation](https://django-allauth.readthedocs.io/en/latest/providers.html) for obtaining provider credentials.

Authentication provider in the application is configured using Django admin UI.

Create super admin with:

```shell
docker-compose exec app ./manage.py createsuperuser
```

Then open http://localhost:8000/admin/socialaccount/socialapp/, login with super user credentials and create new social application for the chosen provider.

Implementation Details
----------------------

* Default setup uses sqlite3 database to store users and their daily best scores. Sqlite is ok for development, but is not suitable for production use. Please switch to what you like most (MySQL, Postgresql or maybe even Oracle). Works with Postgresql out of the box.

* Top daily scores are fetched from database. It's better to store them in memory, e.g. using Redis list.

* Application uses Python NLTK library and Wordnet text corpora to determine if submitted word is English. It's obvious that coropora does not include all known or invented English words (check Hitch-Hiker's Guide of Douglas Adams for nice examples). Therefore custom corpora might be needed.

* Load of corpora to the memory affects requirements to system memory and limits number of Python processes running the app. In order to scale, it can be implemented as separate service running on multiple machines.

* Password-less login uses allauth, see https://django-allauth.readthedocs.io/en/stable/providers.html#google to set it up for Google OAuth

To Do List
----------

* All time top-scores
* Nice UI
* Multi-language support
