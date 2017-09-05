#bu programda kullanıcıdan 8 haneli bir şifre belirlemesini istiyoruz 
#eğer şifre 8 haneden az ise Uyarı verdirip tekrar girmesini istiyoruz.
#programda kullanıcının 3 hakkı var. 3 denemede şartları yerine getirmez ise
#çıkış yapılıyor

#sifre isimli bir fonksiyon oluşturduk
def sifre(s_sifre=None):
    s_sifre = input("Şifrenizi belirleyiniz: ")
    
    #gelen veriyi return ile geri döndürdük
    return s_sifre

#daha sonrada Azal isminde bir sınıf tanımladık.
class Azal():
    #kalanı 3'e eşitledik(bu değişken programa kullanıcının kaç hakkı kaldığını söyliyicek.
    kalan = 3
    
    def __init__(self,gelen):
        self.gelen = gelen
        self.kalan = 3
        #eğer şifre küçükse 8'den 
        if len(self.gelen) < 8:
            # kullanıcıyı uyardık.
            print("Şifre en az beş karakterden oluşmalıdır.")
            #ve sorgu isimli örnekleme methodunu çalıştırdık.
            self.sorgu()
        else:
            #ama yok şifre 8 veya daha fazla karakterden oluşuyorsa burası çalışıp.
            #kullanıcıya şifrenin belirlendiğini söyliyicek
            print("Şifre Belirlendi.")
    @classmethod
    def sorgu(cls):
        #çalışan bu method da kalan değişkeni bir azalacak
        cls.kalan-=1
        #eğer kalan değişkeni 0'a eşitse
        if cls.kalan == 0:
            #Kullanıcıya hakkının kalmadığı söylenicek
            print("Hakkınız kalmadı.")
        else:
            #ama yok kalan değişkeni 0'dan büyükse 
            #kalan hakkını belirtip
            print("Kalan hakkınız: ",cls.kalan)
            #sınıfı tekrar çağırıyoruz. ve tüm program tekrar baştan
            #her durumu kontrol ediyor.
            mb = Azal(sifre())

mb = Azal(sifre())
