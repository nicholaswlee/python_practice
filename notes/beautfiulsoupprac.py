from socket import SOL_UDP
import urlib.request, urllib.parse, urlb.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
# Gives an object that is cleaned up html essentially
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags and returns a list
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))