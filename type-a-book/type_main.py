import readchar

from type_quick import TypeQuick
from type_stuff import TypeStuff
from user_info import UserInfo
from book_info.book_info import BookInfo
from api_request import ApiRequest
from tests.test_book_info import TestBookInfo
import tests.test_book_info

from unittest import TestCase
import unittest



def main():
    user_name = input("Welcome to Type-A-Book.\nPlease type your name:")
    user_name.replace(" ", "_")

    while True:
        introduction = ("Typing proram - Select:" +
                        "\n\tMenu:" +
                        "\n\t\t1: Start typing - 6 words" +
                        "\n\t\t2: Start typing - 2 sentences" +
                        "\n\t\t3: Value of each character" +
                        "\n\n\t\tA: Type A Book" +
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

        try:
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
                except GeneratorExit as e:
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
            elif input_char == 'q' or input_char == chr(3):
                print("Exiting!")
                exit()
            else:
                print("Invalid input")
        except KeyboardInterrupt as e:
            print("\nReturn to main menu")


if __name__ == "__main__":
    TypeStuff("Unit_Tests").unit_tests()
    UserInfo("Unit_Tests").unit_tests()

    suite = unittest.TestLoader().loadTestsFromModule(tests.test_book_info)
    run = unittest.TextTestRunner(verbosity=2).run(suite)
    assert len(run.failures) == 0, run.failures
    assert len(run.errors) == 0, run.errors



    ApiRequest().unit_tests()
    main()
