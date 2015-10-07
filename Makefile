.PHONY: dummy

dummy:
	@echo dummy

# For development
runserver:
	python ./genome/manage.py runserver 127.0.0.1:8000

sql:
	sqlite3 ./genome/db.sqlite3

migrate:
	python ./genome/manage.py migrate
