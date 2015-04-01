English Words Game
==================

Submit the longest English word known to you (and to the application).

Submission requires registration, but it's easy and straighforward.

Can be played on http://words.sergray.me/


Setup Instructions
------------------

There's setup.py script which automates installation on Linux distributives having APT package manager.

It should be started from the root project directory:

```
python setup.py
```

Please follow instructions at the end of setup script.

Social authentication is implemented with http://django-allauth.readthedocs.org/en/latest/installation.html


Implementation Details
----------------------

* Default setup uses sqlite3 database to store users and their daily best scores. Sqlite is ok for development, but is not suitable for production use. Please switch to what you like most (MySQL, Postgresql or maybe even Oracle). Works with Postgresql out of the box.

* Top daily scores are fetched from database. It's better to store them in memory, e.g. using Redis list.

* Application uses Python NLTK library and Wordnet text corpora to determine if submitted word is English. It's obvious that coropora does not include all known or invented English words (check Hitch-Hiker's Guide of Douglas Adams for nice examples). Therefore custom corpora might be needed.

* Load of corpora to the memory affects requirements to system memory and limits number of Python processes running the app. In order to scale, it can be implemented as separate service running on multiple machines.


To Do List
----------

* Add more tests. Coverage is poor at the moment :(

* Bootstrap project with Makefile or Docker

* Support automated setup on Linux distributives without APT. Use cuisine, salt, pupet or chef.

* Password-less registration with Facebook.

* All time top-scores
