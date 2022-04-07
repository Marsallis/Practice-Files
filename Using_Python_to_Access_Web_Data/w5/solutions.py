from itertools import count
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

counts = tree.findall('.//count')

print(counts)
print('Count:',len(counts))
print('Sum:', )

sum = 0
for item in counts:
    print('count', item.find('count'))
























#test URL: http://py4e-data.dr-chuck.net/comments_42.xml
#answer URL: http://py4e-data.dr-chuck.net/comments_1506526.xml