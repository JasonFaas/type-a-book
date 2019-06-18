import os

class UserInfo():
    def __init__(self, user_name):
        self.user_name = user_name.replace(" ", "_")
        self.misspelled_file_name = "../resources/user-info/" + self.user_name + "-words-misspelled.txt"
        self.words_speeds_file_name = "../resources/user-info/" + self.user_name + "-words-typing-speed.txt"

    def log_misspelled_words(self, word_list):
        f = open(self.misspelled_file_name, 'a')
        for word in word_list:
            f.write(word + "\n")
        f.close()

    def retreive_misspelled_words(self):
        f = open(self.misspelled_file_name, "r")
        word_list = set()
        for line in f:
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
            current_speeds[word] = current_speeds[word][-5:]


        f = open(self.words_speeds_file_name, 'w')
        for word, speeds in current_speeds.items():
            f.write(str(word) + ":" + str(speeds) + "\n")
        f.close()


    def retreive_typing_speeds(self):
        if not os.path.exists(self.words_speeds_file_name):
            return {}
        f = open(self.words_speeds_file_name, 'r')
        speed_info = {}
        for line in f:
            word, speeds = line.split(":")
            speed_list = speeds[1:-2].split(",")
            speed_info[word] = []
            for speed_str in speed_list:
                speed_info[word].append(float(speed_str))
        f.close()
        return speed_info


    def unit_tests(self):
        # misspelled words
        if os.path.exists(self.misspelled_file_name):
            os.remove(self.misspelled_file_name)
        self.log_misspelled_words({"what", "that"})
        misspelled_words = self.retreive_misspelled_words()
        if misspelled_words != {'what', 'that'}:
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
        



