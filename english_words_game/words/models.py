import logging

from django.db import models

logger = logging.getLogger(__file__)

# hack to trigger loading of corpora at application start
try:
    from nltk.corpus import wordnet
    logger.debug('Loading NLTK wordnet')
    getattr(wordnet, 'synsets')
    logger.debug('Loaded NLTK wordnet')
except ImportError:
    pass
