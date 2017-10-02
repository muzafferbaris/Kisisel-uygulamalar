import requests
from bs4 import BeautifulSoup

url = "https://belgeler.yazbel.com/python-istihza/print.html"
response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

with open("yazbelPrint.txt","w") as dosyaprint:
    for i in soup.find_all("div",{"class","section"}):
        dosyaprint.write(i.text)
