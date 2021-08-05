import os
import roman

class BookInfo():

    def book_list(self):
        folder = self.path_for_books()
        subfolders = [f.name for f in os.scandir(folder) if f.is_dir() ]
        return subfolders


    def array_first_instance(self, array_to_search, search_for, start_idx):
        return_idx = start_idx
        while not array_to_search[return_idx] == search_for:
            return_idx += 1

        assert return_idx < len(array_to_search) - 2, "Invalid search {}".format(search_for)

        return return_idx


    def chapter_list_new(self, book_name):
        book_by_line = self.contents_of_book_array(book_name)

        contents_line_idx = self.array_first_instance(array_to_search=book_by_line, search_for="Contents", start_idx=0)
        last_chapter_idx = self.array_first_instance(array_to_search=book_by_line, search_for="", start_idx=contents_line_idx + 2)

        chapters_unformatted = book_by_line[contents_line_idx + 2:last_chapter_idx]

        for idx in range(len(chapters_unformatted)):
            chapters_unformatted[idx] = chapters_unformatted[idx][1:]

        return chapters_unformatted

    def contents_of_book_array(self, book_name):
        book_file_name = self.book_file_name(book_name)
        with open("{}/{}".format(self.path_for_book(book_name), book_file_name), 'r') as file:
            data = file.read()
        book_by_line = data.split('\n')
        return book_by_line

    def paragraph_of_book_new(self, book_name, chapter_name, paragraph):
        book_by_line = self.contents_of_book_array(book_name)
        # chapter_list = self.chapter_list_new(book_name)

        current_chapter_line_in_book = "{}.".format((chapter_name.split(".")[0]).strip())
        chapter_start_line = self.array_first_instance(
            array_to_search=book_by_line,
            search_for=current_chapter_line_in_book,
            start_idx=0
        )

        chapter_after_start_line = self.array_first_instance(
            array_to_search=book_by_line,
            search_for=self.next_chapter_line_in_book(current_chapter_line_in_book),
            start_idx=chapter_start_line + 1
        ) - 1
        # TODO: If last chapter, looking for "THE END"


        if paragraph == 1:
            return "{} {}".format(book_by_line[chapter_start_line], book_by_line[chapter_start_line+1])
        else:
            # TODO: Join all lines from starting line to end line, no new line separator needed.
            # THEN: Separate again based on newline.
            # THEN: Return separated_var[paragraph+2]
            # THEN: Figure out what the right magic number is
            # THEN: Write another test with another paragraph number
            pass



        return book_by_line[chapter_start_line + paragraph]


    def book_file_name(self, book_name):
        folder = "../resources/books/project_gutenberg/{}".format(book_name)
        files = [f.name for f in os.scandir(folder) if f.is_file() and f.name[0].isdigit()]
        return files[0]

    def chapter_list(self, book_name):
        folder = self.path_for_book(book_name) + "/chapters/"
        files = []
        if os.path.exists(folder):
            files = [f.name.replace(".txt", "") for f in os.scandir(folder) if (f.is_file() and f.name[0] == '0')]
            files.sort()
        return files

    def chapter_of_book(self, book_name, chapter):
        folder = self.path_for_book(book_name) + "/chapters/"
        file = folder + chapter + ".txt"
        with open(file, 'r') as file:
            data = file.read()

        # TODO make this more efficient
        data = data.replace(chr(8220), "\"").replace(chr(8221), "\"")

        return data

    def path_for_book(self, book_name):
        return self.path_for_books() + book_name

    def path_for_books(self):
        return "../resources/books/project_gutenberg/"

    @staticmethod
    def verify_legal_characters(text):
        for char in text:
            if ord(char) > 127:
                print("Bad value {}".format(ord(char)))
                raise AttributeError("Value of {} greater than 126 {}".format(char, ord(char)))

    def next_chapter_line_in_book(self, current_chapter_line_in_book):
        current_roman = current_chapter_line_in_book[len('Chapter '):-1]
        return 'Chapter {}.'.format(roman.toRoman(roman.fromRoman(current_roman)+1))
        return current_roman

