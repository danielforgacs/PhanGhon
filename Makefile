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
