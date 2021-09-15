# Flask

**Chapters**

 - Chapter 1 : Hello, World!
   + installs ```flask``` and ```python-dotenv```
 - Chapter 2 : Templates
   + template htmls go to */app/template* directory
   + does not really use traditional html, should be rendered thru ```render_template()```
   ```{{% cond or block %}}```
 - Chapter 3 : Web Forms
   + installs ```flask-wtf```
   + code blocks replace traditional html and js form code inside ```<form>``` 
   + *??? what does ```form.hidden_tag```() do?* 
 - Chapter 4 : Database
   + installs ```flask-sqlalchemy``` and ```flask-migrate```
   + the tutorial uses SQLite, but I am trying to use PostgreSQL instead
   + psycopg2 error occurs when connecting to DB -> solved. use ```psycopg2-binary``` instead
   + Flask is to be run from localhost by default. when using docker, add ```--host=0.0.0.0``` option to access Flask server in the container (and do not forget to add ```EXPOSE portnum``` to Dockerfile)
   + network between containers use its name, for example, use ```db:``` instead of ```localhost:```
   + docker-compse up! Flask and PostgreSQL containers are up and linked to each other.
   + for multiple command for executing flask db migration, use
   ```
   command: bash -c "command 1 && command 2 && ... "
   ```
   + from the example microblog, ```User``` model crashes with PostgreSQL default table ```user```. need to avoid the name. Changed into ```Mbluser```
   + Passing ```flask shell```, seems not to be used in docker environment.



**Installed packages**

 - flask
   + flask itself
 - python-dotenv
   + saves environment variables at .flaskenv file
   + ```FLASK_APP=microblog.py```
 - flask-wtf
   + defines variables as ```app.config[dictionary_key]```
   + can use ```config.py``` class
   + supports web form
      ```python
      from flask_wtf import FlaskForm
      from wtforms import StringField, PasswordField, BooleanField, SubmitField
      from wtforms.validators import DataRequired
      ```
 - flask-sqlalchemy
   + flask wrapper for SQLAlchemy, which is an <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">Object Relational Mapper</a>
   + support most of relational DB, such as MySQL, PostgreSQL, SQLite
   + ok. PostgreSQL. am I going to come back here for flask when I study PostgreSQL? -> Yes. been there and now here.
 - flask-migrate
   + created by Miguel Grinberg himself
   + flask wrapper for Albemic, which is a DB migration framework for SQLAlchemy


 updated Sep 15 2021