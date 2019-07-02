# KeenDS Django backend

The front end code is located here:  https://github.com/edlutes/KeenDS-frontend


You should be able to run the 3 commands below to get the backend up and running. 

* python manage makemigrations (not needed if you grab the migrations from the repo)
* python manage migrate 
* python manage runserver
* follow frontend steps (basically ng serve -o)


A "deployed" version can be found at https://keends-frontend.herokuapp.com/
The rest API is located is https://keends-demo.herokuapp.com/

There is a showstopper of a bug between the database and the migrations as one of the slugFields is getting reduced to a max_length of 10 instead of the declared 255.  This prevents migration and therefore the database doesn't map correctly.  With no database the deployed REST API doesn't save anything, but it should work locally.

# REST API

The below options were all tested using Postman

PUT

127.0.0.1:8000/data/940?Observation_Date=1/1/2077&Retail_Price=5

GET

127.0.0.1:8000/data/940

Delete

127.0.0.1:8000/data/940

POST

127.0.0.1:8000/upload/<file>.csv
