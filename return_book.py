


def return_book(rented_book , all_book):
    title = input("Enter the name of the book you want to return: ")

    for book in rented_book:
        if book['title'] == title:  

            print(f"The book '{title}' has been successfully returned. Thank you!")
            rented_book.remove(book)
            all_book.append(book)

