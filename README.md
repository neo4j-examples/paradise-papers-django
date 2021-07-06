# paradise-papers-django
A simple Django web app for searching the Paradise Papers dataset backed by Neo4j

[Welcome to Paradise Paper Search App’s Django + Neomodel Tutorial!](https://neo4j-examples.github.io/paradise-papers-django/)


# Requirements

- Python 3.4+
- Django 2.2+
- neo4j 3.5+, 4.0
- neo4j-driver 4.1.1
- neomodel 4.0.4

# Quickstart

First create an [sandbox database](https://sandbox.neo4j.com/), make sure to select **Paradise Papers by ICIJ** under **Pre-Built Data**, copy the credentials: username, password and bolt URL, you are going to need that later.

``` bash
# Clone this repository
git clone https://github.com/neo4j-examples/paradise-papers-django

# Go into the repository
cd paradise-papers-django 

# active your [virtual environment](https://docs.python.org/3/tutorial/venv.html) and install your dependencies
cd paradise_papers_search
pip install -r ../requirements.txt

# Run the app
export DATABASE_URL=bolt://<username>:<password>@<address>:7687 # update with the credentials from your sandbox database.
python manage.py runserver --settings=paradise_papers_search.settings.dev
```
# Registering Models in the Admin

In `paradise_papers_search/fetch_api/admin`, add the models you would like to explore using the admin:

```python
from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

from .models import Entity

class EntityAdmin(dj_admin.ModelAdmin):
    list_display = ("name",)
neo_admin.register(Entity, EntityAdmin)
```

Create the admin superuser:

```
./manage.py migrate
./manage.py createsuperuser
```

Run the app!

```
python manage.py runserver --settings=paradise_papers_search.settings.dev
```

Start searching at http://127.0.0.1:8000/

View the admin at http://127.0.0.1:8000/admin

While testing locally you may want to do `export ALLOWED_HOST=*`

# Quick Heroku Deployment with Neo4j Sandbox 

Create an sandbox database, make sure to select `Paradise Papers by ICIJ` under Pre-Built Data.
copy the database's username, password, and bolt URL.

Create a Heroku app, (for example, `paradise-papers`)
Go to the app's settings and add the following config vars:
`ALLOWED_HOST` : `paradise-papers.herokuapp.com`
`DATABASE_URL`: the credentials from your sandbox database in the following format `bolt://user:password@ip:port`

Clone the repository and navigate into the directory, add Heroku as a remote, and push to Heroku:
```
git clone git@github.com:neo4j-examples/paradise-papers-django.git
cd paradise-papers-django
git remote add heroku https://git.heroku.com/paradise-papers.git
git push heroku master
```

View your app at the URL you specified earlier.

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/admin-list.png "Admin List")
_________

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/admin-detail.png "Admin Detail")
_________

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img1.png "Search Home")
_________

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img2.png "Search Results")
_________
![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img3.png "Search details")
