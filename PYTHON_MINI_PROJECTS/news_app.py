import requests
import json
a=input("which news do you want to see")
r=requests.get(f"https://newsapi.org/v2/everything?q={a}&from=2024-06-18&sortBy=publishedAt&apiKey=e733a5ee87f74b24916cd362109f2739")
# print(r.text)
j=r.json()
k=0
for i in j['articles']:
     print(i["title"])
     print(i["description"])
     print("------------------------------------------------------------------------------")
     k=k+1
     if(k==5):
          break
     
          



