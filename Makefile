.PHONY: dummy

dummy:
	@echo dummy

# For development
runserver:
	cd ./genome/; \
	python manage.py runserver 127.0.0.1:8000
