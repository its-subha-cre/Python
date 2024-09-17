import requests
from bs4 import BeautifulSoup as bs

leader = ["Harry Potter"]
l_i = []

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

for l in leader:
    params = {
        "q": l,
        "tbm": "isch"
    }
    html = requests.get("https://www.google.com/search", params=params, headers=headers, timeout=30)
    soup = bs(html.content, "html.parser")
    images = soup.select('img')
    
    if images and 'src' in images[1].attrs:
        images_url = images[1]['src']
        l_i.append(images_url)

print(l_i)

