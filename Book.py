
from datetime import date


class Book:
    def __init__(self,id, title, author, type, genre, about ):
        self.id = id
        self.title = self.format_name(title)
        self.author = self.format_name(author)
        self.type = type.lower()
        self.genre = genre
        self.about = about
        self.date = date.today()
        self.quotes = []
        self.notes = []
        self.chapters_summary = []

    def format_name(self, name):
        strs = name.split(" ")
        names = map(lambda x: x[0].upper() + x[1:].lower() , strs )
        return " ".join(list(names))

    def display(self):
        print(f"\nTitle: {self.title}\nAuthor: {self.author}\nType: {self.type}\nGenre: {self.genre}\nAbout: {self.about}\nDate Added: {self.date}")



    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nType: {self.type}\nGenre: {self.genre}\nAbout: {self.about}\nDate Added: {self.date}"


