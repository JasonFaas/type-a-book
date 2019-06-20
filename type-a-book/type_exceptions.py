

class MisspelledWordException(Exception):

    def __init__(self, message, expected_word, actual_word):
        super(MisspelledWordException, self).__init__(message)

        self.expected_word = expected_word
        self.actual_word = actual_word

