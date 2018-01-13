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
    'entity': {
      'name': '',
      'incorporation_date': 'Incorporation',
      'jurisdiction': 'Jurisdiction',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'officer': {
      'name': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'intermediary': {
      'name': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'address': {
      'address': '',
      'countries': 'Linked To',
      'sourceID': 'Data From'
    },
    'other': {
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

      /**
       * Show related tab on the view.
       */
      this._activateTab = ko.observable(false);

      /**
       * Search an Filters related Stuff
       * @todo
       */
      this._search_api = '/search/';
      this._search_filters = {
        'q':'',
        'c':''
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

    /** @todo fetch from api the real data */
    fetch () {
      let data = mockup_data[this._node_type].data;
      data.forEach(row => {
        this._nodeSearchData.push(row);
      });
      this._page(this._page() + 1);
    }


    /** @todo clear search filter and data */
    clear () {
      this._nodeSearchData([]);
    }

  }

  /**
   * This is the actual ModelView app
   *
   */
  class SearchApp {
    constructor() {
      this._searchText = ko.observable('');

      // TODO
      this._countryList = ko.observableArray(mockup_data.countries);
      this._jurisdictionList = ko.observableArray(mockup_data.countries);

      // TODO
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
      window.searchApp = this; // TODO for testing, remove later
    }

    /** @todo initial Search */
    initNodeSeach () {
      this.toggleNodeSearch();
    }

    /** @todo fetch data from the _currentNodeSearch */
    continueNodeSearch () {
      this._currentNodeSearch.fetch();
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

  }

  // Create and bind our SearchApp
  ko.applyBindings(new SearchApp());
})()
