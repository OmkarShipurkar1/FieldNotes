


from Shelf import Shelf


print("--- FIELD NOTES ---")

shelf = Shelf()

while(True):
    print("1. View Books")
    print("2. Add Book")
    print("0. Exit")
    user_input = int(input("your choice: "))

    if user_input == 1:
        print("======================")
        print(shelf.get_book_titles())
        print("======================")

        while(True):
            print("Enter 0 to exit book choice!")
            choice = int(input("Choose the book ID to view it's details : "))
            print("======================")
            shelf.show_book_details(choice) 
            print("======================")
            print(shelf.get_book_titles())
            print("\n")


    if user_input == 2:
        print("======================")
        shelf.add_book()
        print("======================")
        print("Book Added Successfully")
        print("======================")

    if user_input == 0:
        break

