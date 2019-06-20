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
        to_review = list(self.user_info.retreive_misspelled_words())
        if len(to_review) == 0:
            print("No words to review. Go Type-A-Book!")
            return
        print("Words to review")
        print(to_review)

        print("\n1st word:")
        self.type_word_5_times(to_review[0])
        
        self.user_info.remove_misspelled_word(to_review[0])


    def type_word_5_times(self, word_to_type):
        print("Type the word 5 times without making a mistake:")
        counter = 0
        while counter < 5:
            counter += 1
            print(counter)
            try:
                print("\nType:")
                self.type_this_word(word_to_type)
            except MisspelledWordException as e:
                print("What happened?:" + e.expected_word + ":" + e.actual_word)
                counter = 0

    def review_slowest_word(self):
        averages = self.user_info.retreive_typing_speeds_averages()
        print("Average speeds:" + str(averages))
        slowest_word = min(averages, key=averages.get)
        print("Slowest word:" + slowest_word + " " + str(averages[slowest_word]) + " wpm")

        self.type_word_5_times(slowest_word)

        new_averages = self.user_info.retreive_typing_speeds_averages()
        new_slowest_word = min(new_averages, key=new_averages.get)
        print("New slowest_word word:" + new_slowest_word + " " + str(averages[new_slowest_word]) + " wpm")


    def type_this_word(self, word_to_review):
        return_chars = [' ', chr(13)]

        print("'" + word_to_review + "'")
        time_word_start = time.time()
        input_char = ''
        input_word = ''
        while input_char not in return_chars and input_word != word_to_review:
            input_char = self._get_single_char()
            input_word += input_char
        else:
            time_word_stop = time.time()

        input_word = input_word.replace(str(chr(13)), "⏎")
        if input_word != word_to_review:
            raise MisspelledWordException(word_to_review, input_word)
        else:
            word_wpm = self.wpm_calc(time_word_start, time_word_stop, input_word)
            
            type_word_log_value = self.regex_alphanumeric.findall(word_to_review.lower())[0]
            self.user_info.log_words_typing_speeds({type_word_log_value:[word_wpm]})

        return input_word


    def _type_paragraph(self, paragraph_to_type):
        print("Type the words below")
        time_str_start = time.time()
        misspelled_words = set([])

        split_words = paragraph_to_type.split(" ")
        for idx, word_to_type in enumerate(split_words):
            while True:
                print(paragraph_to_type)

                if idx == len(split_words) - 1:
                    word_with_ending = word_to_type + "⏎"
                else:
                    word_with_ending = word_to_type + " "
                try:
                    self.type_this_word(word_with_ending)
                    break
                except MisspelledWordException as e:
                    print("\n!!Wrong Word:" + e.expected_word + ":" + e.actual_word + "::\n")
                    type_word_log_value = self.regex_alphanumeric.findall(word_to_type.lower())[0]
                    misspelled_words.add(type_word_log_value)
        else:
            time_str_stop = time.time()
            paragraph_wpm = self.wpm_calc(time_str_start, time_str_stop, paragraph_to_type + "⏎")

            print("\nComplete! Paragraph at " + str(paragraph_wpm) + " WPM")
            if len(misspelled_words) != 0:
                print("Misspelled Words:")
                print(misspelled_words)
                self.user_info.log_misspelled_words(misspelled_words)
                print("\n")


    def wpm_calc(self, time_start, time_stop, typed_word):
        time_total = time_stop - time_start
        char_per_sec = len(typed_word) / time_total
        words_per_sec = char_per_sec / 5
        words_per_min = words_per_sec * 60
        rounded = round(words_per_min, 2)
        return rounded
