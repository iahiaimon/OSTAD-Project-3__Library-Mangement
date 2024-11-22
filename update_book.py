

def update_book(all_book):
    title = input("Enter the name of the book you want to update: ")

    for book in all_book:
        if book["title"] == title:
            print("Enter the new data about the book :")
            book["author"] = input(f"Author ({book['author']}): ")
            book["isbn"] = input(f"ISBN ({book['isbn']}): ")
            book["year"] = input(f"Year ({book['year']}): ")
            book["publisher"] = input(f"Publisher ({book['publisher']}): ")
            print(f"Book '{title}' updated successfully!")
            return
    print(f"Book '{title}' not found in the library.")