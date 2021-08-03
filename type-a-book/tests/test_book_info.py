import unittest
from book_info.book_info import BookInfo

class TestBookInfo(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBookInfo, self).__init__(*args, **kwargs)
        self.book_info = BookInfo()

    def test_book_list(self):
        assert self.book_info.book_list() == ['Peter_Pan', 'Alices_Adventures_in_Wonderland'], self.book_info.book_list()

    def test_peter_pan_chapter_list(self):
        assert self.book_info.chapter_list("Peter_Pan") == ["00A-Intro",
                                                  "01-Chapter_1",
                                                  "02-Chapter_2",
                                                  "03-Chapter_3"]

    def test_verify_all_books_all_legal_characters(self):
        # TODO make this more efficient
        for book in self.book_info.book_list():
            for chapter in self.book_info.chapter_list(book):
                text = self.book_info.chapter_of_book(book, chapter)
                BookInfo.verify_legal_characters(text)
