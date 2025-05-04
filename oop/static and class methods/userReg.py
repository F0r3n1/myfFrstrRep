class User:
    def __init__(self,name,age, email):
        self.name=name
        self.age=age
        self.email=email
    print("ИНИТИАЛИЗАЦИЯ ПРОШЛА")

    @staticmethod
    def isMail(email):
        if "@" in email and "." in email:
            return True

    @staticmethod
    def validateAge(age):
        if 5<age and age<100:
            return True

    @classmethod
    def register(cls, name, age, email):
        pass

    def showInfo(self):
        pass


User.validateAge(10)