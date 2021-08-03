import os

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
        chapter_list = self.chapter_list_new(book_name)
        pass
        # for



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

