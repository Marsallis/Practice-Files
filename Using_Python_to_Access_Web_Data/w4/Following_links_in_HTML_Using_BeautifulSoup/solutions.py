import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

names = []

while count > 0:
    print ("retrieving: {0}".format(url))
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page)
    tag = soup('a')
    name = tag[position-1].string
    names.append(name)
    url = tag[position-1]['href']
    count -= 1

print (names[-1])


#https://stackoverflow.com/questions/35790064/following-links-in-python