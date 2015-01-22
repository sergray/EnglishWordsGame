English Words Game
==================

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


Implementation Details
----------------------

Use NLTK + wordnet corpora to determine if given word is English.

Scalability
~~~~~~~~~~~

TODO

To Do List
----------

* Automate downloading of wordnet corpora, see nltk.download spec::

    nltk.download(self, info_or_id=None, download_dir=None, quiet=False, force=False, prefix=u'[nltk_data] ', halt_on_error=True, raise_on_error=False)

* Find out a way to determine if given word is English:

- NLTK+Wordnet
- Online web-service?

http://stackoverflow.com/questions/3788870/how-to-check-if-a-word-is-an-english-word-with-python

    >>> from nltk.corpus import wordnet
    >>> wordnet.synsets('identification')
    [Synset('designation.n.03'),
     Synset('identification.n.02'),
     Synset('identification.n.03'),
     Synset('recognition.n.02'),
     Synset('identification.n.05')]
    # first time call takes considerable time, need to warm up, it likely loads everything into memory, so may impose memory depending on size of corpora and number of Python processes
