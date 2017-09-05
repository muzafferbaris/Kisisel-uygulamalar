def sifre(s_sifre=None):
    s_sifre = input("Şifrenizi belirleyiniz: ")
    return s_sifre

class Azal():
    kalan = 3
    def __init__(self,gelen):
        self.gelen = gelen
        self.kalan = 3

        if len(self.gelen) < 8:
            print("Şifre en az beş karakterden oluşmalıdır.")
            self.sorgu()
        else:
            print("Şifre Belirlendi.")
    @classmethod
    def sorgu(cls):
        cls.kalan-=1
        if cls.kalan == 0:
            print("Hakkınız kalmadı.")
        else:
            print("Kalan hakkınız: ",cls.kalan)
            mb = Azal(sifre())

mb = Azal(sifre())
