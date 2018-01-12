/**
 * Paradise Paper Search App
 *
 * @author: Junior Báez
 * @version: 0.1.0
 * @requires ko - global KnowckoutJS object
 */
(() => {
  'use strict';

  // Type of nodes that can be searched
  const node_types = [
    'entity',
    'address',
    'intermediary',
    'officer',
    'other'
  ];

  /**
   * The purpose of this class is to fetch data.
   * Each instance of the class will search and filter a specific node type.
   */
  class NodeSearch {
    constructor(node_type) {
      this._node_type = node_type;
      this._search_api = '/search/';
      this._search_filters = {
          'q':'',
          'c':''
      };

      this._nodeSearchData = ko.observableArray([]);
      this._page = ko.observable(0);
      this._total = ko.observable(0);
      this._activateTab = ko.observable(false);
    }

    /** @todo fetch from api */
    fetch () {
      let data = mockup_data[this._node_type].data;
      data.forEach(row => {
        this._nodeSearchData.push(row);
      });
      this._page(this._page()+1);
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
      
      this._countryList = ko.observableArray(mockup_data.countries);
      this._jurisdictionList = ko.observableArray(mockup_data.countries);

      this._filters = {
        'c': '',
        '': '',
        '': '',
        '': '',
      };

      this._nodeSearchList = ko.observableArray([]);

      node_types.forEach(node_type => {
        this._nodeSearchList.push(new NodeSearch(node_type));
      });

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
