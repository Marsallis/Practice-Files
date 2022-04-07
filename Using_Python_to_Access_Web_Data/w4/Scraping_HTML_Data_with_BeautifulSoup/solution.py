from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup("span")
#print(tags)
sum = 0

# Retrieve all of the span tags
for tag in tags:
    nums = int(tag.contents[0])
    #print(nums)
    sum = sum + nums
print(sum)

#Test URL
#http://py4e-data.dr-chuck.net/comments_1506524.html