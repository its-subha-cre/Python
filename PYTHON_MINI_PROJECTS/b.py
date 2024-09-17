from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://en.wikipedia.org/wiki/Harry_potter')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(images[0]['src']+'\n')
from PIL import Image
import requests
from io import BytesIO

response = requests.get("upload.wikimedia.org/wikipedia/commons/thumb/8/81/The_Elephant_House.jpg/220px-The_Elephant_House.jpg")
img = Image.open(BytesIO(response.content))