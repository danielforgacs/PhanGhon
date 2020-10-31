clean:
	@git clean -xdf -e .venv

migrate:
	@cd PhanGhon && \
		python manage.py migrate

dumpdb:
	@cd PhanGhon && \
		python manage.py dumpdata \
		phantomname \
		--indent 4 \
		--format json \
		-o phantomname/fixtures/phantomname.json

loaddata:
	@python PhanGhon/manage.py migrate
	@python PhanGhon/manage.py loaddata phantomname


pylint:
	@find PhanGhon/phantomname/ -name '*.py' \
		! -name '__init__.py' \
		! -path '**/migrations/**' \
		| xargs pylint

test:
	@pytest PhanGhon

build:
	@docker-compose build --no-cache --force-rm --pull

up:
	@docker-compose up

upd:
	@docker-compose up -d