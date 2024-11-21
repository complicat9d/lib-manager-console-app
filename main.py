from schemas.library import Library
from utils.terminal import clear_terminal


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. List all books")
        print("5. Change book status")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")

            while True:
                try:
                    year = int(input("Enter year of publication: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the year.")

            library.add_book(title, author, year)
            input("\nPress Enter to continue...")
            clear_terminal()

        elif choice == "2":
            while True:
                try:
                    book_id = int(input("Enter book ID to remove: "))
                    break
                except ValueError:
                    print(
                        "Invalid input. Please enter a valid integer for the book ID."
                    )

            library.remove_book(book_id)
            input("\nPress Enter to continue...")
            clear_terminal()

        elif choice == "3":
            print("\nChoose the search parameter:")
            print("1. Search by ID")
            print("2. Search by Year")
            print("3. Search by Title")
            print("4. Search by Author")

            search_choice = input("Enter your choice (1-4): ")

            if search_choice == "1":
                query = input("Enter book ID to search: ")
                library.search_books("id", query)
            elif search_choice == "2":
                query = input("Enter year to search: ")
                library.search_books("year", query)
            elif search_choice == "3":
                query = input("Enter title to search: ")
                library.search_books("title", query)
            elif search_choice == "4":
                query = input("Enter author to search: ")
                library.search_books("author", query)
            else:
                print("Invalid choice. Please try again.")

            input("\nPress Enter to continue...")
            clear_terminal()

        elif choice == "4":
            library.list_books()
            input("\nPress Enter to continue...")
            clear_terminal()

        elif choice == "5":
            while True:
                try:
                    book_id = int(input("Enter book ID to change status: "))
                    break
                except ValueError:
                    print(
                        "Invalid input. Please enter a valid integer for the book ID."
                    )

            new_status = input("Enter new status ('in_stock' or 'handed_out'): ")
            library.change_status(book_id, new_status)
            input("\nPress Enter to continue...")
            clear_terminal()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")
            input("\nPress Enter to continue...")
            clear_terminal()


if __name__ == "__main__":
    main()
