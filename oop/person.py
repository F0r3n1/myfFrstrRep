class Person:
    def __init__(self,fio,age,passport,weight):
        self.__fio=fio.split()
        self.__age=age
        self.__passport=passport
        self.__weight-weight

    @classmethod
    def verifyFio(cls,fio):
        if type(fio)!=str:
            raise TypeError("ФИО должно быть словами")
        f=