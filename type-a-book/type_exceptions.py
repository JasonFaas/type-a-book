

class MisspelledWordException(Exception):

    def __init__(self, expected_word, actual_word):
        super(MisspelledWordException, self).__init__("Typed " + actual_word + " instead of " + expected_word)

        self.expected_word = expected_word
        self.actual_word = actual_word

