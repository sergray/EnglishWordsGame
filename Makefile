PROJECT = ./english_words_game
MANAGE.PY = $(PROJECT)/manage.py

all: run

run:
	$(MANAGE.PY) runserver

qa:
	(cd $(PROJECT) && ./manage.py test)

deploy:
	(cd ./ansible && ansible-playbook -i inventory.ini deploy.yml)
