from .Person import Person
from time import sleep
from os import system

class ATM:
    def __init__(self,naxt_pul:int,nomi:str):
        self.__naxt_pul=naxt_pul
        self.nomi=nomi

    def parol_tekshir(self,person:Person):
        count=0
        for i in range(4):
            if count ==3:
                print("Bloklandingiz")
                sleep(1)
                system('clear')
                exit()
            else:
                if person.card.get_parol() == int(input("Parolni kiriting:")):
                    print("DONE")
                    sleep(1)
                    system('clear')
                    break
                else:
                    count+=1
                    print("Noto'g'ri qayta urining")

    def get_naxt_pul(self):
        return self.__naxt_pul

    def naxt_pul_minus(self,qancha):
        self.__naxt_pul-=qancha

    def naxt_pul_plus(self,qancha):
        self.__naxt_pul+=qancha
