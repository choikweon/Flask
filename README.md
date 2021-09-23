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
   + _*??*_ what does ```form.hidden_tag```() do?
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
 - Chapter 5 : User Logins
   + installs ```flask-login```, ```email-validator```
   + ```@login_required``` decorator flashes unwanted messages. if I want to fix this, do I have to fix ```flask-login``` from the source?
 - Chapter 6 : Profile Page and Avatars
   + the tutorial uses Gravatar service to generate a picture from md5 hash of the email, but I chose to use a random portrait from <a href="https://www.eveonline.com">EVE Online</a>. using url for the image : ```https://images.evetech.net/characters/95######/portrait``` where # is a digit.
   + adding more and more to the db. and making more templates and forms for them.
 - Chapter 7 : Error Handling
   + making template for some frequent errors : 404 and 500.
   + logs into ```./log``` when ```DEBUG=False``` in config.py
   + built another python container "debug" for ```python -m smtpd -n -c DebuggingServer localhost:8025```
   + python mock mail server did work on localhost, but did not in new debug container. could not find out the reason. whatever. removed the debug container.
   + at the end of the chapter, ```EditProfileForm``` overloads constructor to get a username argument passed to it. NOT fully understood. gotta study python inheritance and overloading part again.
 - Chapter 8 : Followers
   + added user-user m:n relation ```followed```
   + now my brain is getting overheated.
   + I do not understand how ORM and SQLAlchemy is working.
   + need to study ORM and SQLAlchemy, taking enough time. skipping for now.
   + _*!!*_ the code actuall generated a table called ```followers```. need to take a look at the code.
   + added ```tests.py``` for unit testing.
   + avatar test fails. sure.
   + the other tests passed but the test cases used SQLite. meaningless.
 - Chapter 9 : Pagination
   + added ```PostForm``` for posting
   + added ```explore``` function which renders index as explore page.
   + ```{% if form %}``` to switch between index and explore
   + pagination applied. using config ```POST_PER_PAGE```
   + _*??*_ uses ```request.args.get()``` the part I do not understand. comes from ```from flask import request```. need to study on it.
   + user/<username> page still shows temp posts. did I miss something?
   + when registering new user, the user is automatically logged in sometimes, or not logged in some of the times. need to check.
 - Chapter 10 : Email Support
   + ~~added ```.env.dev``` to ```.gitignore``` temporally, because the file now contains my Google account and password (which is for email server configuration). I don't want to publish them into a public github repo.~~
   + gmail does not allow 'low security apps' to access the account. should make gmail allow it in the account settings.
   + tested flask-email in a seperate environment, and got ```RuntimeError: Working outside of application context.``` message. need to study what an "app" is in Flask.
   + sending email works in ```with app.app_context():``` clause. app and context.
     - does run without the clause if it runs within the app. _*??*_
   + as email server is run in a seperate container, ```.env.dev``` is removed from ```.gitignore```
   + email server did not work as expected: forgot ```--host=0.0.0.0``` as mentioned in Ch. 4. 으악 짜증나.. 이것땜에 똑같은 삽질을 반복함..



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
 - psycopg2-binary
   + used for Flask-PostgreSQL data interface. to be exact, python library for psql. ```psycopg2``` package exists, but somehow ```psycopg2-binary``` should be installed instead. ```psycopg2``` throws some error when intalled.
   + not from the tutorial.
 - flask-login
   + user login module for Flask. keeps tracking the logged in user.
 - email-validator
   + as the name says...
 - flask-mail
   + sends email from the configured email server
 - pyjwt
   + python JSON web token
 - requests
   + sends http request
   + _*!!*_ not from the tutorial, but i installed it to make a seperate mail server container and send a mail request to it.


 updated Sep 23 2021