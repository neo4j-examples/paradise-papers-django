const mockup_data = {
  'Entity': {
    "sourceID": "Panama Papers",
    "address": "ORION HOUSE SERVICES (HK) LIMITED ROOM 1401; 14/F.; WORLD COMMERCE  CENTRE; HARBOUR CITY; 7-11 CANTON ROAD; TSIM SHA TSUI; KOWLOON; HONG KONG",
    "jurisdiction": "SAM",
    "service_provider": "Mossack Fonseca",
    "countries": "Hong Kong",
    "jurisdiction_description": "Samoa",
    "valid_until": "The Panama Papers data is current through 2015",
    "ibcRUC": "25221",
    "name": "TIANSHENG INDUSTRY AND TRADING CO., LTD.",
    "country_codes": "HKG",
    "incorporation_date": "23-MAR-2006",
    "node_id": "10000001",
    "status": "Defaulted"
  },
  'Address': {
    "sourceID": "Bahamas Leaks",
    "country_codes": "BHS",
    "valid_until": "The Bahamas Leaks data is current through early 2016.",
    "address": "LYFORD CAY HOUSE, 3RD FLOOR, LYFORD CAY, P.O. BOX N-3024, NASSAU, BAHAMAS",
    "countries": "Bahamas",
    "node_id": "24000005"
  },
  'Intermediary': {
    "sourceID": "Panama Papers",
    "valid_until": "The Panama Papers  data is current through 2015",
    "name": "DAVID, RONALD",
    "country_codes": "MCO",
    "countries": "Monaco",
    "node_id": "11000003",
    "status": "SUSPENDED"
  },
  'Officer': {
    "sourceID": "Panama Papers",
    "name": "KIM SOO IN",
    "country_codes": "KOR",
    "valid_until": "The Panama Papers data is current through 2015",
    "countries": "South Korea",
    "node_id": "12000001"
  },
  'Other': {
    "sourceID": "Paradise Papers - Aruba corporate registry",
    "note": "Closed date stands for Cancelled date.",
    "valid_until": "Aruba corporate registry data is current through 2016",
    "name": "ANTAM ENTERPRISES N.V.",
    "country_codes": "ABW",
    "countries": "Aruba",
    "node_id": "85004929"
  }
};

// Make each node an array of 20 repeated element
for (let node in mockup_data) {
  if (mockup_data.hasOwnProperty(node)) {
    let data = mockup_data[node];
    mockup_data[node] = {
      status: '200',
      rows: 20,
      data: []
    };
    for (let i = 0; i < mockup_data[node].rows; i++) {
      mockup_data[node].data.push({
          node_properties: data
      });
    }
  }
}

mockup_data.countries = [
  'Aruba',
  'China',
  'Japon',
  'Bahamas',
  'Panama'
]

mockup_data.jurisdictions = [
  'Aruba',
  'Bahamas',
  'Dubai'
]

mockup_data.dataSource = [
    'Bahamas Leaks',
    'Offshore Leaks',
    'Panama Papers'
]
