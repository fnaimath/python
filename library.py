class Library:
    def __init__(self, books):
        self.books = books
    def borrow(self, book):
        self.books.remove(book)
    def retrn(self, book):
        self.books.add(book)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


b1 = Book("Dune", "herb")
b2 = Book("LOTR", "jr")
b3 = Book("Harry Potter", "jk")
l1 = Library({b1, b2, b3})
l1.borrow(b1)
l1.retrn(b1)