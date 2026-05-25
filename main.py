#3-m
class Book:
    def __init__(self, title, author):
        self.title = title
        self.__author = author
    
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, new_author):
        self.__author = new_author
        
b1 = Book("Python Programming", "<NAME>")
print(b1.author)

res = b1.author
print(res)

b1.author = "<NAME>"
print(b1.author)
