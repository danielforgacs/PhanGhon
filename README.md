## Phantom Ghost Name Picker

**for usage see Makefile targets.**


### The project uses pipenv

```
$ pipenv shell

$ pipenv install [--dev]
```

### Run the project

```
# create a python env...

# apply migrations
$ make migrate

# load fixtues: ghostname table, a few users
$ make loaddata
```

### Run the project - in a container

```
$ make build

$ make up
```

## Notes:

- I always remove the SECRET_KEY and DEBUG vars and move  
them into env vars. I left SECRET_KEY hardcoded for this  
test task. Safe sites is not updated, set the DEBUG  
env var to something non empty. (pipenv will use  
the .env file and set this.)

- I checked out the __4-hours-mark__ branch to mark  
when 4 hours has passed since I started working  
on this project.

- the __approx-10-hours-mark__ branch marks approximatelly  
10 hours of work. At that point the product works,
needs testing.

- I set indentation to 4 spaces in the .pylintrc  
specified in the brief. I also turned off docstring    
messages, I would say the standard Django view,  
model, urls, etc... modules or few lines classes
need documentation.


## ToDo:

- sphinx docs
- more testing, QA
- CI/CD

## Possible Improvement:

- performance test queries
- the secrets should be stored better
- class based views
