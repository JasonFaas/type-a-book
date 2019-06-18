import time
import pprint
import readchar

from type_quick import TypeQuick
from user_info import UserInfo


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
                        "\n\t\tB: Review misspelled words - TODO: Implemente!" +
                        "\n\t\tC: Improve slower words - TODO: Implemente!" +
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
            start_typing.single_char()
        elif input_char == 'b':
            print("Reviewing misspelled words!")
            start_typing.review_misspelled()
            exit()
        elif input_char == 'q':
            print("Exiting!")
            exit()
        else:
            print("Invalid input")



if __name__ == "__main__":
    UserInfo("Unit_Tests").unit_tests()
    main()
