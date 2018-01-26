==============================
How to create the base models.
==============================

Create a new app for the API: 
==============================
Right now, we need to create  a Django app which is going to be use to create the search API and, with it, we will define our models classes.

To create this new app, it is needed to run this command: 

``python manage.py startapp fetch_api``

Where ``fetch_api`` is the name of the application we are creating, if you prefer you can use any other name.  This will create a new folder inside the Django project directory, and the structure of it is: ::

    ├── fetch_api/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    |   ├── models.py
    │   ├── migrations/
    │   │   └── __init__.py 


Create The Models Directory:
==============================

On The ``fetch_api`` folder, first, we need to remove the ``models.py`` file. Then we need to create a new folder called ``models``.  Inside the folder, you will need to add the files with the structure of the nodes. Each file will have the essential fields and methods of the data stored in Neo4j database. 

.. [*] Note: Before we start creating our models we need to create a  ``__init__.py`` file inside the model’s folder so Python treat the directory as a module

Start creating The Models Files:
===================================
To start we will create an ``entity.py`` file: 

1. The first step is to add the imports needed::

    from neomodel import (
        StringProperty,
        StructuredNode,
        RelationshipTo,
        RelationshipFrom
    )

2. Create a class for the node call Entity. We are connecting to a Neo4j database instead of the regular Django database; therefore,  we are going to use  ``StructuredNode``.  This is the equivalent of  ``models.Model`` which is usually  used when creating a Models class in Django. When using ``StructuredNode`` , neomodel automatically creates a label for each class using it with the corresponding indexes and constraints.

 If you need ``ModelForm``, you will need to change ``StructuredNode`` to ``DjangoNode``. Also, you will need to add a ‘Meta’ class. For more reference see the documentation for django-neomodel_

    .. _django-neomodel: https://github.com/neo4j-contrib/django-neomodel

    ``class Entity(StructuredNode):``


3. The next step is to add the properties for the node. Each node property in the Neo4j database should be a property in the model class.

The properties of  the ``Entity`` node in the database have the following scheme::

        {
          "sourceID": "Panama Papers",
          "address": "MEI SERVICES LIMITED ROOM E; 6TH FLOOR; EASTERN COMMERCIAL CENTRE; 395-399 HENNESSY ROAD HONG KONG",
          "jurisdiction": "SAM",
          "service_provider": "Mossack Fonseca",
          "countries": "Hong Kong",
          "jurisdiction_description": "Samoa",
          "valid_until": "The Panama Papers data is current through 2015",
          "ibcRUC": "25475",
          "name": "JIE LUN INVESTMENT LIMITED",
          "country_codes": "HKG",
          "incorporation_date": "10-APR-2006",
          "node_id": "10000020",
          "status": "Active,
        }

Therefore, the structure of the ``Entity`` class should be::

    class Entity(StructuredNode):
        sourceID                           = StringProperty()
        address                            = StringProperty()
        jurisdiction                       = StringProperty()
        service_provider                   = StringProperty()
        countries                          = StringProperty()
        jurisdiction_description           = StringProperty()
        valid_until                        = StringProperty()
        ibcRUC                             = StringProperty()
        name                               = StringProperty()
        country_codes                      = StringProperty()
        incorporation_date                 = StringProperty()
        node_id                            = StringProperty(index = True)
        status                             = StringProperty()

4. Add the relationships for the node::

    officers                 = RelationshipFrom('.officer.Officer', 'OFFICER_OF')
    intermediaries           = RelationshipFrom('.intermediary.Intermediary', 'INTERMEDIARY_OF')
    addresses                = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    others                   = RelationshipFrom('.other.Other', 'CONNECTED_TO')

.. [*]  You can find the nodes relation by calling on the database: CALL db.schema(). To access your local database click HERE_. note: you need to have it up and running to work. 

    .. _HERE: http://localhost:7474/browser/ 



