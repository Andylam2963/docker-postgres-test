# PostgreSQL on Docker
This repository is a mini exercise to build a PostgreSQL image on Docker, and attempting to insert data that persists even after stopping or restarting the container.

## Requirements

### Environments and Libraries

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- Python 3
    - [psycopg2](https://www.psycopg.org/docs/install.html)

### Files

- `.env` - Create this file to store your environment variables locally. The environments needed in this project are:
    - `DB_NAME`
    - `DB_USER`
    - `DB_PASSWORD`

A sample `.env` file is as such

```bash
DB_NAME=databasename
DB_USER=username
DB_PASSWORD=yourpassword
```

## Building the Image and Database

You can simply build the image and run a container using a single command

```bash
docker-compose up
```

This command builds the image using the instructions given in `Dockerfile`, and `docker-compose.yml` configures the database within a container.

The database would already contain the table `users` with the columns:

name | user_id | email_address
-----|---------|--------------|

## Inserting Test Data

You can attempt to insert randomised test data using the `main.py` script. This script generates a list of user tuples in the format `(name, user_id, email_address)`, using a `first_name` and `last_name` parameter to generate them. The list of names are obtained through `namelist.json` for generation.

`main.py` requires a single `int` argument to indicate the size of the sample data you wish to insert. 

The example below inserts 100 randomised user data into the connected database.

```bash
python main.py 100
```

###### The names in `namelist.json` were obtained from https://github.com/smashew/NameDatabases.

## Testing

use `pytest --ignore=postgres-data` to run tests. The `--ignore=postgres-data` ignores the folder `postgres-data` since it is inaccessible by the testing module.


