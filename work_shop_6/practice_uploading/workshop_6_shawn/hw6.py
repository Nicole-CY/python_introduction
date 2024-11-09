class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self.borrowed =  False
    def __str__(self):
        return f"{self.title} by {self.author} -Price: {self.price}"


class Novel (Book):
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def __str__(self):
        return f"{self.title} by {self.author} -Price: {self.price} -Genre: {self.genre}"

novel = Novel("The Da Vinci Code", "Dan Brown", 24.50, "Mystery")
print(novel.title)
print(novel.genre)
print("-----------------------------")

class Bookshelf:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("This is not a book")

    def book_list(self):
        if not self.books:
            return "No books"
        return "\n".join([str(book) for book in self.books])


    def search_books(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return str(book)
        return "Book not found"

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.borrowed:
                book.borrowed = True
                return f"You borrowed {book.title}"
            elif book.title.lower() == title.lower() and book.borrowed:
                return f" {book.title}is already borrowed"

        return "Not found"

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() & book.borrowed == True:
                book.borrowed = False
                return f"You returned {book.title}"
        return f"Not found"


if __name__ == "__main__":
    shelf = Bookshelf()
    shelf.add_book(Book("The Da Vinci Code", "Dan Brown", 24.50))
    shelf.add_book(Novel("The Da Vinci Code", "Dan Brown", 24.50, "Mystery"))
    shelf.add_book(Novel("Journey to the West", "Wu Chengen", 20.00, "Fantasy"))
    print(shelf.book_list())
    print("-----------------------------")
#     Search by title
    print(shelf.search_books("da vinci"))
    print("-----------------------------")
#     Borrow book




