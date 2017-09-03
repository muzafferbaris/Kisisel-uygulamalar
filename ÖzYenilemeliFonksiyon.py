# python
#değerlerin bulunduğu bir sözlük oluşturuyoruz
sözlük = {"Edirne":"22","Malatya":"44","İzmir":"35","Balıkesir":"10"}
#kullanıcıdan plakasını öğrenmek istediği ilin adını alıyoruz 
sorgula = input("Plaka kodunu öğrenmek istediğiniz ilin ismini giriniz: ")
#while ile sonsuz bir döngü oluşturuyoruz
while True:
    #eğer kullanıcıdan gelen veri q'ya eşitse break ile döngüyü kırıp programdan çıkış yapıyoruz
    if sorgula == "q":
        break
    #eğer kullanıcıdan gelen veri q değilse 
    elif sorgula:
        #sorgula değişkenini sözlük içindeki değerlerle karşılaştırıp eşleşen veriyi ekrana yazdırıyoruz 
        print(sözlük.get(sorgula,"Böyle Bir İl Bulunamadı!"))
        sorgula = input("Plaka kodunu öğrenmek istediğiniz ilin ismini giriniz: ")
