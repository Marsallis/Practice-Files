import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1506527.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
#print(info)
comments = (info['comments'])
print('count', len(comments))
sum = 0
for item in comments:
    num = item['count']
    sum = sum + num
    print(item)
    #print(item['count'])

print('Sum:', sum)