# Configuring local development branding

- pyvenv env
- source env/bin/activate
- pip install -r requirements.txt

python manage.py migrate

#Gerar e Comilar Tradução
python manage.py makemessages -l pt_BR
python manage.py compilemessages

python manage.py runserver


# server requirements

- python 3
- virtualenv
- pip3
- uwsgi
- uwsgi_plugin34
- gettext

#Setup steps

- Create web app user or use the default
- chown permissions
- Create uwsgi ini file
- Create uwsgi startup script in emperor mode
- Create nginx app config file

#Services
start uwsgi
service nginx restart
	#(uwsgi startup script)
start uwsgi 
- Se tiver alteração de tradução
python manage.py compilemessages

#Check if uwsgi is running with configuration
ps -ef | grep [script init file name e.g uwsgi]



