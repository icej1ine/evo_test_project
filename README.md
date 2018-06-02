EVO test project repository. 

Installation:

1. install django
2. start django project
3. copy notes directory application
4. add 'notes' to INSTALLED_APPS
5. run manage.py makemigrations notes 
6. run manage.py migrate
7. include notes.urls to root url file ( path('', include('notes.urls')) )