# paradise-papers-django
A simple Django web app for searching the Paradise Papers dataset backed by Neo4j

[Welcome to Paradise Paper Search App’s Django + Neomodel Tutorial!](https://neo4j-examples.github.io/paradise-papers-django/)


# Requirements

- Python 3.4+
- Django 1.11
- neo4j 3.0, 3.1, 3.2, 3.3
- neo4j-driver 1.2.1
- neomodel 3.2.5


# Quickstart

``` bash
# Clone this repository
git clone https://github.com/neo4j-examples/paradise-papers-django

# Go into the repository
cd paradise-papers-django
cd paradise_papers_search

# Run the app(after installing requirements)
python manage.py runserver --settings=paradise_papers_search.settings.dev
```


![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img1.png "Search Home")
_________

![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img2.png "Search Results")
_________
![alt text](https://github.com/neo4j-examples/paradise-papers-django/blob/master/docs/tutorial/_images/part07-img3.png "Search details")
