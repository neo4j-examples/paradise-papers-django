.. Paradise Paper Search documentation master file, created by
   sphinx-quickstart on Tue Jan 23 15:25:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

===================================================================
Welcome to Paradise Paper Search App's Django + Neomodel Tutorial!
===================================================================

Overview
--------

The aim of this tutorial is to demonstrate how to develop a web application using the Django framework backed by Neo4j, connecting them with the Neomodel driver. Neomodel is an Object Graph Mapper (OGM) for the Neo4j graph database.

The tutorial covers several topics, some of them are: how to configure Neomodel within a Django program, create models, query to the database, create an API. It provides best-practice guidance on implementing Neomodel.

The project is a web application to search for information on a Paradise Paper Graph Database. The data from the Database includes companies and people in more than 200 countries that are part of the Paradise Papers, Panama Papers, Bahama Leaks or the Offshore Leaks investigations.

The search of the program can filter the mentioned data by country, jurisdiction and/or data source. The approach adopted to make the program was to create a single-page web application, from which the data that is displayed will be obtained from an API. The API will fetch the data from the Neo4j database and return it as a JSON. This allows you to retrieve fast segments of data in several smaller requests, instead of making a single large request.

The types of data you can encounter when searching are: Entity , Officer , Intermediary , Address , Other.  Each of these data records is displayed as a `Node` within the database. If you are not familiar with the definition of a node, it is a graphic data record. There is also a term that we are going to use called `relationship` which is what connects the nodes with each other. An example of these `relationships` could be ``REGISTERED_ADDRESS`` , ``OFFICER_OF``. What’s more, each node will have `properties` , which is where the data is sotored. `Properties` are simple value pairs. eg: ``name: "Emil"``

.. toctree::
   :maxdepth: 2
   :glob:
   :numbered:
   :caption: Contents:

   tutorial/*

