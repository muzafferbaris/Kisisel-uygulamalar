#Gerekli modüller içe aktarıldı
import requests
from bs4 import BeautifulSoup

#işlem yapılacak site adresi
url = "https://belgeler.yazbel.com/python-istihza/print.html"

#web sayfasındaki bütün bilgileri çekiyoruz.
tümicerik = requests.get(url)

#sayfanın html dökümanını alıyoruz.
html_icerigi = tümicerik.content

#BeautifulSoup sınıfı ile html içeriği parse ediyoruz.(daha düzgün gözükmesi için)
soup = BeautifulSoup(html_icerigi,"html.parser")

#yazbelPrint adında bir txt dosyası oluşturuyoruz.
with open("yazbelPrint.txt","w") as dosyaprint:
    #daha sonra html içindeki class'ı section olan tüm divleri üzerinde işlem yapmak için buluyoruz.
    for i in soup.find_all("div",{"class","section"}):
        #Ve bu seçili olan class içindeki tüm yazıları yazbelPrint dosyasının içine yazdırıyoruz.
        dosyaprint.write(i.text)
