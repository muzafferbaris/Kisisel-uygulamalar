# python

sözlük = {"Edirne":"22","Malatya":"44","İzmir":"35","Balıkesir":"10"}
sorgula = input("Plaka kodunu öğrenmek istediğiniz ilin ismini giriniz: ")
while True:
    if sorgula == "q":
        break
    elif sorgula:
        print(sözlük.get(sorgula,"Böyle Bir İl Bulunamadı!"))
        sorgula = input("Plaka kodunu öğrenmek istediğiniz ilin ismini giriniz: ")
