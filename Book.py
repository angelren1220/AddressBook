import csv


class Book:

    # initialize the book and generate the csvfile
    def __init__(self):

        self.filename = "contacts_book.csv"
        self.header = ("Name", "Number")

    # set the original contacts into book
    def writer(self, data):
        with open(self.filename, "w", newline="") as f:
            contacts = csv.writer(f)
            contacts.writerow(self.header)
            for x in data:
                contacts.writerow(x)

    # add a new contact
    def adder(self, new):
        with open(self.filename, "a", newline="") as f:
            contacts = csv.writer(f)
            contacts.writerow(new)

    # search an exist contact with name, print full contact if found, otherwise "not found"
    def searcher(self, name):
        with open(self.filename, "r") as f:
            contacts = csv.reader(f)
            for row in contacts:
                for field in row:
                    if field == name:
                        return row
            return "not found"

    # delete an exist contact with name, using a list as temporary book and overwrite the original book
    def remover(self, name):
        lines = list()
        with open(self.filename, "r") as f:
            contacts = csv.reader(f)
            for row in contacts:
                lines.append(row)
                for field in row:
                    if field == name:
                        lines.remove(row)
        with open(self.filename, "w") as f:
             contacts = csv.writer(f)
             contacts.writerows(lines)

    # sort the contacts by name, using a list as temporary book and overwrite the original book
    def sorter(self):
        lines = list()
        with open(self.filename, "r") as f:
            contacts = csv.reader(f)
            for row in contacts:
                lines.append(row)
            lines.sort()

        with open(self.filename, "w") as f:
            contacts = csv.writer(f)
            contacts.writerows(lines)

    # view full contacts
    def view(self):
        with open(self.filename, "r") as f:
            contacts = csv.reader(f)
            for contact in contacts:
                print(contact)
            print("\n")
