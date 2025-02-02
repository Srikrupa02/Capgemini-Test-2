#  Write an example where `Operator Overloading` is used to concatenate 
# two `Book` objects,treating them as a series.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __add__(self, other):
        new_title = f"{self.title} and {other.title}"
        new_author = f"{self.author} & {other.author}"
        return Book(new_title, new_author)
    def __str__(self):
        return f"Book Title: {self.title}, Author: {self.author}"

book1 = Book("Wings of Fire", "APJ Abdul Kalam")
book2 = Book("Harry Potter", "J.K. Rowling")
series = book1 + book2
print(series)