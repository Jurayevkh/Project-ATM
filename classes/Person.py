from .Card import Card

class Person:
    def __init__(self,name:str,card:Card,karmon:int):
        self.name=name
        self.card=card
        self.karmon=karmon

    def karmon_minus(self,qancha):
        self.karmon-=qancha

    def karmon_plus(self,qancha):
        self.karmon+=qancha

