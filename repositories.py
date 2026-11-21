from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List, Dict

from library_management_system.models import Book, Member, Loan


class BookRepository(ABC):

    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def get_by_id(self, book_id: str) -> Optional[Book]:
        pass

    @abstractmethod
    def list_all_books(self) -> List[Book]:
        pass

    @abstractmethod
    def update_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def save(self):
        pass


class MemberRepository(ABC):

    @abstractmethod
    def add_member(self, member: Member) -> None:
        pass

    @abstractmethod
    def get_by_id(self, member_id: str) -> Optional[Member]:
        pass

    @abstractmethod
    def list_all_members(self) -> List[Member]:
        pass

    @abstractmethod
    def update_member(self, member: Member) -> None:
        pass

    @abstractmethod
    def save(self):
        pass


class LoanRepository(ABC):

    @abstractmethod
    def add_loan(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def get_by_id(self, loan_id: str) -> Optional[Loan]:
        pass

    @abstractmethod
    def list_all_loans(self) -> List[Loan]:
        pass

    @abstractmethod
    def update_loan(self, loan: Loan) -> None:
        pass

    @abstractmethod
    def save(self):
        pass



class FileBasedBookRepository(BookRepository):

    def __init__(self, filename: str = "books.txt"):
        self.filename = filename
        self.books: Dict[str, Book] = {}
        self.load()

    def load(self):

        try:
            with open(self.filename, "r+") as file:

                for data in file:
                    split_data = data.strip().split(",")
                    book = Book(book_id=split_data[0],
                                title=split_data[1],
                                author=split_data[2],
                                year=split_data[3],
                                book_lend_member_id=
                                None if split_data[4] == "None" else str(split_data[4]))

                    self.books[book.book_id] = book

        except FileNotFoundError as e:
            print(e)

    def save(self):

        with open("books.txt", "w") as f:

            for book in self.books.values():

                f.write(f"{book.book_id},{book.title},{book.author},{book.year},{book.book_lend_member_id}\n")

    def add_book(self, book: Book) -> None:
        self.books[book.book_id] = book
        self.save()

    def list_all_books(self) -> List[Book]:
        return list (self.books.values())

    def update_book(self, book: Book) -> None:
        if self.books.get(book.book_id) is None:
            raise ValueError("This book doesn't exists in library")

        self.books[book.book_id] = book
        self.save()

    def get_by_id(self, book_id: str) -> Optional[Book]:
        return self.books.get(book_id)


class FileBasedMemberRepository(MemberRepository):

    def __init__(self, filename: str = "members.txt"):
        self.filename = filename
        self.members: Dict[str, Member] = {}
        self.load()

    def load(self):

        try:
            with open("members.txt", "r+") as file:

                for data in file:
                    split_data = data.strip().split(",")
                    member = Member(member_id=split_data[0],
                                    name=split_data[1],
                                    contact=split_data[2])

                    self.members[member.member_id] = member

        except FileNotFoundError as e:
            print(e)

    def save(self):

        with open("members.txt", "w") as f:

            for member in self.members.values():
                f.write(f"{member.member_id},{member.name},{member.contact}\n")

    def add_member(self, member: Member) -> None:
        self.members[member.member_id] = member
        self.save()

    def get_by_id(self, member_id: str) -> Optional[Member]:
        return self.members.get(member_id)

    def list_all_members(self) -> List[Member]:
        return list (self.members.values())

    def update_member(self, member: Member) -> None:
        if self.members.get(member.member_id) is None:
            raise ValueError("Member doesn't exists")

        self.members[member.member_id] = member
        self.save()


class FileBasedLoanRepository(LoanRepository):

    def __init__(self, filename: str = "loans.txt"):
        self.filename = filename
        self.loans: Dict[str, Loan] = {}
        self.load()

    def load(self):

        try:
            with open("loans.txt", "r+") as file:

                for data in file:
                    split_data = data.strip().split(",")
                    loan = Loan(loan_id=split_data[0],
                                member_id=split_data[1],
                                book_id=split_data[2],
                                borrowed_at=datetime.strptime(split_data[3],"%Y-%m-%d %H:%M:%S"),
                                returned_at=
                                None if split_data[4] == "None" else
                                datetime.strptime(split_data[4],"%Y-%m-%d %H:%M:%S"))

                    self.loans[loan.loan_id] = loan

        except FileNotFoundError as e:
            print(e)

    def save(self):

        with open("loans.txt", "w") as f:

            for loan in self.loans.values():
                f.write(f"{loan.loan_id},{loan.member_id},{loan.book_id},{loan.borrowed_at},{loan.returned_at}\n")

    def add_loan(self, loan: Loan) -> None:
        self.loans[loan.loan_id] = loan
        self.save()

    def get_by_id(self, loan_id: str) -> Optional[Loan]:
        return self.loans.get(loan_id)

    def list_all_loans(self) -> List[Loan]:
        return list (self.loans.values())

    def update_loan(self, loan: Loan) -> None:
        if self.loans.get(loan.loan_id) is None:
            raise ValueError("Loan doesn't exists")

        self.loans[loan.loan_id] = loan
        self.save()