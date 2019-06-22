# CAJNvoice
This is the new and improved CAJNvoice. using the django web framework we will finally put the project on the web.

# Important Commands
** all commands must be run at the root (where manage.py is located) **
```
python manage.py runserver 
```
this will create a server on your localhost

```
python manage.py makemigrations
python manage.py migrate
```
use whatever is in the model.py to populate a sqllite3 database

```
python manage.py startapp <name>
```
this will create a new app that can be used on the server
