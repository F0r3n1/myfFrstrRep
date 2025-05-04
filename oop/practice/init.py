class Book:
    def __init__(self,author,title):
        self.title=title
        self.author=author

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}")

Yesli=Book("Xz","JOPA")
Yesli.info()