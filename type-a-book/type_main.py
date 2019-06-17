import time
import pprint
import readchar

from type_quick import TypeQuick




def main():
    introduction = ("Typing proram - Select:" +
                    "\n\tMenu:" +
                    "\n\t\t1: Start typing - 6 words" +
                    "\n\t\t2: Start typing - 2 sentences" +
                    "\n\t\t3: Value of each character" +
                    "\n\t\tA: Choose book" +
                    "\n\t\tB: Study recently misspelled words" +
                    "\n\t\tC: Study slower typed words" +
                    "\n\t\tQ: Exit Program" +
                    "\n\tHotkeys during Typing:"
                    "\n\t\tCtrl+C: Exit Program" +
                    "\n\t\tCtrl+Q: Main Menu" +
                    "\n\t\tCtrl+W: Look up definition for recent word")

    print(introduction)
    print("\n")

    input_char = readchar.readchar().lower()
    start_typing = TypeQuick()

    if input_char == '1':
        print("Quick Type!")
        start_typing.short()
        exit()
    elif input_char == '2':
        print("Long Type!")
        start_typing.long()
        exit()
    elif input_char == '3':
        print("Character Interogate!")
        start_typing.single_char()
        exit()
    elif input_char == 'q':
        print("Exiting!")


if __name__ == "__main__":
    main()
