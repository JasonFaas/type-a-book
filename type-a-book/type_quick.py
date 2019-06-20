from type_exceptions import MisspelledWordException
from type_stuff import TypeStuff
from user_info import UserInfo

class TypeQuick():
    def __init__(self, user_name):
        self.user_info = UserInfo(user_name)
        self.type_stuff = TypeStuff(user_name)

    def short(self):
        self.type_stuff._type_paragraph("The quick and the fast!")

    def long(self):
        self.type_stuff._type_paragraph("The quick brown fox jumps over the lazy dog. " + 
            "No kidding, Lorenzo called off his trip to Mexico City just because they told him the conquistadors were extinct.")

    def print_char_info(self):
        while True:
            single_char = self.type_stuff._get_single_char()
            print("ASCII Value: " + str(ord(single_char)))

    def review_misspelled(self):
        to_review = list(self.user_info.retreive_misspelled_words())
        if len(to_review) == 0:
            print("No words to review. Go Type-A-Book!")
            return
        print("Words to review")
        print(to_review)

        print("\n1st word:")
        self._type_word_5_times(to_review[0])
        
        self.user_info.remove_misspelled_word(to_review[0])


    def review_slowest_word(self):
        averages = self.user_info.retreive_typing_speeds_averages()
        print("Average speeds:" + str(averages))
        slowest_word = min(averages, key=averages.get)
        print("Slowest word:" + slowest_word + " " + str(averages[slowest_word]) + " wpm")

        self._type_word_5_times(slowest_word)

        new_averages = self.user_info.retreive_typing_speeds_averages()
        new_slowest_word = min(new_averages, key=new_averages.get)
        print("New slowest_word word:" + new_slowest_word + " " + str(averages[new_slowest_word]) + " wpm")


    def _type_word_5_times(self, word_to_type):
        print("Type the word 5 times without making a mistake:")
        counter = 0
        words_speeds = {}
        words_speeds[word_to_type] = []
        while counter < 5:
            counter += 1
            print(counter)
            try:
                print("\nType:")
                wpm = self.type_stuff.type_this_word(word_to_type)
                words_speeds[word_to_type].append(wpm)
            except MisspelledWordException as e:
                print("What happened?:" + e.expected_word + ":" + e.actual_word)
                counter = 0
        else:
            self.user_info.log_words_typing_speeds(words_speeds)
