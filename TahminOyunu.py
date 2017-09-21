import random
import time

def Oyun(oyuncu=0,pc=0):
    Rsayi = random.randint(0,40)
    tahmin = int(input("Tahmininiz: "))

    if (Rsayi == tahmin):
        print("Sorgulanıyor",end="")
        for i in range(0,2):
            time.sleep(0.7)
            print(".",end="")
            if i == 1:
                time.sleep(0.7)
                print(".")
        print("Tahmininiz Tuttu.")
        oyuncu += 1
        print("Sen: {}\nPc: {}".format(oyuncu,pc))
        return Oyun(oyuncu,pc)

    elif (Rsayi != tahmin):
        print("Sorgulanıyor",end="")
        for i in range(0,2):
            time.sleep(0.7)
            print(".", end="")
            if i == 1:
                time.sleep(0.7)
                print(".")
        print("Başarısız.")
        pc += 1
        print("Sen: {}\nPc: {}".format(oyuncu, pc))
        return Oyun(oyuncu,pc)

Oyun()