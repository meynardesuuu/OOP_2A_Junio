# Junio, Meynard Brian Y.
# BSIT - 2A

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
book1 = Book("To Kill a Mockingbird", "Harper Lee")
book2 = Book("Moby-Dick", "Herman Melville")
print(book1.title, book1.author)
print(book2.title, book2.author)
del book1.author
# print(book1.title, book1.author)
print(book2.title, book2.author)
