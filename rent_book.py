

def rent_book(all_book , rented_book):
    title = input("Enter the name of the book that you want to rent: ")

    for book in all_book:

        if book['title'] == title:
            if book['rented'] == True:
                print("\nSorry, this book is already rented.")
            elif book['rented'] == False:
                print(f"\nYou have successfully rented '{title}' book ")
                print("You have to return the book in 15 days ")
                rented_book.append(book)
                all_book.remove(book)


    