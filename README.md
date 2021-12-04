# fullstack-chat
A full stack messaging app built with React, Flask and PostgreSQL

## Running the App
### Database
To start the database, start a PostgreSQL server using [pgAdmin](https://www.pgadmin.org).
Next, create a file named `db.yml` in the `server` folder. Use the following template to add your database's credentials to the file.
```yml
host: localhost
database: YOUR_DATABASE
user: YOUR_USER
password: YOUR_PASSWORD
port: 5432
```

### API
In a new command line window, navigate to the root directory of this project. Then, run:
```console
$ python server/server.py
```

### Web Application
In a new command line window, navigate to the root directory of this project. Next, move to the frontend directory and start the web application by using one of the following methods:
#### npm
```console
$ cd frontend
$ npm start
```

#### Yarn
```console
$ cd frontend
$ yarn start
```

And, that's it. Enjoy!