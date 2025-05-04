class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def createUser(cls,name,age):
        print(f"Зарегестрирован новый пользователь:{name}, {age}")
    @staticmethod
    def ageTrue(age):
        if age<100 and age>3:
            return True
