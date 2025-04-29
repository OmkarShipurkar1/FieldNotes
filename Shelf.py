

from Book import Book

harry_potter = Book(1,'harry potter', 'j.k. rowling', 'fiction', 'children', "harry's adventures in hogwarts")
siddhartha = Book(2,"siddhartha", 'hermann hesse', 'fiction', 'spirituality',"siddhartha knowing of life's a unstopable suffering")
norewgian_wood = Book(3,"norwegian wood","Murakami", 'fiction', 'Magical Realism', 'a boy running from his fate')

class Shelf(Book):
    def __init__(self):
        self.books = []
        self.books.append(harry_potter)
        self.books.append(siddhartha)
        self.books.append(norewgian_wood)
        self.count = len(self.books)


    def add_book(self):
        title = input("Book title : ")
        author = input("Author name : ")
        type = input("Type (fiction, non-fiction) : ")
        while type != "fiction" and type != "non-fiction": 
            print("enter the correct book type as defined!! ")
            type = input("Type (fiction, non-fiction) : ")
        genre = input("Book Genre : ")
        about = input("About : ")
        self.count += 1

        new_book = Book(self.count,title, author, type, genre , about)
        self.books.append(new_book)

    def get_book_titles(self):
        return "\n".join(list(map(lambda book: f"{book.id}. {book.title}", self.books)))

    def show_book_details(self, id):
        return self.books[id-1].display()

    def handle_input(self,*args ):
        if args == "":
            return 

    def get_total_books(self):
        return self.count

    def __str__(self):
        return "\n-----------------------------\n".join(list(map(Book.__str__,self.books)))




