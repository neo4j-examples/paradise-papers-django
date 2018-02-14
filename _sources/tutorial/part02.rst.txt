============================
Set the NeoModel database
============================

On this section, we are going to install Neo4j on our local machine and show how
you are going to connect it with our app. First, we use the `paradise-papers`
database for the example app. Here_ is a quick set up for the Desktop app that
will bring the database included

    .. _here: https://offshoreleaks.icij.org/pages/database

Follow the steps of the wizard to install the app. If you want a more deep look
of Neo4j; here is the official guide_ that you can follow to get Neo4j working
on your local machine.

    .. _guide: https://neo4j.com/developer/get-started/

On the app example, we are going to use the LEAKS DATABASE. This is the data
from the  Panama Papers, the Offshore Leaks, the Bahamas Leaks provided by the
ICIJ(International Consortium of Investigative Journalists) here are some
information about the ICIJ_ and the offshore_ leaks.

    .. _icij: https://www.icij.org/about/
    .. _offshore: https://offshoreleaks.icij.org/

On this tutorial, we are going to concentrate on replicating the offshore leaks
search app and it's important that you know the entities that we are going to
handle the app.

Offshore Entity:
A company, trust or fund created in a low-tax, offshore jurisdiction by an
agent.

Officer:
A person or company who plays a role in an offshore entity.

Intermediary:
A go-between for someone seeking an offshore corporation and an offshore service
provider -- usually a law-firm or a middleman that asks an offshore service
provider to create an offshore firm for a client.

Address:
Contact postal address as it appears in the original databases obtained by ICIJ.

Definitions provided by
https://offshoreleaks.icij.org/pages/about#terms_definition

We use the paradise-papers database for the example app. Here_ is a quick set up
for the Desktop app that will bring the database included

    .. _here: https://offshoreleaks.icij.org/pages/database

After you have Neo4j up and running we only need to create the connection
between Django and the database to do this Neomodel will give us a hand.

Go to the settings file on your project and import config from newmodel::

    from neomodel import config

Then you need to delete the default database setting::

    # Database
    # https://docs.djangoproject.com/en/1.11/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

And now you only need to set the Neo4j database on the config in the settings
like this::

    #Connect to Neo4j Database
    config.DATABASE_URL = 'bolt://neo4j:neo4j@localhost:7687'

Now you are all set just need to run your local server with the runserver
command::

    python manage.py runserver
