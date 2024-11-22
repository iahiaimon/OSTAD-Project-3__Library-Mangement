

# def search_book(all_book):
#     title = input("Enter the name of the book you want to search: ")

#     if title in all_book:
#         print(f"Book found {['title']} | {['author']} | {['isbn']} | {['year']} | {['publisher']}")
    
#     else:
#         print("Book not found in the library")
#         # search_book(all_book)




def search_book(all_book):
    title = input("Enter the name of the book you want to search: ")

    for book in all_book:
        if book["title"]== title: 
            print(f"\nBook found: {book['title']} | {book['author']} | {book['isbn']} | {book['year']} | {book['publisher']}")
            return
        
    print("Book not found in the library.\n")
