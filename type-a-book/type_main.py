import time
import pprint
import readchar

from type_quick import TypeQuick
from user_info import UserInfo
from book_info import BookInfo


def main():
    user_name = input("Welcome to Type-A-Book.\nPlease type your name:")
    user_name.replace(" ", "_")

    while True:
        introduction = ("Typing proram - Select:" +
                        "\n\tMenu:" +
                        "\n\t\t1: Start typing - 6 words" +
                        "\n\t\t2: Start typing - 2 sentences" +
                        "\n\t\t3: Value of each character" +
                        "\n\t\tA: Type A Book - TODO: Implemente!" +
                        "\n\t\tB: Review misspelled words" +
                        "\n\t\tC: Improve slower words" +
                        "\n\t\tD: Learn recent word - TODO: Implemente!" +
                        "\n\t\tQ: Exit Program" +
                        "\n\tHotkeys during Typing:"
                        "\n\t\tCtrl+C: Exit Program" +
                        "\n\t\tCtrl+Q: Main Menu - TODO: Implemente!" +
                        "\n\t\tCtrl+W: Look up definition for recent word - TODO: Implemente!")

        print(introduction)
        print("\n")

        input_char = readchar.readchar().lower()
        start_typing = TypeQuick(user_name)

        if input_char == '1':
            print("Quick Type!")
            start_typing.short()
        elif input_char == '2':
            print("Long Type!")
            start_typing.long()
        elif input_char == '3':
            print("Character Interogate!")
            try:
                start_typing.print_char_info()
            except Exception as e:
                print("Threw established excpetion:\n\t" + str(e))
        elif input_char == 'a':
            print("Type-A-Book!")
            start_typing.type_a_book()
        elif input_char == 'b':
            print("Reviewing misspelled words!")
            start_typing.review_misspelled()
        elif input_char == 'c':
            print("Improve slower words!")
            start_typing.review_slowest_word()
        elif input_char == 'd':
            print("Should write learn new words!")
            print("Look through slow or less than 5 entries or just recent words!")
        elif input_char == 'q':
            print("Exiting!")
            exit()
        else:
            print("Invalid input")



if __name__ == "__main__":
    UserInfo("Unit_Tests").unit_tests()
    BookInfo().unit_tests()
    main()
