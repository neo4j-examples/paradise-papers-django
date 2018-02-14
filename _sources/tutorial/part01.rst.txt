=======================
Set up the environment.
=======================

The following section will have the steps we need to set our local
environment, so we can begin to work on your Django-Neomodel implementation. If
you want a point to start, we provide a base app to begin the tutorial.

First clone the paradise-papers-django_ repo.

    .. _paradise-papers-django: https://github.com/neo4j-examples/paradise-papers-django

After you download the repo go to the ``start_app`` branch, and you will get a
working Django application that will serve as a starting point.

.. [*] Note:
    If we use the start branch, mentioned before, we only will get the front-end
    of the app.

Set your virtualenv
===================

First, we will need Python 3.6 and pip installed on your local environment. Here
is the official download page for Python_.

    .. _Python: https://www.python.org/downloads/

Here is a quick tutorial on how to install pip_.

    .. _pip: https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py

Now we have everything we need to create our virtualenv. On the next part we are
going to introduce the basics to get your app running; if you want more
information check this virtualenv_ tutorial.

    .. _virtualenv: https://virtualenv.pypa.io/en/stable/

First go to your app folder in the case of the ``paradise-papers-django``
project, we need to be on the main folder ``localPath/ paradise-papers-django``
and run the following command to install virtualenv::

    pip install virtualenv

You can use this pip command to check the dependencies installed::

    pip freeze

After the virtualenv is installed; we need to create a virtual environment for
the app. On the same folder that the virtualenv is installed we only need to run
the following command::

    virtualenv .

The dot means that is going to install your virtual environment on the current
folder, but you can specify the path that you need to create your virtual
environment.

After your virtual environment is ready your directory should look like this if
you are using the example app::

    ├── paradise-papers-django/
    |   ├── docs/
    │   ├── Include/
    │   ├── Lib/
    │   ├── paradise_papers_search/
    |   ├── LICENSE
    │   ├── pip-selfcheck.json
    │   ├── PULL_REQUEST_TEMPLATE.md
    |   ├── README.md

Now we need to activate your brand new virtual environment with the following
command::

    .\Scripts\activate

On Linux and Mac::

    source bin/activate

Now you are in your new virtual environment!!!

Add project dependencies
========================

The next step is to install the other dependencies that we need. For this, we
can use our requirement file if you are using the example app otherwise, we
need to install the following dependencies using the
``pip install <name>===<version>`` command::

    Django==1.11.2
    django-neomodel==0.0.4
    neo4j-driver==1.2.1
    neomodel==3.2.5

If you’re using your own requirement file you can use this command to get all
your dependencies::

    pip install -r /path/to/requirements.txt

If you're using our starting app; go to the paradise-papers-search folder and
run this command::

    pip install -r requirements.txt

Now you have all dependencies that you need for this implementation!!!!
