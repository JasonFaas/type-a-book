import time
import pprint
import readchar

class TypeQuick():

    def short(self):
        self.type_paragraph("The quick and the fast")

    def long(self):
        self.type_paragraph("The quick brown fox jumps over the lazy dog")

    def single_char(self):
        while True:
            input_char = readchar.readchar()
            print("ASCII Value: " + str(ord(input_char)))
            if ord(input_char) == 3:
                raise Exception("Contrl+C Detected")



    def type_paragraph(self, type_string):
        print("Type the words below")
        time_str_start = time.time()

        spelled_words_and_time = {}
        misspelled_words = set([])

        for idx, type_word in enumerate(type_string.split(" ")):
            input_word = ""
            return_chars = [' ', chr(13)]

            while input_word != type_word:
                input_word = ""
                print(type_string)
                print(type_word)
                time_word_start = time.time()
                input_char = readchar.readchar()
                while input_char not in return_chars:
                    if ord(input_char) == 3:
                        raise Exception("Contrl+C Detected")
                    input_word += input_char
                    input_char = readchar.readchar()
                else:
                    time_word_stop = time.time()

                if input_word != type_word:
                    misspelled_words.add(type_word)
                    print("\n!!Wrong Word!!\n")
                else:
                    word_wpm = self.wpm_calc(time_word_start, time_word_stop, type_word)

                    if type_word.lower() in spelled_words_and_time:
                        spelled_words_and_time[type_word.lower()].append(word_wpm)
                    else:
                        spelled_words_and_time[type_word.lower()] = [word_wpm, ]

        else:
            time_str_stop = time.time()
            print("\n\nComplete!")
            print(self.wpm_calc(time_str_start, time_str_stop, type_string))
            if len(misspelled_words) != 0:
                print("misspelled_words:")
                print(misspelled_words)
                print("\n")

        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(str(spelled_words_and_time))

    def wpm_calc(self, time_start, time_stop, type_word):
        time_total = time_stop - time_start
        char_per_sec = (len(type_word) + 1) / time_total
        words_per_sec = char_per_sec / 5
        words_per_min = words_per_sec * 60
        rounded = round(words_per_min, 2)
        return rounded