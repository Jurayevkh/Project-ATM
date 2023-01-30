from time import sleep

class Card:
    def __init__(self,nomi,balans,parol):
        self.nomi=nomi
        self.__balans=balans
        self.__parol =parol

    def get_balans(self):
        return self.__balans

    def set_balans_minus(self,qancha:int):
        self.__balans -=qancha

    def set_balans_plus(self,qancha:int):
        self.__balans+=qancha

    def get_parol(self):
        return self.__parol

    def set_parol(self,new_parol:int):
        self.__parol = new_parol
        print("Parol o'zgardi")
        sleep(1)
