import time


def wpm_calc(time_start, time_stop, type_word):
    time_total = time_stop - time_start
    char_per_sec = (len(type_word) + 1) / time_total
    words_per_sec = char_per_sec / 5
    words_per_min = words_per_sec * 60
    rounded = round(words_per_min, 2)
    return rounded


def main():
    print("Hello World!")
    import readchar

    print("Type the words below")
    type_string = "The quick brown fox jumps over the lazy dog"

    for idx, type_word in enumerate(type_string.split(" ")):
        input_word = ""
        return_chars = [' ', chr(13)]

        while input_word != type_word:
            input_word = ""
            print(type_string)
            print(type_word)
            time_start = time.time()
            input_char = readchar.readchar()
            while input_char not in return_chars:
                if ord(input_char) == 3:
                    raise Exception("Contrl+C Detected")
                input_word += input_char
                input_char = readchar.readchar()
            else:
                time_stop = time.time()

            if input_word != type_word:
                print("\n!!Wrong Word!!\n")

        print(wpm_calc(time_start, time_stop, type_word))

    print("\n\nComplete!")


if __name__ == "__main__":
    main()
