English Words Game
==================

Submit the longest English word known to you (and to the application).

Submission requires registration, but it's easy and straighforward.


Setup Instructions
------------------

There's setup.py script which automates installation on Linux distributives having APT package manager.

It should be started from the root project directory:

```
python setup.py
```

Please follow instructions at the end of setup script.


Implementation Details
----------------------

* Current application uses sqlite3 database to store users and their best scores. Sqlite is ok for development, but is not suitable for production use. Please switch to what you like most (MySQL, Postgresql or maybe even Oracle) and note, that application was not tested with mentioned RDBM systems. However it only uses Django ORM without any raw SQL, so it should work out of the box.

* Best scores are kept in database. It's better to store them in memory, e.g. using Redis list.

* Application uses Python NLTK library and Wordnet text corpora to determine if submitted word is English. It's obvious that coropora does not include all known or invented English words (check Hitch-Hiker's Guide of Douglas Adams for nice examples). Therefore custom corpora might be needed.

* NLTK seems to load corpora to the memory on the first use. It makes the first request slow and must be fixed, loading corpora on application start before the first request.

* Load of corpora to the memory affects requirements to system memory and limits number of Python processes running the app. In order to scale, it can be implemented as separate service running on multiple machines.


To Do List
----------

* Add more tests. Coverage is poor at the moment :(

* Bootstrap project with Makefile or Docker

* Support automated setup on Linux distributives without APT. Use cuisine, salt, pupet or chef.
