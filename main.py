import sys
from datetime import date
from os import system

sys.path.append('./classes')

from classes.Card import Card
from classes.Person import Person
from classes.bankomat import ATM
from loader import load

if __name__ =='__main__':
    karta=Card(input("Karta nomi:"),int(input("Balansi:")),int(input("Parol o'ylang:")))
    odam=Person(input("Ismingiz:"),karta,int(input("Naxt pulingiz qancha:")))
    bank1=ATM(1400000,'NBU')
    bank1.parol_tekshir(odam)
    load()
    print('''[1]--> Balansni tekshirish
[2]--> Naqd pul yechish
[3]--> Parolni o'zgartirish
[4]--> Kartaga pul o'tkazish
[5]--> Naqd pul balansi
[6]--> Chiqish''')
    while True:
        tanlov=int(input(">>>"))
        if tanlov ==1:
            print(karta.get_balans())
        elif tanlov==2:
            qancha=int(input("Qancha pul yechasiz:"))
            if qancha <=karta.get_balans() and qancha<=bank1.get_naxt_pul():
                karta.set_balans_minus(qancha)
                bank1.naxt_pul_minus(qancha)
                odam.karmon_plus(qancha)
                print(f'''           Chek
    Pul yechilgan sana:{date.today()}
    {qancha} pul yechildi
    Balans:{karta.get_balans()} so'm''')
            else:
                print("Mablag' yetarli emas")
        elif tanlov==3:
            karta.set_parol(input("Yangi parol:"))

        elif tanlov==4:
            qiymat=int(input('Qancha pul tashlamoqchisiz:'))
            if qiymat<=odam.karmon:
                bank1.naxt_pul_plus(qiymat)
                odam.karmon_minus(qiymat)
                karta.set_balans_plus(qiymat)
            else:
                print("Mablag' yetarli emas")
        elif tanlov==5:
            print(odam.karmon)
        elif tanlov==6:
            system('clear')
            exit()
        else:
            print("Tushunarsiz buyruq!!")