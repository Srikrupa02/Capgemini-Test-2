class Book:
    def __init__(self):
        self.title=input("Enter title:")
        self.author=input("Enter author: ")
        self.isbn=int(input("Enter isbn: "))
    def show(self):
        print(f'The book title is :{self.title} ,The book author is:{self.author}, The book isbn is:{self.isbn}')
book=Book()
book.show()
