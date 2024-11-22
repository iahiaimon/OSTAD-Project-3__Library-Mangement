

def save_all_books(all_book):
    with open("library.txt", "w") as file:
        for book in all_book:
            line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['publisher']} , {book['price']} , {book['quantity']} \n"
            file.write(line)