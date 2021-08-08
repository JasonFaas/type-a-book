import unittest
from book_info.book_info import BookInfo

class TestBookInfo(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBookInfo, self).__init__(*args, **kwargs)
        self.book_info = BookInfo()

    def test_file_name_of_book(self):
        actual_file_name = self.book_info.book_file_name("Peter_Pan")
        assert actual_file_name == "16-0.txt", actual_file_name

    def test_peter_pan_chapter_list(self):
        chapter_list_new = self.book_info.chapter_list("Peter_Pan")
        expected_chapter_list = [
            "Chapter I. PETER BREAKS THROUGH",
            "Chapter II. THE SHADOW",
            "Chapter III. COME AWAY, COME AWAY!",
            "Chapter IV. THE FLIGHT",
            "Chapter V. THE ISLAND COME TRUE",
            "Chapter VI. THE LITTLE HOUSE",
            "Chapter VII. THE HOME UNDER THE GROUND",
            "Chapter VIII. THE MERMAIDS' LAGOON",
            "Chapter IX. THE NEVER BIRD",
            "Chapter X. THE HAPPY HOME",
            "Chapter XI. WENDY'S STORY",
            "Chapter XII. THE CHILDREN ARE CARRIED OFF",
            "Chapter XIII. DO YOU BELIEVE IN FAIRIES?",
            "Chapter XIV. THE PIRATE SHIP",
            "Chapter XV. \"HOOK OR ME THIS TIME\"",
            "Chapter XVI. THE RETURN HOME",
            "Chapter XVII. WHEN WENDY GREW UP",
        ]
        assert chapter_list_new == expected_chapter_list, chapter_list_new

    def test_alice_adventure_chapter_list(self):
        chapter_list_new = self.book_info.chapter_list("Alices_Adventures_in_Wonderland")
        expected_chapter_list = [
            'CHAPTER I. Down the Rabbit-Hole',
            'CHAPTER II. The Pool of Tears',
            'CHAPTER III. A Caucus-Race and a Long Tale',
            'CHAPTER IV. The Rabbit Sends in a Little Bill',
            'CHAPTER V. Advice from a Caterpillar',
            'CHAPTER VI. Pig and Pepper',
            'CHAPTER VII. A Mad Tea-Party',
            "CHAPTER VIII. The Queen's Croquet-Ground",
            "CHAPTER IX. The Mock Turtle's Story",
            'CHAPTER X. The Lobster Quadrille',
            'CHAPTER XI. Who Stole the Tarts?',
            "CHAPTER XII. Alice's Evidence"
        ]
        assert chapter_list_new == expected_chapter_list, chapter_list_new

    def test_next_chapter_line_in_book(self):
        actual_next_chapter = self.book_info.next_chapter_line_in_book('Chapter VI.')
        assert actual_next_chapter == 'Chapter VII.', ':{}:'.format(actual_next_chapter)

    def test_first_paragraph_of_chapter_of_book(self):
        paragraph_1_actual = self.book_info.paragraph_of_book("Peter_Pan", "Chapter I. PETER BREAKS THROUGH", 1)
        assert paragraph_1_actual == "Chapter I. PETER BREAKS THROUGH", paragraph_1_actual

    def test_second_paragraph_of_chapter_book(self):
        book_name = "Peter_Pan"
        chapter_name = "Chapter I. PETER BREAKS THROUGH"
        paragraph_number = 2
        paragraph_2_actual = self.book_info.paragraph_of_book(book_name, chapter_name, paragraph_number)
        assert paragraph_2_actual == "All children, except one, grow up. They soon know that they will grow up, and the way Wendy knew was this. One day when she was two years old she was playing in a garden, and she plucked another flower and ran with it to her mother. I suppose she must have looked rather delightful, for Mrs. Darling put her hand to her heart and cried, \"Oh, why can't you remain like this for ever!\" This was all that passed between them on the subject, but henceforth Wendy knew that she must grow up. You always know after you are two. Two is the beginning of the end.", "Actual:{}:".format(paragraph_2_actual)

    def test_last_paragraph_of_chapter_book(self):
        book_name = "Peter_Pan"
        chapter_name = "Chapter I. PETER BREAKS THROUGH"
        paragraph_number = 53
        paragraph_2_actual = self.book_info.paragraph_of_book(book_name, chapter_name, paragraph_number)
        paragraph_expected = "She started up with a cry, and saw the boy, and somehow she knew at once that he was Peter Pan. If you or I or Wendy had been there we should have seen that he was very like Mrs. Darling's kiss. He was a lovely boy, clad in skeleton leaves and the juices that ooze out of trees but the most entrancing thing about him was that he had all his first teeth. When he saw she was a grown-up, he gnashed the little pearls at her."

        assert paragraph_2_actual == paragraph_expected, "Actual:{}:".format(paragraph_2_actual)

    def test_paragraph_beyond_paragraphs_in_chapter_of_book(self):
        book_name = "Peter_Pan"
        paragraph_name = "Chapter I. PETER BREAKS THROUGH"
        paragraph_to_lookup = 54

        chapter_2_paragraph_1_actual = self.book_info.paragraph_of_book(book_name, paragraph_name, paragraph_to_lookup)

        assert chapter_2_paragraph_1_actual == "Chapter II. THE SHADOW", "Actual:{}:".format(chapter_2_paragraph_1_actual)


    def test_paragraph_last_chapter_of_book(self):
        book_name = "Peter_Pan"
        paragraph_name = "Chapter XVII. WHEN WENDY GREW UP"
        paragraph_to_lookup = 7

        chapter_last_paragraph_7_actual = self.book_info.paragraph_of_book(book_name, paragraph_name, paragraph_to_lookup)

        assert chapter_last_paragraph_7_actual == "\"We could lie doubled up,\" said Nibs.", "Actual:{}:".format(chapter_last_paragraph_7_actual)

    def test_beyond_last_chapter(self):
        book_name = "Peter_Pan"
        paragraph_name = "Chapter XVII. WHEN WENDY GREW UP"
        paragraph_to_lookup = 5000

        chapter_last_paragraph_7_actual = self.book_info.paragraph_of_book(book_name, paragraph_name,
                                                                               paragraph_to_lookup)

        assert chapter_last_paragraph_7_actual == "THE END", "Actual:{}:".format(
            chapter_last_paragraph_7_actual)

    def test_get_next_chapter(self):
        book_name = "Peter_Pan"
        next_chapter_actual = self.book_info.get_next_chapter(book_name, "Chapter VI. THE LITTLE HOUSE")
        assert next_chapter_actual == "Chapter VII. THE HOME UNDER THE GROUND", next_chapter_actual
