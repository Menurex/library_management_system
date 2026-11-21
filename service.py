from dataclasses import dataclass
from typing import Optional, List

from library_management_system.models import Book, Member, Loan
from library_management_system.repositories import BookRepository, MemberRepository, LoanRepository


@dataclass
class LibraryManagementService:

    book_repository: BookRepository
    member_repository: MemberRepository
    loan_repository: LoanRepository

    def add_book(self, book: Book) -> Optional[Book]:

        if self.book_repository.get_by_id(book_id=book.book_id) is not None:
            raise ValueError("Book already exists")

        self.book_repository.add_book(book=book)

        return book

    def get_book_by_id(self, book_id: str) -> Optional[Book]:
        if self.book_repository.get_by_id(book_id=book_id) is None:
            raise ValueError(f"No book in the library related to id - {book_id}")

        return self.book_repository.get_by_id(book_id=book_id)

    def list_all_books(self) -> List[Book]:
        if len(self.book_repository.list_all_books()) == 0:
            raise ValueError("No books in the list")

        return self.book_repository.list_all_books()

    def update_book(self, book: Book) -> None:

        if self.book_repository.get_by_id(book_id=book.book_id) is None:
            raise ValueError(f"No book in the library related to id - {book.book_id}")

        self.book_repository.update_book(book=book)

    def add_member(self, member: Member) -> None:

        if self.member_repository.get_by_id(member_id=member.member_id) is not None:
            raise ValueError("Member already added")

        self.member_repository.add_member(member=member)

    def get_member_by_id(self, member_id: str) -> Optional[Member]:

        if self.member_repository.get_by_id(member_id=member_id) is None:
            raise ValueError("No member registered for this member ID")

        return self.member_repository.get_by_id(member_id=member_id)

    def list_all_members(self) -> List[Member]:

        if len(self.member_repository.list_all_members()) == 0:
            raise ValueError("No members to view")

        return self.member_repository.list_all_members()

    def update_member(self, member: Member) -> None:

        if self.member_repository.get_by_id(member_id=member.member_id) is None:
            raise ValueError("No member registered to this member ID")

        self.member_repository.update_member(member=member)


    def add_loan(self, loan: Loan) -> None:

        if self.loan_repository.get_by_id(loan_id=loan.loan_id) is not None:
            raise ValueError("Loan ID already added")

        if self.member_repository.get_by_id(member_id=loan.member_id) is None:
            raise ValueError("No member registered to this member ID")

        if self.book_repository.get_by_id(book_id=loan.book_id) is None:
            raise ValueError("NO book registered to this book ID")

        book = self.book_repository.get_by_id(book_id=loan.book_id)

        if book.book_lend_member_id is not None:
            raise ValueError("This book already borrowed")

        self.loan_repository.add_loan(loan=loan)
        self.book_repository.save()

    def get_loan_by_id(self, loan_id: str) -> Optional[Loan]:

        if self.loan_repository.get_by_id(loan_id=loan_id) is None:
            raise ValueError("No loan have been given to this Loan ID")

        return self.loan_repository.get_by_id(loan_id=loan_id)

    def list_all_loans(self) -> List[Loan]:

        if len(self.loan_repository.list_all_loans()) == 0:
            raise ValueError("No loans to view")

        return self.loan_repository.list_all_loans()

    def update_loan(self, loan: Loan) -> None:

        if self.loan_repository.get_by_id(loan_id=loan.loan_id) is None:
            raise ValueError("No loan have been given to this loan ID")

        self.loan_repository.update_loan(loan=loan)
        self.book_repository.save()