class library:

    def  __init__(self, books):
        self.books = books

    def availablebook(self):
        if self.books != None:
            print("Books are Available!")
        for bookslib in self.books:
            print(bookslib)
        


    def lendbook(self, requesedtbook):
        if requesedtbook in self.books:
            self.books.remove(requesedtbook)
            print("Thanks for book")
        else:
            print("Book doesn't exists")


    def addbook(self, returnedbook):
        self.books.append(returnedbook)
        print(" book added successfully in library")

        
class Customer:

    def requsetbook(self):
        print("enter the book name to get ")
        self.book= input()
        

    def returnbook(self):
        print("enter the book name to return")
        self.book = input()


library_book = library(["Rich dad poor dad", "Discipline", "Money by confidence"])
customer = Customer()
while True:
    print("enter 1 to get the avilable books")
    print("enter 2 to get the lend books")
    print("enter 3 to addbook")
    print("enter 4 to exit")

    userchoice  = int(input())
    print()

    if userchoice == 1:
        library_book.availablebook()
        print()
    elif userchoice == 2:
        library_book.lendbook(input("Enter Book Name:"))
        print()
    elif userchoice == 3:
        library_book.addbook(input("Enter Book Name to Add:"))
        print()
    elif userchoice == 4:
        quit()
        





































































































































































































































































































































































































































































































































































































































































































































































