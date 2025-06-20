class Book: 
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return f"{self.book_id}|{self.title}|{self.author}|{self.price}"
class BookStore:
    FILE_NAME = "books.txt"
    def add_book(self, book):
        with open(self.FILE_NAME, "a") as file:
            file.write(str(book) + "\n")
        print("Book added successfully.")
    def view_books(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                books = file.readlines()
                if not books:
                    print("No Books Found.")
                    return
                print("\nAll Books:")
                for line in books:
                    book = line.strip().split('|')
                    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}")
        except FileNotFoundError:
            print("No books file found.")
    def search_book(self, book_id):
        found = False
        try:
            with open(self.FILE_NAME, "r") as file:
                for line in file:
                    book = line.strip().split('|')
                    if book[0] == book_id:
                        print(f"Book Found: ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Price: {book[3]}")
                        found = True
                        break
                if not found:
                        print("Book not found.")
        except FileNotFoundError:
            print("No books file found.")
    def update_book(self, book_id, new_title, new_author, new_price):
        updated = False
        try:
            with open(self.FILE_NAME, "r") as file:
                books = file.readlines()
            with open(self.FILE_NAME, "w") as file:
                for line in books:
                    book = line.strip().split('|')
                    if book[0] == book_id:
                        file.write(f"{book_id}|{new_title}|{new_author}|{new_price}\n")
                        updated = True
                    else:
                        file.write(line)
            if updated:
                print("Book updated successfully.")
            else:
                print(" book not found.")
        except FileNotFoundError:
            print("No books file found.")
    def delete_book(self, book_id):
        deleted = False
        try:
            with open(self.FILE_NAME, "r") as file:
                books = file.readlines()
            with open(self.FILE_NAME, "w") as file:
                for line in books:
                    book = line.strip().split('|')
                    if book[0] != book_id:
                        file.write(line)
                    else:
                        deleted = True
            if deleted:
                print("book deleted successfully.")
            else:
                print("book not found.")
        except FileNotFoundError:
            print("No books file found.")
def main():
        store = BookStore()
        while True:
            print("\n--- Book Store Menu ---")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Update Book")
            print("5. Delete book")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                book_id = input("Enter Book Id: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                price = input("Enter Price: ")
                book = Book(book_id, title, author, price)
                store.add_book(book)
            elif choice == '2':
                store.view_books()
            elif choice == '3':
                book_id = input("Enter Book ID to search: ")
                store.search_book(book_id)
            elif choice == '4':
                book_id = input("Enter book id to update: ")
                new_title = input("Enter new title: ")
                new_author = input("Enter new author: ")
                new_price = input("Enter new price: ")
                store.update_book(book_id, new_title, new_author, new_price)
            elif choice == '5':
                book_id = input("Enter book Id to delete: ")
                store.delete_book(book_id)
            elif choice == '6':
                print("Exiting.... Goodbye!")
                break   
            else:
                print("Invalid choice. Try again.")
if __name__ == "__main__":
        main()