How **RelationshipFrom** and **RelationshipTo** works:

        1. The first parameter is the type of node you want to connect. e.g ``.officer.Officer``
        2. The second parameter is the relationship type. e.g. ``OFFICER_OF``


* **RelationshipFrom** is an INCOMING relationship 
* **RelationshipTo**  is an OUTGOING relationship 
* Also, there is one call **Relationship** which can be either

If  **RelationshipFrom**  be illustrated,  the output would be something like: 

.. image:: images/relfrom.png
   :width: 100%
   :alt: alternate text


Repeat these steps for each node class you wish to create. On this program, those would be: ``address.py``, ``intermediary.py``, ``officer.py``, and ``other.py``. You must add the following code to each of the files:

address.py ::

    from neomodel import (
        StringProperty,
        StructuredNode,
        RelationshipFrom
    )

    class Address(StructuredNode):
        sourceID       = StringProperty()
        country_codes  = StringProperty()
        valid_until    = StringProperty()
        address        = StringProperty()
        countries      = StringProperty()
        node_id        = StringProperty()
        officers       = RelationshipFrom('.officer.Officer', 'REGISTERED_ADDRESS')
        intermediaries = RelationshipFrom('.intermediary.Intermediary', 'REGISTERED_ADDRESS')   


intermediary.py::

    from neomodel import (
        StringProperty,
        StructuredNode,
        RelationshipTo
    )

    class Intermediary(StructuredNode, NodeUtils):
        sourceID      = StringProperty()
        valid_until   = StringProperty()
        name          = StringProperty()
        country_codes = StringProperty()
        countries     = StringProperty()
        node_id       = StringProperty()
        status        = StringProperty()
        entities      = RelationshipTo('.entity.Entity', 'INTERMEDIARY_OF')
        addresses     = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')



officer.py::

    from neomodel import (
        StringProperty,
        StructuredNode,
        RelationshipTo,
    )

    class Officer(StructuredNode):
        sourceID      = StringProperty()
        name          = StringProperty()
        country_codes = StringProperty()
        valid_until   = StringProperty()
        countries     = StringProperty()
        node_id       = StringProperty()
        addresses     = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
        entities      = RelationshipTo('.entity.Entity', 'OFFICER_OF')

other.py::

    from neomodel import (
        StringProperty,
        StructuredNode,
        RelationshipTo,
    )

    class Other(StructuredNode):
        sourceID    = StringProperty()
        name        = StringProperty()
        valid_until = StringProperty()
        node_id     = StringProperty()
        countries   = StringProperty()
        addresses   = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')

Modify the __init__.py file:
==================================
Now we need to add a little bit of code to the __init__.py. If you noticed in the previous code, we refer to other classes but we did no import them. e.g : ``.officer.Officer``. This means that it should not work because the program doesn't know what that is; Therefore, we are going to add all the imports to the init file so that each model has all the imports ::

    from .entity import Entity
    from .address import Address
    from .intermediary import Intermediary
    from .officer import Officer
    from .other import Other


    MODEL_ENTITIES = {
        'Entity': Entity,
        'Address': Address,
        'Intermediary': Intermediary,
        'Officer': Officer,
        'Other': Other
    } 


Create constraints or indexes: 
==================================

Creating constraints and labels have to be done after you add/change the node definitions.
The command that you will need to use is: 

    ``python manage.py install_labels``

In this case, since we added `index=True` on the node_id property the output would create indexes on each of the property mentioned:

.. image:: images/indexes.png
   :width: 100%
   :alt: alternate text

.. [*]  Note: manage.py intall_labels works like manage.py migrate

After doing these steps, the structure folder of the project changed. Right now the structure of the fetch_api app should be::

    ├── fetch_api/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   │   └── __init__.py
    │   ├── models/
    │   │   ├── __init__.py
    │   │   ├── address.py
    │   │   ├── entity.py
    │   │   ├── intermediary.py
    │   │   ├── officer.py
    │   │   └── other.py
