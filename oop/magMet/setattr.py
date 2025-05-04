class A:
    def __setattr__(self, name, value):
        self.__dict__[name] = value
        print(f"{name} установлено в {value}")

a = A()
a.x = 5