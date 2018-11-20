
(requirements in virtualenv= django, djangorestframework, googletrans)
Instructions for viewing:

activate virtual environment with

	$ source  env/bin/activate

cd into the translation_service/api directory

	execute the command python manage.py runserver

if run server is successful:

	navigate to http://127.0.0.1:8000/index/
	or localhost:8000/index

test it out!

This app is composed using the Django web framework as a backend and Django Rest Framework API layer. The API Layer can be accessed at http://127.0.0.1:8000/api/translations/.

The API is consumed by a React Application consisting of 3 components. The React app is included separately as a zip file for viewing the code. It is not needed to run the project; I have already installed the files from the project into the root level of the Django project. 

The Django folder contains a built, deployable version of the code and points to the build's index.html as the base view template for the project.

If any problems arise, please notify me so that I can take note and fix them or provide screenshots of working app. 