# term-deposit-sample
This is a sample exceution for the term deposit project
## installation
1. Clone the project
2. cd to term project
3. pip install -r requirements.txt
4. python manage.py runserver

Note: No need to migrate the project as we dont use any of the admin system and django mainframe

sudo cp supervisor.conf /etc/supervisor/conf.d/
sudo supervisorctl reread
sudo service supervisor restart all
sudo supervisorctl status