from save_all_books import save_all_books

def add_book(all_book):
    title = input("\nEnter the name of your book : ")
    author = input("\nEnter the name of the author : ")
    isbn = int(input("\nEnter the ISBN number : "))
    year = int(input("\nEnter the year of publication : "))
    publisher = input("\nEnter the name of the publisher : ")
    price = input("\nEnter the price of the book : ")
    quantity = input("\nHow many book you want to add : ")

    book = {
        "title" : title,
        "author" : author,
        "isbn" : isbn,
        "year" : year,
        "publisher" : publisher,
        "price" : price,
        "quantity" : quantity,
        "rented" : False
        
    }
    
    all_book.append(book)
    save_all_books(all_book)

    print(f"Book '{title}' added successfully!")

    return all_book