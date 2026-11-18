from datetime import datetime

from library_management_system.models import Book, Member, Loan
from library_management_system.repositories import FileBasedBookRepository, FileBasedMemberRepository, \
    FileBasedLoanRepository
from library_management_system.service import LibraryManagementService

library_management_service = LibraryManagementService(
    book_repository=FileBasedBookRepository(),
    member_repository=FileBasedMemberRepository(),
    loan_repository=FileBasedLoanRepository()
)

def add_book():

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Published Year: ")

    new_book = Book(book_id=book_id,title=title,author=author,year=year)
    library_management_service.add_book(book=new_book)

    print("\nBook Added Successfully")
    return

def get_book_by_id():

    book_id = input("Enter Book ID: ")
    book = library_management_service.get_book_by_id(book_id=book_id)

    print(f"\n ID  |    Title    |     Author     |   Year  | Book lend Member ID  | Availability"
          f"\n{book.book_id}    {book.title}    {book.author}       {book.year}           {book.book_lend_member_id}             {book.is_available()}")

def list_all_books():

    book_list = library_management_service.list_all_books()
    print(" ID  |    Title    |     Author     |   Year  | Book lend Member ID  | Availability"
          "\n")

    for book in book_list:
        print(f"{book.book_id}    {book.title}    {book.author}       {book.year}           {book.book_lend_member_id}             {book.is_available()}")

def update_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    year = input("Enter Published Year: ")

    up_book = Book(book_id=book_id, title=title, author=author, year=year)
    library_management_service.update_book(book=up_book)

    print("\nBook updated Successfully")
    return

def add_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")
    contact = input("Contact Number: ")

    new_member = Member(member_id=member_id,name=name,contact=contact)
    library_management_service.add_member(member=new_member)

    print("\nMember Added Successfully")
    return

def get_member_by_id():

    member_id = input("Enter Member ID: ")

    member = library_management_service.get_member_by_id(member_id=member_id)

    print(f"\n ID   |     Name     |      Tel NO"
          f"\n{member.member_id}      {member.name}         {member.contact}")

def list_all_members():

    member_list = library_management_service.list_all_members()

    print(" ID   |     Name     |      Tel NO")
    for member in member_list:
        print(f"{member.member_id}      {member.name}         {member.contact}")

def update_member():
    member_id = input("Enter Member ID: ")
    name = input("Enter Name: ")
    contact = input("Contact Number: ")

    up_member = Member(member_id=member_id, name=name, contact=contact)
    library_management_service.update_member(member=up_member)


def borrow_book():

    loan_id = input("Enter Loan ID: ")
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    new_loan = Loan(loan_id=loan_id,member_id=member_id,book_id=book_id)
    library_management_service.add_loan(loan=new_loan)

    borrow_book = library_management_service.get_book_by_id(book_id=book_id)
    up_book = Book(book_id=borrow_book.book_id,
                   title=borrow_book.title,
                   author=borrow_book.author,
                   year=borrow_book.year,
                   book_lend_member_id=member_id)
    library_management_service.update_book(book=up_book)

def get_loan_by_id():

    loan_id = input("Enter Loan ID: ")
    loan = library_management_service.get_loan_by_id(loan_id=loan_id)

    print(f"\nLoan ID | Member ID | Book ID | Borrow Time | Return Time"
          f"\n{loan.loan_id}  {loan.member_id}  {loan.book_id}  {loan.borrowed_at}  {loan.returned_at}")

def list_all_loans():

    loan_list = library_management_service.list_all_loans()

    print("\nLoan ID | Member ID | Book ID | Borrow Time | Return Time"
          "\n")

    for loan in loan_list:
        print(f"{loan.loan_id}  {loan.member_id}  {loan.book_id}  {loan.borrowed_at}  {loan.returned_at}")

def return_book():

    loan_id = input("Enter Loan ID: ")
    loan = library_management_service.get_loan_by_id(loan_id=loan_id)

    up_loan = Loan(loan_id=loan.loan_id,
                   member_id=loan.member_id,
                   book_id=loan.book_id,
                   borrowed_at=loan.borrowed_at,
                   returned_at=datetime.now())

    library_management_service.update_loan(loan=up_loan)

    borrow_book = library_management_service.get_book_by_id(loan.book_id)
    up_book = Book(book_id=borrow_book.book_id,
                   title=borrow_book.title,
                   author=borrow_book.author,
                   year=borrow_book.year)
    library_management_service.update_book(book=up_book)


def main_cli():

    while True:

        try:

            print("\n====================================================="
                  "\n             LIBRARY MANAGEMENT SYSTEM"
                  "\n====================================================="
                  "\n01. Add Book"
                  "\n02. Search Book"
                  "\n03. View All Books"
                  "\n04. Update Book"
                  "\n====================================================="
                  "\n05. Register Member"
                  "\n06. Search Member"
                  "\n07. View All Members"
                  "\n08. Update Member"
                  "\n====================================================="
                  "\n09. Borrow Book"
                  "\n10. Search Borrowing History"
                  "\n11. View All Borrowing History"
                  "\n12. Return Book"
                  "\n00. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_book()

            elif choice == "2":
                get_book_by_id()

            elif choice == "3":
                list_all_books()

            elif choice == "4":
                update_book()

            elif choice == "5":
                add_member()

            elif choice == "6":
                get_member_by_id()

            elif choice == "7":
                list_all_members()

            elif choice == "8":
                update_member()

            elif choice == "9":
                borrow_book()

            elif choice == "10":
                get_loan_by_id()

            elif choice == "11":
                list_all_loans()

            elif choice == "12":
                return_book()

            elif choice == "0":
                exit()

            else:
                print("\nInvalid Menu Choice")


        except ValueError as e:
            print(str(f"\n{e}"))

        except Exception as e:
            print(f"\n{e}")


if __name__ == "__main__":

    main_cli()