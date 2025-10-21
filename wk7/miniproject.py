class book():
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


books = []

options = ("1. Add book/n View books/n 3. Borrow book/n 4. Return book/n 5. Exit")

choice = input(f"Enter your choice \n{options}:")

while True:
    match choice:
        case "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                copies = int(input("Enter number of copies: "))
                new_book = book(title, author, copies)
                books.append(new_book)
                print(
                    f"Book '{title}' by {author} has been successfully added with {copies} copies.")

            case "2":
                if not books:
                    print("No books available.")
                else:
                    for i in books:
                        print(f"Book {books.index(i)+1}")
                        print(
                            f"Title: {i.title}, Author: {i.author}, Copies: {i.copies}")

            case "3":
                book_title = input(
                    "Enter the title of the book you want to borrow: ")
                for i in books:
                    if i.title == book_title:
                        if copies > 0:
                            i.copies -= 1
                            print(
                                f"You have successfully borrowed '{book_title}'.")
                        else:
                            print(
                                f"Sorry, '{book_title}' is currently unavailable, try to add some copies.")
                    else:
                        print("Book not found.")

            case "4":
                book_title = input(
                    "Enter the title of the book you want to return: ")
                for i in books:
                    if i.title == book_title:
                        i.copies += 1
                        print(
                            f"You have successfully returned '{book_title}'.")
                    else:
                        print("Book not found in system.")

            case "5":
                print("Exiting the program .....Goodbye.")
                break
    else:
        print("Invalid choice, please try again.")
