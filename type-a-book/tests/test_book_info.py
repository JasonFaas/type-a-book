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

    def test_file_name_of_book(self):
        actual_file_name = self.book_info.book_file_name("Peter_Pan")
        assert actual_file_name == "16-0.txt", actual_file_name

    def test_peter_pan_chapter_list_new(self):
        chapter_list_new = self.book_info.chapter_list_new("Peter_Pan")
        expected_chapter_list = [
            "Chapter I. PETER BREAKS THROUGH",
            "Chapter II. THE SHADOW",
            "Chapter III. COME AWAY, COME AWAY!",
            "Chapter IV. THE FLIGHT",
            "Chapter V. THE ISLAND COME TRUE",
            "Chapter VI. THE LITTLE HOUSE",
            "Chapter VII. THE HOME UNDER THE GROUND",
            "Chapter VIII. THE MERMAIDS’ LAGOON",
            "Chapter IX. THE NEVER BIRD",
            "Chapter X. THE HAPPY HOME",
            "Chapter XI. WENDY’S STORY",
            "Chapter XII. THE CHILDREN ARE CARRIED OFF",
            "Chapter XIII. DO YOU BELIEVE IN FAIRIES?",
            "Chapter XIV. THE PIRATE SHIP",
            "Chapter XV. “HOOK OR ME THIS TIME”",
            "Chapter XVI. THE RETURN HOME",
            "Chapter XVII. WHEN WENDY GREW UP",
        ]
        assert chapter_list_new == expected_chapter_list, chapter_list_new

    def test_alice_adventure_chapter_list_new(self):
        chapter_list_new = self.book_info.chapter_list_new("Alices_Adventures_in_Wonderland")
        expected_chapter_list = [
            "CHAPTER I.     Down the Rabbit-Hole",
            "CHAPTER II.    The Pool of Tears",
            "CHAPTER III.   A Caucus-Race and a Long Tale",
            "CHAPTER IV.    The Rabbit Sends in a Little Bill",
            "CHAPTER V.     Advice from a Caterpillar",
            "CHAPTER VI.    Pig and Pepper",
            "CHAPTER VII.   A Mad Tea-Party",
            "CHAPTER VIII.  The Queen’s Croquet-Ground",
            "CHAPTER IX.    The Mock Turtle’s Story",
            "CHAPTER X.     The Lobster Quadrille",
            "CHAPTER XI.    Who Stole the Tarts?",
            "CHAPTER XII.   Alice’s Evidence",
        ]
        assert chapter_list_new == expected_chapter_list, chapter_list_new

    def test_verify_all_books_all_legal_characters(self):
        # TODO make this more efficient
        for book in self.book_info.book_list():
            for chapter in self.book_info.chapter_list(book):
                text = self.book_info.chapter_of_book(book, chapter)
                BookInfo.verify_legal_characters(text)

    def test_chapter_of_book(self):
        paragraph_1_actual = self.book_info.paragraph_of_book_new("Peter_Pan", "Chapter I. PETER BREAKS THROUGH", 1)
        assert paragraph_1_actual == "Chapter I. PETER BREAKS THROUGH", paragraph_1_actual
        paragraph_2_actual = self.book_info.paragraph_of_book_new("Peter_Pan", "Chapter I. PETER BREAKS THROUGH", 2)
        assert paragraph_2_actual == "All children, except one, grow up. They soon know that they will grow up, and the way Wendy knew was this. One day when she was two years old she was playing in a garden, and she plucked another flower and ran with it to her mother. I suppose she must have looked rather delightful, for Mrs. Darling put her hand to her heart and cried, “Oh, why can’t you remain like this for ever!” This was all that passed between them on the subject, but henceforth Wendy knew that she must grow up. You always know after you are two. Two is the beginning of the end.", "Actual:{}:".format(paragraph_2_actual)

    def test_last_chapter_of_book(self):
        # TODO: Write this!
        # Likely just "THE END"
        pass
