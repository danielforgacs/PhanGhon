clean:
	@git clean -xdf -e .venv

migrate: clean
	@cd PhanGon && \
		python manage.py migrate
