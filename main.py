import add_book
import delete_book
import search_book
import update_book
import view_all_books
import rent_book
import return_book

all_book = []

rented_book = []


def main():

    while True :
        print("\nWelcome to the library!\n")
        print("1: Add book ")
        print("2: Delete book ")
        print("3: Search book.... ")
        print("4: Update book ")
        print("5: View all books")
        print("6: Rent a book")
        print("7: Return a book")
        print("0: Exit")

        choice = int(input("Select an option.... : "))

        if 0<=choice<=7 :

            if choice == 0:
                print("\nThank you for using the library management system!\n")
                break

            elif choice == 1 :
                add_book.add_book(all_book)

            elif choice == 2 :
                delete_book.delete_book(all_book)

            elif choice == 3 :
                search_book.search_book(all_book)

            elif choice == 4 :
                update_book.update_book(all_book)

            elif choice == 5 :
                view_all_books.view_all_books(all_book)

            elif choice == 6 :
                rent_book.rent_book(all_book , rented_book)

            elif choice == 7 :
                return_book.return_book(rented_book , all_book)


        else:
            print("\nInvalid option! Please select a valid option.\n")


if __name__ == "__main__":
    main()