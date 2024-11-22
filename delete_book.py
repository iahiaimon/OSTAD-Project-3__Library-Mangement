

def delete_book(all_book):
    title = input("Enter the name of the book that you want to remove :")

    for book in all_book:
        if book["title"] == title:
            all_book.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found in the library.")

