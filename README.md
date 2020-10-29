## Phantom Ghost Name Picker


### The project uses pipenv

```
$ pipenv shell

$ pipenv install
```

### Run the project

```
# create a python env...

# apply migrations
$ make migrate

# load fixtues: ghostname table, a few users
$ make loaddata
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


## ToDo: