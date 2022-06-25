import urlib.request, urllib.parse, urlb.error
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(addresss) < 1:
        break
    ### Creates the url that has the json file
    url = serviceurl + urllib.parse.urlencode({'address' : address})

    ### Get the JSON file
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    ### Attempt to load the json file
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lat = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)