# -*- coding: utf-8 -*-
"""
Exercise 100
"""

station = {
 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901
}

for key,value in station.items():
  print("latitude %s" % station['latitude'])
  print("longitude %s" % station['longitude'])
  print("number %s" % station['number'])
  print("name %s" % station['name'])
  print("address %s" % station['address'])

