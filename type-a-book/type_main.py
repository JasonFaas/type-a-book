import time


def main():
    print("Hello World!")
    import readchar


# getch = _find_getch()
    what = readchar.readchar()
    print("what")
    print(what)
    print("what")

    print("Type the words below")
    type_string = "The quick brown fox jumps over the lazy dog"

    for type_word in type_string.split(" "):
        print(type_string)
        print(type_word)
        time_start = time.time()
        while input() != type_word:
            print("!Error!")
            print(type_word)
            time_start = time.time()
        else:
            time_stop = time.time()
            time_total = time_stop - time_start
            char_per_sec = (len(type_word) + 1) / time_total
            words_per_sec = char_per_sec / 5
            words_per_min = words_per_sec * 60
            print(words_per_min)
            print(round(words_per_min))

    print("\n\nComplete!")


if __name__ == "__main__":
    main()
