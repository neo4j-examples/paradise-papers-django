/**
 * Paradise Paper Search App
 *
 * @author: Junior Báez
 * @version: 0.2.0
 * @requires ko - global KnowckoutJS object
 *
 * @todo Implement RequireJS and split app into modules
 * @todo Implement page routing, possibly with Page.js
 * @todo Write JSDocs
 *
 */
(() => {
  'use strict';

  /**
  *  Nodes Settings metadata
  *  {
  *    '<node_type>': {
  *        '<property_name>': ['<Property Label>', <boolDisplayTable>],
  *        ...
  *    },
  *   ...
  *  }
  *
  * @todo Add missing properties
  */


  const nodes_settings = {
    'Entity': {
      'name': ['', true],
      'incorporation_date': ['Incorporation', true],
      'jurisdiction': ['Jurisdiction', true],
      'countries': ['Linked To', true],
      'sourceID': ['Data From', true]
    },
    'Officer': {
      'name': ['', true],
      'countries': ['Linked To', true],
      'sourceID': ['Data From', true]
    },
    'Intermediary': {
      'name': ['', true],
      'countries': ['Linked To', true],
      'sourceID': ['Data From', true]
    },
    'Address': {
      'address': ['', true],
      'countries': ['Linked To', true],
      'sourceID': ['Data From', true]
    },
    'Other': {
      'name': ['', true],
      'countries': ['Linked To', true],
      'sourceID': ['Data From', true]
    }
  };

  /**
   * Representation of a Node
   *
   * @param node_type
   * @param node_properties
   */
  class Node {

    constructor(node_type, node_id_or_properties) {
      this._node_type = node_type;
      this._node_properties = {};
      this._node_connections = ko.observableArray();
      this._fetchStateNode = ko.observable(false);

      if (typeof node_id_or_properties === 'number') {
        this._node_id = node_id_or_properties;
      } else {
        this._node_id = node_id_or_properties.node_id;
        this._node_properties = node_id_or_properties;
      }
    }

    /**
     * Fetch connected nodes.
     */
    fetchConnections () {
      this._fetchStateNode(true);
      $.getJSON(
        '/fetch/node',
        {
          'id': this._node_id,
          't': this._node_type
        }
      )
      .done(nodeFetch => {
        this._node_properties = nodeFetch.response.data.node_properties;
        nodeFetch.response.data.node_connections.forEach(conns => {
          conns.nodes_count = conns.nodes_related.length;
          // check if the current connections group really has nodes
          if (conns.nodes_count > 0) {
            // Convert nodes_related to instaces of the class Node
            conns.nodes_related = conns.nodes_related.map((n) => {
              return new Node(conns.nodes_type, n.node_properties);
            });
            this._node_connections.push(conns);
          }
        });
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
      .always(() => {
        this._fetchStateNode(false);
      });
    }
  }

  /**
   * The purpose of this class is to fetch data.
   * Each instance of the class will search and filter a specific node type.
   *
   * @param node_type
   * @param node_settings
   */
  class NodeSearch {

    constructor(node_type, node_settings) {
      /**
       * Type of Nodes to fetch
       */
      this._node_type = node_type;

      /**
       * List of node properties metadata
       *
       * [
       *  {
       *    property_name: <propertyname>,
       *    property_label: <Property Label>
       *    property_display_table: <bool>
       *  },
       *  ...
       * ]
       */
      this._nodePropertyList = [];

      /**
       * Container of Nodes
       * as an observableArray in order to dynamicly update the view
       */
      this._nodeSearchData = ko.observableArray();

      /**
       * How many nodes have being fetched
       */
      this._nodeSearchDataCount = ko.observable(-1);

      /**
       * Show related tab on the view.
       */
      this._activateTab = ko.observable(false);

      /**
       * State of the current fetch
       */
      this._fetchState = ko.observable(false);

      /**
       * API endpoint
       */
      this._search_api = '/fetch/';

      /**
       * Filter the Nodes that will be fetched
       */
      this._search_filters = {
        't': this._node_type,
      };

      /**
       * Last page fetched
       */
      this._last_page_fetched = ko.observable(0);

      // Construct _nodePropertyList defined above
      for (let property_name in node_settings) {
        if (node_settings.hasOwnProperty(property_name)) {
          this._nodePropertyList.push({
            property_name,
            'property_label': node_settings[property_name][0],
            'property_display_table': node_settings[property_name][1]
          });
        }
      }
    }

   /**
    * Set the filters
    *
    * @param: newFilters - Object of filters to change
    * @return: this._search_filters
    */
    setFilters(newFilters) {
      return Object.assign(this._search_filters, newFilters);
    }

    fetch () {
        // Test code
        let mock = mockup_data[this._node_type].data;
        mock.forEach(row => {
            this._nodeSearchData.push(new Node(this._node_type, row.node_properties));
        });
        return;
        // /Test code
      this._fetchState(true);

      $.getJSON(
        this._search_api + 'nodes',
        this.setFilters({ 'p': this._last_page_fetched() + 1 })
      )
      .done(nodes => {
        nodes.response.data.forEach(node => {
          this._nodeSearchData.push(
            new Node(this._node_type, node.node_properties)
          );
        });
        this._last_page_fetched(this._last_page_fetched() + 1);
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
      .always(() => {
        this._fetchState(false);
      });
    }

    fetchCount() {
        // Mock Data
        return this._nodeSearchDataCount(0);

      $.getJSON(
        this._search_api + 'count',
        this._search_filters
      )
      .done(nodes => {
        this._nodeSearchDataCount(nodes.response.data.count)
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
    }

    /**
     * Clear and reset
     */
    clear () {
      this._nodeSearchData([]);
      this._last_page_fetched(0);
      this._nodeSearchDataCount(-1);
      this.setFilters({
          'q': '',
          'c': '',
          'j': '',
          'p': 0,
      });
    }

  }

  /**
   * This is the actual ModelView app
   *
   */
  class SearchApp {

    constructor() {
      this._initialSearchDone = ko.observable(false);
      this._searchText = ko.observable('');
      this._countryList = ko.observableArray();
      this._jurisdictionList = ko.observableArray();
      this._dataSourceList = ko.observableArray();
      this._filters = {};

      // Node details tracking
      this._nodesCache = {};
      this._currentNode = ko.observable();

      // Construct NodeSearch instances
      this._nodeSearch = {};
      this._nodeSearchList = ko.observableArray([]);
      for (let node_type in nodes_settings) {
        if (nodes_settings.hasOwnProperty(node_type)) {
          const nodeSearch = new NodeSearch(node_type, nodes_settings[node_type]);
          this._nodeSearch[node_type] = nodeSearch;
          this._nodeSearchList.push(nodeSearch);
        }
      }

      this._currentNodeSearch = this._nodeSearchList()[0];
      this.fetchCountries();
      this.fetchJurisdictions();
      this.fetchDataSource();
    }

    /**
     * Init Search
     */
    initNodeSeach () {
      this._nodeSearchList().forEach(nodeSearch => {

        nodeSearch.clear();
        nodeSearch.setFilters({
          'q': this._searchText(),
          'c': this._filters['country'],
          'j': this._filters['jurisdiction'],
          's': this._filters['dataSource'],
        });

        nodeSearch.fetchCount();
      });

      this._initialSearchDone(true)
      this.displayNodeSearch();
    }

    /**
     * Toggle _currentNodeSearch to show on the view
     */
    displayNodeSearch (nodeSearch) {
      if (nodeSearch) {
        this._currentNodeSearch._activateTab(false);
        this._currentNodeSearch = nodeSearch;
      }

      this._currentNodeSearch._activateTab(true);

      if (this._currentNodeSearch._last_page_fetched() === 0) {
        this._currentNodeSearch.fetch();
      }
    }

    /**
     * Toggle _currentNode to show on the view
     */
    displayNode (node) {
      const node_id = node._node_id;

      // Show node from cache if connections have being fetched
      if (this._nodesCache.hasOwnProperty(node_id)) {
        this._currentNode(this._nodesCache[node_id]);
        return;
      }

      // Fetch node connections once
      node.fetchConnections();
      this._currentNode(node);
      this._nodesCache[node_id] = node;
    }

    fetchCountries() {
        // Test code
        mockup_data.countries.forEach(country => {
            this._countryList.push(country);
        });

        return this._countryList;
        // /Test code
      $.getJSON(
        'fetch/countries'
      )
      .done(countries => {
        countries.response.data.forEach(country => {
          this._countryList.push(country);
        });
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
    }

    fetchJurisdictions() {
        // Test code
        mockup_data.jurisdictions.forEach(jurisdiction => {
            this._jurisdictionList.push(jurisdiction);
        });
        // /Test code
        return this._jurisdictionList;

      $.getJSON(
        'fetch/jurisdictions'
      )
      .done(jurisdictions => {
        jurisdictions.response.data.forEach(jurisdiction => {
          this._jurisdictionList.push(jurisdiction);
        });
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
    }

    fetchDataSource() {
        // mock data
        mockup_data.dataSource.forEach(dataSource => {
            this._dataSourceList.push(dataSource);
        });

        return this._dataSourceList;

      $.getJSON(
        'fetch/datasource'
      )
      .done(dataSources => {
        dataSources.response.data.forEach(dataSource => {
          this._dataSourceList.push(dataSource);
        });
      })
      .fail(() => {
        /** @todo Handle errors */
        console.log("Fetch error");
      })
    }
  }

  // Create and bind our SearchApp
  ko.applyBindings(new SearchApp());
})();
