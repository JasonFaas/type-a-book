import time
import pprint
import readchar
import re

from type_exceptions import MisspelledWordException
from user_info import UserInfo

class TypeQuick():
    def __init__(self, user_name):
        self.user_info = UserInfo(user_name)
        self.regex_alphanumeric = re.compile('\\w+')

    def short(self):
        self._type_paragraph("The quick and the fast!")

    def long(self):
        self._type_paragraph("The quick brown fox jumps over the lazy dog. " + 
            "No kidding, Lorenzo called off his trip to Mexico City just because they told him the conquistadors were extinct.")

    def print_char_info(self):
        while True:
            single_char = self._get_single_char()
            print("ASCII Value: " + str(ord(single_char)))

    def _get_single_char(self):
        input_char = readchar.readchar()
        if ord(input_char) == 3:
            raise Exception("Contrl+C Detected")
        return input_char

    def review_misspelled(self):
        # TODO: display list of misspelled words
        to_review = list(self.user_info.retreive_misspelled_words())
        if len(to_review) == 0:
            print("No words to review. Go Type-A-Book!")
            return
        print("Words to review")
        print(to_review)

        print("\n1st word:")
        print("Type the word 5 times without making a mistake:")
        counter = 0
        while counter < 5:
            counter += 1
            print(counter)
            try:
                self.review_word(to_review[0])
            except MisspelledWordException as e:
                print("What happened?:" + e.expected_word + ":" + e.actual_word)
                count = 0
        self.user_info.remove_misspelled_word(to_review[0])


    def review_word(self, word_to_review):
        input_word = ""
        return_chars = [' ', chr(13)]

        while input_word != word_to_review:
            input_word = ""
            print("\nType:")
            print(word_to_review)
            type_word_log_value = self.regex_alphanumeric.findall(word_to_review.lower())[0]
            time_word_start = time.time()
            input_char = ''
            while input_char not in return_chars and input_word != word_to_review:
                input_word += input_char
                input_char = self._get_single_char()
            else:
                time_word_stop = time.time()

            if input_word != word_to_review:
                raise MisspelledWordException(word_to_review, input_word)
            else:
                word_wpm = self.wpm_calc(time_word_start, time_word_stop, input_word)
                self.user_info.log_words_typing_speeds({input_word:[word_wpm]})


    def _type_paragraph(self, type_string):
        print("Type the words below")
        time_str_start = time.time()

        spelled_words_and_time = {}
        misspelled_words = set([])

        split_words = type_string.split(" ")
        for idx, type_word in enumerate(split_words):
            input_word = ""
            return_chars = [' ', chr(13)]

            while input_word != type_word:
                input_word = ""
                print(type_string)
                if idx == len(split_words) - 1:
                    print(type_word + "⏎")
                else:
                    print(type_word)
                type_word_log_value = self.regex_alphanumeric.findall(type_word.lower())[0]
                time_word_start = time.time()
                input_char = ''
                while input_char not in return_chars:
                    input_word += input_char
                    input_char = self._get_single_char()
                else:
                    time_word_stop = time.time()

                if input_word != type_word:
                    misspelled_words.add(type_word_log_value)
                    print("\n!!Wrong Word!!\n")
                else:
                    word_wpm = self.wpm_calc(time_word_start, time_word_stop, type_word + " ")

                    if type_word_log_value not in spelled_words_and_time:
                        spelled_words_and_time[type_word_log_value] = []
                    spelled_words_and_time[type_word_log_value].append(word_wpm)
                        
        else:
            time_str_stop = time.time()
            print("\n\nComplete!")
            print(self.wpm_calc(time_str_start, time_str_stop, type_string))
            if len(misspelled_words) != 0:
                print("Misspelled Words:")
                print(misspelled_words)
                self.user_info.log_misspelled_words(misspelled_words)
                print("\n")

        self.user_info.log_words_typing_speeds(spelled_words_and_time)

    def wpm_calc(self, time_start, time_stop, type_word):
        time_total = time_stop - time_start
        char_per_sec = len(type_word) / time_total
        words_per_sec = char_per_sec / 5
        words_per_min = words_per_sec * 60
        rounded = round(words_per_min, 2)
        return rounded
