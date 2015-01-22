English Words Game
==================

Submit the longest Egnlish word as you can (and what is known by us).

Submission requires registration, but it's easy and fast.

Setup Instructions
------------------

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt

Setup NLTK corpora::

   import nltk
   nltk.download()


Shows Tk GUI. selected wordnet corpora. Downloads to $HOME/nltk_data directory by default::

    $ du -hs $HOME/nltk_data/corpora/wordnet
    35M /Users/sergray/nltk_data/corpora/wordnet

$ cd english_words_game/
$ ./manange.py syncdb  # creates sqlite3 database
$ ./manage.py runserver


Implementation Details
----------------------

* Current application uses sqlite3 database to store users and their best scores. Sqlite is ok for development, but is not suitable for production use. Please switch to what you like most (MySQL, Postgresql or maybe even Oracle) and note, that application was not tested with mentioned RDBM systems. However it only uses Django ORM without any raw SQL, so it should work out of the box.

* Best scores are kept in database. It's better to store them in memory, e.g. using Redis list.

* Application uses Python NLTK library and Wordnet text corpora to determine if submitted word is English. It's obvious that coropora does not include all known or invented English words (check Hitch-Hiker's Guide of Douglas Adams for nice examples). Therefore custom corpora might be needed.

* NLTK seems to load corpora to the memory on the first use. It makes the first request slow and must be fixed, loading corpora on application start before the first request.

* Load of corpora to the memory affects requirements to system memory and limits number of Python processes running the app. In order to scale, it can be implemented as separate service running on multiple machines.


To Do List
----------

* Add Makefile setting up the project

* Automate downloading of wordnet corpora, see nltk.download spec::

    nltk.download(self, info_or_id=None, download_dir=None, quiet=False, force=False, prefix=u'[nltk_data] ', halt_on_error=True, raise_on_error=False)

* Add more tests. Coverage is poor at the moment :(
