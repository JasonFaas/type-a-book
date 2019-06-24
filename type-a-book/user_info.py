import json
import os
import statistics

class UserInfo():
    def __init__(self, user_name):
        self.user_name = user_name.replace(" ", "_")
        self.misspelled_file_name = "../resources/user-info/{}-words-misspelled.txt".format(self.user_name)
        self.words_speeds_file_name = "../resources/user-info/{}-words-typing-speed.txt".format(self.user_name)
        self.book_positions_file_name = "../resources/user-info/{}-books-positions.txt".format(self.user_name)
        self.max_speeds_logged = 5

    def log_misspelled_words(self, word_list, file_write_style = 'a'):
        f = open(self.misspelled_file_name, file_write_style)
        for word in word_list:
            f.write(word + "\n")
        f.close()

    def remove_misspelled_word(self, word_to_remove):
        curr_set = self.retreive_misspelled_words()
        curr_set.remove(word_to_remove)
        self.log_misspelled_words(curr_set, 'w')

    def retreive_misspelled_words(self):
        f = open(self.misspelled_file_name, "r")
        word_list = set()
        for line in f:
            if len(line) > 2:
                word_list.add(line[:-1])
        f.close()
        return word_list

    def log_words_typing_speeds(self, typing_speeds):
        current_speeds = self.retreive_typing_speeds()

        for word, speeds in typing_speeds.items():
            if word not in current_speeds:
                current_speeds[word] = []

            for speed in speeds:
                current_speeds[word].append(speed)

            current_speeds[word] = current_speeds[word][self.max_speeds_logged * -1:]

        f = open(self.words_speeds_file_name, 'w')
        for word, speeds in current_speeds.items():
            f.write(str(speeds) + str(word) + "\n")
        f.close()

    def log_book_position(self, new_book, new_info):
        current_positions = self.retreive_book_positions()
        current_positions[new_book] = new_info

        with open(self.book_positions_file_name, 'w') as file:
             file.write(json.dumps(current_positions))

    def retreive_book_positions(self):
        if not os.path.exists(self.book_positions_file_name):
            return {}

        f = open(self.book_positions_file_name, 'r')
        s = f.read()
        return_val = eval(s)
        f.close()
        return return_val

    def remove_book_position(self, book_to_remove):
        if not os.path.exists(self.book_positions_file_name):
            return

        book_positions = self.retreive_book_positions()
        del book_positions[book_to_remove]

        with open(self.book_positions_file_name, 'w') as file:
             file.write(json.dumps(book_positions))

    def _words_and_speeds_from_file_line(self, line):
        line = line.replace(" ", "")

        seperator_point = line.index("]")

        word = line[seperator_point+1:]
        speed_list_str = line[1:seperator_point].split(",")
        speed_list_float = []
        for speed_str in speed_list_str:
            speed_list_float.append(float(speed_str))
        return word, speed_list_float

    def retreive_typing_speeds(self):
        if not os.path.exists(self.words_speeds_file_name):
            return {}
        f = open(self.words_speeds_file_name, 'r')
        speed_info = {}
        for line in f:
            word, speed_list = self._words_and_speeds_from_file_line(line[:-1])
            speed_info[word] = speed_list
        f.close()
        return speed_info

    def retreive_typing_speeds_averages(self):
        word_speeds = self.retreive_typing_speeds()
        word_averages = {}
        for word, speeds in word_speeds.items():
            word_averages[word] = round(statistics.mean(speeds), 2)

        return word_averages

    def unit_tests(self):
        # line parsing
        word, speed_list = self._words_and_speeds_from_file_line("[160.79, 155.14, 155.16, 113.9, 118.46]is,")
        assert word == "is,"
        assert speed_list == [160.79, 155.14, 155.16, 113.9, 118.46]

        word, speed_list = self._words_and_speeds_from_file_line("[160.79, 155.14, 155.16, 113.9, 118.46]is,:")
        assert word == "is,:"
        assert speed_list == [160.79, 155.14, 155.16, 113.9, 118.46]


        # misspelled words
        if os.path.exists(self.misspelled_file_name):
            os.remove(self.misspelled_file_name)
        self.log_misspelled_words({"what", " ", "that"})
        misspelled_words = self.retreive_misspelled_words()
        if misspelled_words != {'what', 'that'}:
            raise Exception("Failure:" + str(misspelled_words) + ":")

        # remove misspelled word
        if os.path.exists(self.misspelled_file_name):
            os.remove(self.misspelled_file_name)
        self.log_misspelled_words({"what", "that"})
        self.remove_misspelled_word("what")
        misspelled_words = self.retreive_misspelled_words()
        if misspelled_words != {'that'}:
            raise Exception("Failure:" + str(misspelled_words) + ":")

        # add duplicate word
        self.log_misspelled_words({"that"})
        self.log_misspelled_words({"that"})
        misspelled_words = self.retreive_misspelled_words()
        if misspelled_words != {'that'}:
            raise Exception("Failure:" + str(misspelled_words) + ":")


        # user typing speeds
        if os.path.exists(self.words_speeds_file_name):
            os.remove(self.words_speeds_file_name)
        expected_typing_speeds = {"what":[30.4, 40.2], "that":[30.2]}
        self.log_words_typing_speeds(expected_typing_speeds)
        actual_typing_speeds = self.retreive_typing_speeds()
        if actual_typing_speeds != expected_typing_speeds:
            raise Exception("Failure:" + str(actual_typing_speeds) + ":")

        round_2_typing_speeds = {'what':[11.1, 22.2, 33.3, 44.4], 'hello':[3.3, 4.4], 'that':[22.2]}
        self.log_words_typing_speeds(round_2_typing_speeds)
        round_2_expected = {'what':[40.2, 11.1, 22.2, 33.3, 44.4], 'that':[30.2, 22.2], 'hello':[3.3, 4.4]}
        round_2_actual = self.retreive_typing_speeds()
        if round_2_actual != round_2_expected:
            raise Exception("Failure:" + str(round_2_actual) + ":")

        round_2_averages_expected = {'what':30.24, 'that':26.20, 'hello':3.85}
        round_2_averages_actual = self.retreive_typing_speeds_averages()
        if round_2_averages_actual != round_2_averages_expected:
            raise Exception("Failure:" + str(round_2_averages_actual) + ":")
        
        # log location of book
        if os.path.exists(self.book_positions_file_name):
            os.remove(self.book_positions_file_name)
        expected_book_positions = {"Peter_Pan":{"Chapter":"01-Chapter_1.txt", "Paragraph":3},
                                   "Starship_Troopers":{"Chapter":"01-Chapter_2.txt", "Paragraph":4}}
        self.log_book_position("Peter_Pan", expected_book_positions["Peter_Pan"])
        self.log_book_position("Starship_Troopers", expected_book_positions["Starship_Troopers"])
        actual_book_positions = self.retreive_book_positions()
        assert actual_book_positions == expected_book_positions
        self.remove_book_position("Starship_Troopers")
        del expected_book_positions["Starship_Troopers"]
        actual_book_positions = self.retreive_book_positions()
        assert actual_book_positions == expected_book_positions


