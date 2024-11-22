
def view_all_books(all_book):
    if all_book != []:
        for book in all_book:
            print(f"Title: {book['title']} | Author: {book['author']} | ISBN: {book['isbn']} | Year: {book['year']} | Publisher: {book['publisher']} | Price: {book['price']} | Quantity: {book['quantity']}")

    else:
        print("\nNo Book found in program")

