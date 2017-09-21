import random
import time

def Oyun(oyuncu=0,pc=0):
    print("""**********************************************
Programın rastgele ürettiği sayıyı 3 denemede 
bulmaya çalışın.
Not: Sayı 1 ile 7 Arasındadır.
**********************************************
    """)
    while True:

        Rsayi = random.randint(0, 7)
        tahmin = int(input("Tahmininiz: "))

        if oyuncu == 2:
            print("Oyun bitti. Kazandın.")
            oyuncu+=1
            break
        elif pc == 2:
            print("Oyun bitti. Kaybettin.")
            pc+=1
            print("Sen:",oyuncu,"PC:",pc)
            break

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