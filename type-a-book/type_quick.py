from book_info.book_info import BookInfo
from print_to_screen.print_screen import PrintScreen
from print_to_screen.screen_input import ScreenInput
from type_exceptions import MisspelledWordException
from type_stuff import TypeStuff
from user_info import UserInfo
from api_request import ApiRequest


class TypeQuick():
    def __init__(self, user_name):
        self.user_info = UserInfo(user_name)
        self.type_stuff = TypeStuff(user_name)
        self.book_info = BookInfo()
        self.api_request = ApiRequest()
        self.print_screen = PrintScreen(self.book_info)
        self.screen_input = ScreenInput(self.book_info)

    def short(self):
        self.type_stuff._type_paragraph("The quick and-the fast!")

    def long(self):
        self.type_stuff._type_paragraph("The quick brown fox jumps over the lazy dog. " + 
            "No kidding, Lorenzo called off his trip to Mexico City just because they told him the conquistadors were extinct.")

    def print_char_info(self):
        while True:
            single_char = self.type_stuff._get_single_char()
            print("ASCII Value: " + str(ord(single_char)))

    def type_a_book(self):
        while True:
            self.print_screen.book_list()
            book_chosen = self.screen_input.book_to_type()
            book_chapters = self.book_info.chapter_list(book_chosen)
            if len(book_chapters) > 0:
                break
            else:
                print("Wrong choice '" + book_chosen + "'")

        self.print_screen.chapter_list(book_chapters)

        all_book_positions = self.user_info.retreive_book_positions()
        print("\t" + "\"Start\"-Start at the beginning?")
        if book_chosen.replace(" ", "_") in all_book_positions:
            book_position = all_book_positions[book_chosen.replace(" ", "_")]
            print("\t" + "\"Resume\"-Continue at \"{}\" paragraph {}".format(book_position["Chapter"], book_position["Paragraph"]))

        while True:
            chapter_chosen = input("Choose chapter from above list:")

            if chapter_chosen == "Start":
                chapter_chosen = book_chapters[0]
                paragraph_chosen = 1
                break
            elif chapter_chosen == "Resume":
                book_pos_info = all_book_positions[book_chosen]
                chapter_chosen = book_pos_info["Chapter"]
                paragraph_chosen = book_position["Paragraph"]
                break
            elif chapter_chosen in book_chapters:
                paragraph_chosen = 1
                break
            else:
                print("Wrong choice '" + chapter_chosen + "'")

        print("Starting to type {} at Chapter {} Paragraph {}.\n".format(book_chosen, chapter_chosen, paragraph_chosen))

        # New paradigm
        self.user_info.log_book_position(book_chosen,
                                         {"Chapter": chapter_chosen,
                                          "Paragraph": paragraph_chosen})
        paragraph_to_type = self.book_info.paragraph_of_book(book_chosen, chapter_chosen, paragraph_chosen)
        while True:
            self.type_stuff._type_paragraph(paragraph_to_type)

            paragraph_chosen += 1
            paragraph_to_type = self.book_info.paragraph_of_book(book_chosen, chapter_chosen, paragraph_chosen)
            if paragraph_to_type == self.book_info.get_next_chapter(book_chosen, chapter_chosen):
                chapter_chosen = paragraph_to_type
                paragraph_to_type = 1

            self.user_info.log_book_position(
                book_chosen,
                {"Chapter": chapter_chosen, "Paragraph": paragraph_chosen}
            )

    def review_misspelled(self):
        to_review = list(self.user_info.retreive_misspelled_words())
        if len(to_review) == 0:
            print("No words to review. Go Type-A-Book!")
            return
        print("{} words to review".format(len(to_review)))
        # print(to_review)

        try:
            print("Looking up '{}' online".format(to_review[0]))
            self._review_with_definition(to_review[0])
        except LookupError as e: 
            print(e)
            print("'{}' not found online".format(to_review[0]))
            self._type_word_5_times(to_review[0])
        
        self.user_info.remove_misspelled_word(to_review[0])


    def review_slowest_word(self):
        before_averages = self.user_info.retreive_typing_speeds_averages()

        values = before_averages.values()
        print(" 100+ WPM Word count: {}".format(len(list(x for x in values if 100 < x < 1000))))
        print("75-99 WPM Word count: {}".format(len(list(x for x in values if 75 < x < 100))))
        print("50-74 WPM Word count: {}".format(len(list(x for x in values if 50 < x < 75))))
        print(" 0-49 WPM Word count: {}".format(len(list(x for x in values if 1 < x < 50))))
        # print("Average speeds:" + str(before_averages))
        
        before_slowest_word = min(before_averages, key=before_averages.get)
        print("Slowest word:" + before_slowest_word + " " + str(before_averages[before_slowest_word]) + " wpm")

        self._type_word_5_times(before_slowest_word)

        after_averages = self.user_info.retreive_typing_speeds_averages()
        print(before_slowest_word + " improved from " + str(before_averages[before_slowest_word]) + " to " + str(after_averages[before_slowest_word]))

        new_slowest_word = min(after_averages, key=after_averages.get)
        print("New slowest_word word:" + new_slowest_word + " " + str(before_averages[new_slowest_word]) + " wpm")


    def _review_with_definition(self, word_to_type):

        word_info = self.api_request.word_info(word_to_type)
        print("Review '{}' by typing the word and definition:\n".format(word_to_type))

        build_a_parapgraph = "{} {} {}.".format(word_to_type.title(), 
                                               word_to_type, 
                                               word_to_type)
        build_a_parapgraph += " Type: {}.".format(word_info.part_of_language())

        build_a_parapgraph += " Meaning: {}.".format("; ".join(word_info.definitions()))
        build_a_parapgraph += " Examples: {}".format(" ".join(word_info.sentences()))

        derivative = word_info.derivative_of()
        if derivative != "":
            derivative_info = self.api_request.word_info(derivative)
            build_a_parapgraph += " Derivative info: {} is derivative of {}. Derivative meaning: {}.".format(word_to_type, derivative, "; ".join(derivative_info.definitions()))

        build_a_parapgraph += " {} {} {}".format(word_to_type.upper(), 
                                               word_to_type, 
                                               word_to_type)

        self.type_stuff._type_paragraph(build_a_parapgraph)


    def _type_word_5_times(self, word_to_type):
        print("\nType '{}' 5 times without making a mistake:".format(word_to_type))
        counter = 0
        words_speeds = {}
        words_speeds[word_to_type] = []
        while counter < 5:
            counter += 1
            print(counter)
            try:
                wpm = self.type_stuff.type_this_word(word_to_type)
                words_speeds[word_to_type].append(wpm)
            except MisspelledWordException as e:
                print("What happened?: " + e.expected_word + " : " + e.actual_word + " :")
                counter = 0
        else:
            self.user_info.log_words_typing_speeds(words_speeds)
