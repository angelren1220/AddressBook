from Book import Book


book1 = Book()

data = [
        ("Ann Liner", "123456"),
        ("Peter Burger", "234567"),
        ("Ben Trump", "345678"),
        ("Lee Mia", "099932"),
        ("Cathy Zhang", "10102374")
    ]

book1.writer(data)
'''print("Original Book:")
book1.view()

book1.adder(("Oreo More", "10203845"))
print("A new contact added:")
book1.view()

book1.sorter()
print("Sorted contacts:")
book1.view()

book1.remover("Peter Burger")
print("An old contact deleted:")
book1.view() '''

while True:
        option = input("Choose your option:\n"
                       "0. view book\n"
                       "1. search a contact\n"
                       "2. add a new contact\n"
                       "3. delete a contact\n"
                       "4. sort contacts\n"
                       "5. exit\n")
        if option == "0":
                book1.view()
        elif option == "1":
                target: str = input("Enter full name to search:\n")
                result = book1.searcher(target)
                print(result)
        elif option == "2":
                name: str = input("Enter name to add:\n")
                number: str = input("Enter number to add:\n")
                book1.adder((name, number))
        elif option == "3":
                temp = input("Enter full name to delete:\n")
                result = book1.searcher(temp)
                print(result)
                book1.remover(temp)
        elif option == "4":
                book1.sorter()
        elif option == "5":
                exit()
        else:
                print("not an option\n")