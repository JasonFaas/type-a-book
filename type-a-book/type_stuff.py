import re
import readchar
import time

from type_exceptions import MisspelledWordException
from user_info import UserInfo

class TypeStuff():

    def __init__(self, user_name):
        self.regex_log_word = re.compile(r"['A-Za-z0-9_-]+")
        self.user_info = UserInfo(user_name)

    def _get_single_char(self):
        input_char = readchar.readchar()
        if ord(input_char) == 3:
            raise Exception("Contrl+C Detected")
        return input_char

    def type_this_word(self, word_to_review):
        return_chars = [' ', chr(13)]

        # print("'" + word_to_review + "'")
        input_char = self._get_single_char()
        time_word_start = time.time()
        input_word = "" + input_char
        while word_to_review.startswith(input_word) \
              and input_char not in return_chars \
              and input_word != word_to_review:
            input_char = self._get_single_char()
            input_word += input_char

        time_word_stop = time.time()

        input_word = input_word.replace(str(chr(13)), "⏎")
        if input_word != word_to_review:
            raise MisspelledWordException(word_to_review, input_word)
        else:
            word_wpm = self.wpm_calc(time_word_start, time_word_stop, word_to_review)
            
            type_word_log_value = self.regex_log_word.findall(word_to_review.lower())[0]
            self.user_info.log_words_typing_speeds({type_word_log_value:[word_wpm]})

        return word_wpm


    def _type_paragraph(self, paragraph_to_type):
        # print("Type the words below\n")
        time_str_start = time.time()
        misspelled_words = set([])
        words_speeds = {}
        split_words = paragraph_to_type.split(" ")
        for word_to_type in split_words:
            type_word_log_value = self.regex_log_word.findall(word_to_type.lower())[0]
            words_speeds[type_word_log_value] = []

        paragraph_display = "{}⏎".format(paragraph_to_type)
        display_offset = 0
        print(paragraph_display)
        for idx, word_to_type in enumerate(split_words):
            while True:
                type_word_log_value = self.regex_log_word.findall(word_to_type.lower())[0]
                # print(paragraph_display)

                if idx == len(split_words) - 1:
                    word_with_ending = word_to_type + "⏎"
                else:
                    word_with_ending = word_to_type + " "
                try:
                    wpm = self.type_this_word(word_with_ending)
                    words_speeds[type_word_log_value].append(wpm)
                    display_offset += len(word_with_ending)
                    break
                except MisspelledWordException as e:
                    print("\n!!Wrong Word:" + e.expected_word + ":" + e.actual_word + "::\n")
                    misspelled_words.add(type_word_log_value)
                    paragraph_display = paragraph_display[display_offset:]
                    display_offset = 0
                    print(paragraph_display)


        else:
            time_str_stop = time.time()
            paragraph_wpm = self.wpm_calc(time_str_start, time_str_stop, paragraph_to_type + "⏎")

            self.user_info.log_words_typing_speeds(words_speeds)

            print("\nComplete! Paragraph at " + str(paragraph_wpm) + " WPM")
            if len(misspelled_words) != 0:
                print("Misspelled Words:")
                print(misspelled_words)
                self.user_info.log_misspelled_words(misspelled_words)
                print("\n")

    def type_chapter(self, full_chapter_text, book_chosen, chapter_chosen, starting_index=0):
        paragraphs = full_chapter_text.split('\n')
        for idx, section in enumerate(paragraphs[starting_index:]):
            if len(section) > 1:
                self._type_paragraph(section)
                self.user_info.log_book_position(book_chosen, 
                                                {"Chapter":chapter_chosen, 
                                                 "Paragraph":1+idx+starting_index})


    def wpm_calc(self, time_start, time_stop, typed_word):
        time_total = time_stop - time_start
        char_per_sec = len(typed_word) / time_total
        words_per_sec = char_per_sec / 5
        words_per_min = words_per_sec * 60
        rounded = round(words_per_min, 2)
        return rounded

    def unit_tests(self):
        regex_verify = [["what", "what"],
                        ["what-t'he", "what-t'he"],
                        ["what-the.", "what-the"]]
        for word, expected_word in regex_verify:
            actual_regex = self.regex_log_word.findall(word)[0]
            if actual_regex != expected_word:
                print(actual_regex)
                print(expected_word)
            assert actual_regex == expected_word        
