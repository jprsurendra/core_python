import http.client
import requests


conn = http.client.HTTPSConnection("api.maersk.com")

headers = { "Accept": "*/*", 'Consumer-Key': "MCcuYysgoC4DeIDhPh7n3BpMf1BHyWTJ" }

# params = { "UNLocationCode": "SADMM" }
params = { "UNLocationCode": "GBLON" }
# params = { "countryCode": "GB"}
# params = { "UNLocationCode": "INNSA" , "countryCode": "IN", "locationType": "CITY" }
# params = { "UNLocationCode": "CNPDG", 'countryCode': 'CN' }
url = "https://api.maersk.com/reference-data/locations"
r = requests.get(url, headers=headers, params=params)
# r = requests.get(url+"/?UNLocationCode=SADMM", headers=headers)
# res = requests.get(url=api_url, params=payload, headers=headers, verify=verify)
print(r.json())
'''
[
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CITY',
    'locationName': 'Dammam',
    'carrierGeoID': '1OIFQMS1FSLFJ',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'DEPOT',
    'locationName': 'Dammam IACC',
    'carrierGeoID': '2Q09IEJVC0UMV',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'KANOO TERMINAL SERVICES 1',
    'carrierGeoID': '2EDLZ07X1BXR7',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'Crecent Terminal Services',
    'carrierGeoID': '2EN5J0KTJFCMB',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'RAIL TERMINAL',
    'locationName': 'Damam Rail Terminal',
    'carrierGeoID': 'SOBNV51Y9JSAK',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'DEPOT',
    'locationName': 'Dammam 1',
    'carrierGeoID': '1TJ6ISO9FPACN',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'Saudi Global Ports',
    'carrierGeoID': 'W2FNWWDSUJQVK',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'DEPOT',
    'locationName': 'IMA Dammam Depot',
    'carrierGeoID': 'MCPH7CALMPSET',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'Sultan Transport Yard',
    'carrierGeoID': '4HUWDP9N1INN5',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'DEPOT',
    'locationName': 'Dammam CST',
    'carrierGeoID': 'CDAHIYDF2IUWA',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CONTAINER FREIGHT STATION',
    'locationName': 'BARWIL AGENCIES LTD FOR SHIPPING',
    'carrierGeoID': 'S5CQSFVPNWP2A',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'Majdouie Depot Dammam',
    'carrierGeoID': '4EADVGGFCAYVE',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CUSTOMER LOCATION',
    'locationName': 'Dammam MCF',
    'carrierGeoID': 'U6ILXO9C995DP',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'West Group Logistics Port Services',
    'carrierGeoID': '4CKGBKLV7OZOJ',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CONTAINER FREIGHT STATION',
    'locationName': 'Wolf Transport Terminal Dammam',
    'carrierGeoID': 'SCG6KKSKFNXZQ',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CONTAINER FREIGHT STATION',
    'locationName': 'Globe Terminal Dammam',
    'carrierGeoID': 'LSGIX4ZHBSHGS',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'CONTAINER FREIGHT STATION',
    'locationName': 'Jadeer Terminal Dammam',
    'carrierGeoID': '37VLXXZGPLLOJ',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'TERMINAL',
    'locationName': 'Al Hajri Dammam Terminal',
    'carrierGeoID': '51XDU3KHVEGOW',
    'UNLocationCode': 'SADMM'
  },
  {
    'countryCode': 'SA',
    'countryName': 'Saudi Arabia',
    'cityName': 'Dammam',
    'locationType': 'DEPOT',
    'locationName': 'KANOO TERMINAL SERVICES 2',
    'carrierGeoID': '2780296645491',
    'UNLocationCode': 'SADMM'
  }
]
'''


# conn.request("GET", "/reference-data/locations", headers=headers)
#
#
# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))




'''
https://api.maersk.com/reference-data/locations/?UNLocationCode=SADMM

Consumer Key: MCcuYysgoC4DeIDhPh7n3BpMf1BHyWTJ
Secret:OxKDnlFYWBlUl6Tr

{"Content-Type": "application/json", "Consumer-Key": "MCcuYysgoC4DeIDhPh7n3BpMf1BHyWTJ"}

'''

