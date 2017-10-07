import json

from opensky_api import OpenSkyApi
api = OpenSkyApi()
s = api.get_states()
#print(s)

with open('result.json', 'w') as fp:
    json.dump(s, fp)
