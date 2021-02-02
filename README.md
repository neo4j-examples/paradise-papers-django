# paradise-papers-django
A simple Django web app for searching the Paradise Papers dataset backed by Neo4j

[Welcome to Paradise Paper Search App’s Django + Neomodel Tutorial!](https://neo4j-examples.github.io/paradise-papers-django/)


# Requirements

- Python 3.4+
- Django 2.2
- neo4j 3.0, 3.1, 3.2, 3.3
- neo4j-driver 1.2.1
- neomodel 4.0.2

# Quickstart

First create an [sandbox database](https://sandbox.neo4j.com/), make sure to select **Paradise Papers by ICIJ** under **Pre-Built Data**, copy the credentials: username, password and bolt URL, you are going to need that later.

``` bash
# Clone this repository
git clone https://github.com/neo4j-examples/paradise-papers-django

# Go into the repository
cd paradise-papers-django/paradise_papers_search
pip install -r ../requirements.txt

# Run the app
export DATABASE_URL=bolt://user:password@hostnameOrIP:port # update with the credentials from your sandbox database.
python manage.py runserver --settings=paradise_papers_search.settings.dev
```


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


![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img1.png "Search Home")
_________

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img2.png "Search Results")
_________
![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img3.png "Search details")
