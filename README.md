# Flask

 - Chapter 1 : Hello, World!
   + installs *flask* and *python-dotenv*
 - Chapter 2 : Templates
   + template htmls go to */app/template* directory
   + does not really use traditional html, should be rendered thru ```render_template()```
   ```{{% cond or block %}}```
 - Chapter 3 : Web Forms
   + installs *flask-wtf*
   + code blocks replace traditional html and js form code inside ```<form>``` 
   + *??? what does ```form.hidden_tag```() do?* 


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
   


 updated Sep 08 2021