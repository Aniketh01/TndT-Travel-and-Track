from opensky_api import OpenSkyApi
import json
api = OpenSkyApi()
states = api.get_states()
for s in range(5):
    s=states.states[s]
    print("(%r, %r)" % (s.latitude, s.longitude))
    with open('latitude.json', 'a+w') as outfile:
        json.dump(s.latitude, outfile)
        outfile.write("\n")
    with open('longitude.json', 'a+w') as outfile:
        json.dump(s.longitude, outfile)
        outfile.write("\n")

    