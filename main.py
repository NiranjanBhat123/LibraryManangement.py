import random
class Library:

    def __init__(self,listOfBooks):
        self.books= listOfBooks

    def displayAvailableBooks(self):

        print("The books available in this library are:\n")
        for book in self.books:

            print("*\t"+book)


    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you have been issued the book {bookName}\n")
            print(f"due date for book is {random.randint(1,30)}th\nenjoy reading!\n")

            self.books.remove(bookName)

        else:
            print("This book is not available currently :(")
            return False


    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Book returned successfully")


class student:
    def requestBook(self):
        self.book=input("enter the name of the book you want to borrow\n")

        return self.book

    def returnBook(self):
        self.book = input("enter the name of the book you want to return\n")




if __name__ == "__main__":
    centralLibrary= Library(["algorithms","DSA","50 shades of grey","faynman's lectures"])
    centralLibrary.displayAvailableBooks()
    student= student()

    while(True):

        welcomeMsg='''*******WELCOME TO CENTRAL LIBRARY*******
                   'please choose an option
                   1. list all the books
                   2. request a book
                   3. return a book 
                   4.exit the library'''
        print(welcomeMsg)
        a = int(input("enter a choice\n"))


        if(a==1):
            centralLibrary.displayAvailableBooks()

        elif(a==2):
            centralLibrary.borrowBook(student.requestBook())

        elif(a==3):
            centralLibrary.returnBook(student.returnBook())
        elif(a==4):

            print("Thank you")
            exit()
        else:
            print("Invalid choice")





