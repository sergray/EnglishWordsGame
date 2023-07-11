PROJECT_DIR ?= ./english_words_game
MANAGE.PY = $(PROJECT_DIR)/manage.py

.PHONY: setup nltk_data django_migrate django_runserver qa deploy

setup: setup.py
	python setup.py

nltk_data:
	python -c "import nltk, os; nltk.download('wordnet')"

django_migrate:
	$(MANAGE.PY) migrate

# Target bellow starts Django development runserver listening on all interfaces
# It is meant to be used only in Docker container
django_runserver: nltk_data django_migrate
	$(MANAGE.PY) runserver 0.0.0.0:8000

qa:
	(cd $(PROJECT_DIR) && ./manage.py test)
