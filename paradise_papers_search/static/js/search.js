/**
 * Paradise Paper Search App
 *
 * @author: Junior Báez
 * @version: 0.1.0
 * @requires ko - global KnowckoutJS object
 */
(() => {
  'use strict';

  /**
  *  Node types mapping
  *  {
  *    '<node_type>': {
  *        '<property_name>': '<Property Label>',
  *        ...
  *    },
  *   ...
  *  }
  */
  const node_types = {
    'Entity': {
      'name': '',
      'incorporation_date': 'Incorporation',
      'jurisdiction_description': 'Jurisdiction',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'Officer': {
      'name': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'Intermediary': {
      'name': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'Address': {
      'address': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'Other': {
      'name': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    }
  };

  /**
   * The purpose of this class is to fetch data.
   * Each instance of the class will search and filter a specific node type.
   *
   * @param node_type
   * @param node_properties
   */
  class NodeSearch {
    constructor(node_type, node_properties) {
      /**
       * Type of Nodes
       */
      this._node_type = node_type;
      /**
       * List of node properties
       *
       * [
       *  {
       *    property_name: <propertyname>,
       *    property_label: <Property Label>
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

      /*count*/
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
       * Search an Filters related Stuff
       */
      this._search_api = '/fetch/';

      this._search_filters = {
        't': this._node_type,
      };

      this._page = ko.observable(0);
      this._total = ko.observable(0);


      // Construct _nodePropertyList defined above
      for (var property_name in node_properties) {
        if (node_properties.hasOwnProperty(property_name)) {
          this._nodePropertyList.push({
            property_name,
            'property_label': node_properties[property_name]
          });
        }
      }
    }
    /*
    * Set the filters
    * @param: newFilters - Object of filters to change
    * @return: this._search_filters
    */
    setFilters(newFilters) {
      return Object.assign(this._search_filters, newFilters)
    }

    fetch () {
      this._fetchState(true);

      $.getJSON(
        this._search_api + 'nodes',
        this.setFilters({ 'p': this._page() + 1 })
      )
      .done(nodes => {
        nodes.response.data.forEach(node => {
          this._nodeSearchData.push(node.node_properties);
        });
        this._page(this._page() + 1);
      })
      .fail(() => {
        /*TODO Handle errors */
        console.log("Fetch error");
      })
      .always(() => {
        this._fetchState(false);
      });
    }


    fetchCount() {
      $.getJSON(
        this._search_api + 'count',
        this._search_filters
      )
      .done(nodes => {
        this._nodeSearchDataCount(nodes.response.data.count)
      })
      .fail(() => {
        /*TODO Handle errors */
        console.log("Fetch error");
      })
    }



    /** @todo init search filter and data */
    clear () {
      this._nodeSearchData([]);
      this._page(0);
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
      this._filters = {};
      this._nodeSearchList = ko.observableArray([]);

      // Construct NodeSearch instances
      for (var node_type in node_types) {
        if (node_types.hasOwnProperty(node_type)) {
          this._nodeSearchList.push(
            new NodeSearch(node_type, node_types[node_type])
          );
        }
      }

      this._currentNodeSearch = this._nodeSearchList()[0];
      this.fetchCountries();
      this.fetchJurisdictions();
      window.searchApp = this; // TODO for testing, remove later
    }

    /** @todo initial Search */
    initNodeSeach () {

      this._initialSearchDone(true)
      this._nodeSearchList().forEach(nodeSearch => {

        nodeSearch.clear();
        nodeSearch.setFilters({
          'q': this._searchText(),
          'c': this._filters['country'],
          'j': this._filters['jurisdiction'],
        });

        nodeSearch.fetchCount();
      });
      this.toggleNodeSearch();
    }

    /** @todo Toggle _currentNodeSearch and tab */
    toggleNodeSearch (nodeSearch) {

      if (nodeSearch) {
        this._currentNodeSearch._activateTab(false);
        this._currentNodeSearch = nodeSearch;
      }

      this._currentNodeSearch._activateTab(true);

      if (this._currentNodeSearch._page() === 0) {
        this._currentNodeSearch.fetch();
      }
    }

    fetchCountries() {
      $.getJSON(
        'fetch/countries'
      )
      .done(countries => {
        countries.response.data.forEach(country => {
          this._countryList.push(country);
        });
      })
      .fail(() => {
        /*TODO Handle errors */
        console.log("Fetch error");
      })
    }

    fetchJurisdictions() {
      $.getJSON(
        'fetch/jurisdictions'
      )
      .done(jurisdictions => {
        jurisdictions.response.data.forEach(jurisdiction => {
          this._jurisdictionList.push(jurisdiction);
        });
      })
      .fail(() => {
        /*TODO Handle errors */
        console.log("Fetch error");
      })
    }
  }

  // Create and bind our SearchApp
  ko.applyBindings(new SearchApp());
})()
