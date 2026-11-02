def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    with open("library.txt", "a") as f:
        f.write(title + "," + author + "\n")
    print("Book added successfully!")

def search_book():
    name = input("Enter title or author to search: ")
    with open("library.txt", "r") as f:
        found = False
        for line in f:
            if name.lower() in line.lower():
                print(line.strip())
                found = True
        if not found:
            print("Book not found!")

def report():
    with open("library.txt", "r") as f:
        books = f.readlines()
    print("Total number of books:", len(books))
    author = input("Enter author name for report: ")
    for book in books:
        if author.lower() in book.split(",")[1].lower():
            print(book.strip())

while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Generate Report")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        report()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")