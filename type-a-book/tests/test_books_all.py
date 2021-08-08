import unittest
from book_info.book_info import BookInfo

class TestBooksAll(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBooksAll, self).__init__(*args, **kwargs)
        self.book_info = BookInfo()

    def test_book_list(self):
        assert self.book_info.book_list() == ['Alices_Adventures_in_Wonderland', 'Peter_Pan', ], self.book_info.book_list()

    def test_all_chapter_list(self):
        for book in self.book_info.book_list():
            chapter_list = self.book_info.chapter_list(book)
            print(chapter_list)
            chapter_count = len(chapter_list)
            assert 4 < chapter_count < 40, "Book {} does not have sufficient number of chapters {}".format(book, chapter_count)

    def test_verify_all_books_all_legal_characters(self):
        # TODO make this more efficient
        for book in self.book_info.book_list():
            text = self.book_info.contents_of_book_array(book)
            BookInfo.verify_legal_characters("\n".join(text), book)

    def test_first_paragraph_of_chapter_of_book(self):
        for book in self.book_info.book_list():
            chapter_list = self.book_info.chapter_list(book)


            first_chapter = self.book_info.paragraph_of_book(book, chapter_list[0], 1)
            assert first_chapter == chapter_list[0], '{} {}'.format(first_chapter, chapter_list[0])

            print("\n\n\nTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTESTTEST\n\n\n")
            last_chapter = self.book_info.paragraph_of_book(book, chapter_list[-1], 1000 * 1000)
            assert last_chapter == "THE END", last_chapter
