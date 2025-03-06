from book_dao import BookDAO
from book import Book

class TestBookDAO:
    def setup_method(self): # Denna metod används i samband med testning i python och för vårat testbiblotek
        self.dao = BookDAO("test_db.sqlite") # Denna rad skapar ett nytt objekt av klassen BookDAO
        self.dao.clear_table() # Denna rad rensar tabellen så att den är tom och att vi säkerställer att det inte finns någon data innan man kör ett nytt test
        

        self.dao.insert_book(Book("Book1", "ABCD", "Karl Franz"))
        self.dao.insert_book(Book("Book2", " DVBD", "Franz Karl"))
        self.dao.insert_book(Book("Book3", "UHUH", "Ghurmak"))
        

    def teardown_method(self):
        self.dao.clear_table()
        self.dao.close()

    def test_get_all_books(self):

        books = self.dao.get_all_books()
        assert len(books) == 3
        assert books[0].title == "Book1"
        assert books[1].title == "Book2"
        assert books[2].title == "Book3"
    
    def test_insert_new_book(self):

        new_book = Book("Mordet på masken", "Ett erkännande av mordet om den döda masken", "George Bush")
        book_id = self.dao.insert_book(new_book)

        saved_book = self.dao.find_by_title("Mordet på masken")
        assert saved_book is not None
        assert saved_book.id == book_id
        assert saved_book.title == "Mordet på masken"
        assert saved_book.description == "Ett erkännande av mordet om den döda masken"
        assert saved_book.author == "George Bush"

    def test_find_book_by_title(self):

        book = self.dao.find_by_title("Book2")
        assert book is not None
        assert book.title == "Book2"
        assert book.author == "Franz Karl"

    def test_find_book_by_title_and_update_description(self):

        book = self.dao.find_by_title("Book1")
        assert book is not None

        book.description = "En thriller om en borttappad tand."
        self.dao.update_book(book)

        updated_book = self.dao.find_by_title("Book1")
        assert updated_book.description == "En thriller om en borttappad tand."

    def test_delete_book(self):
        book = self.dao.find_by_title("Book3")
        assert book is not None

        self.dao.delete_book(book)
        assert self.dao.find_by_title("Book3") is None
        assert self.dao.find_by_title("Book3") == None
