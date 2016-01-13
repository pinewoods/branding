# Configuring local development branding

- pyvenv env
- source env/bin/activate
- pip install -r requirements.txt

python manage.py migrate

python manage.py runserver


# server requirements

- python 3
- virtualenv
- pip3
- uwsgi
- uwsgi_plugin34

#Setup steps

- Create web app user or use the default
- chown permissions
- Create uwsgi ini file
- Create uwsgi startup script in emperor mode
- Create nginx app config file

#Services
service nginx restart
start uwsgi (uwsgi startup script)

#Check if uwsgi is running with configuration
ps -ef | grep [script init file name e.g uwsgi]