clean:
	@git clean -xdf -e .venv

migrate: clean
	@cd PhanGon && \
		python manage.py migrate

dumpdb:
	@cd PhanGon && \
		python manage.py dumpdata \
		phantomname \
		--indent 4 \
		--format json \
		-o phantomname/fixtures/phantomname.json

loaddata:
	- @rm PhanGon/db.sqlite3
	@python PhanGon/manage.py migrate
	@python PhanGon/manage.py loaddata phantomname