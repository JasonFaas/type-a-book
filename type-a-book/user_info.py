import os

class UserInfo():
    def __init__(self, user_name):
        self.user_name = user_name
        self.misspelled_file_name = "../resources/user-info/" + self.user_name + "-misspelled-words.txt"
        self._unit_tests()

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

    def _unit_tests(self):
        if os.path.exists(self.misspelled_file_name):
            os.remove(self.misspelled_file_name)
        self.log_misspelled_words({"what", "that"})
        misspelled_words = self.retreive_misspelled_words()
        if misspelled_words != {'what', 'that'}:
            raise Exception("Failure:" + str(misspelled_words) + ":")
