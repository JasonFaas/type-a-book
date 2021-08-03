import os

class BookInfo():

    def book_list(self):
        folder = "../resources/books/project_gutenberg/"
        subfolders = [f.name for f in os.scandir(folder) if f.is_dir() ]
        return subfolders

    def chapter_list(self, book_name):
        folder = "../resources/books/project_gutenberg/" + book_name + "/chapters/"
        files = []
        if os.path.exists(folder):
            files = [f.name.replace(".txt", "") for f in os.scandir(folder) if (f.is_file() and f.name[0] == '0')]
            files.sort()
        return files

    def chapter_of_book(self, book_name, chapter):
        folder = "../resources/books/project_gutenberg/" + book_name + "/chapters/"
        file = folder + chapter + ".txt"
        with open(file, 'r') as file:
            data = file.read()

        # TODO make this more efficient
        data = data.replace(chr(8220), "\"").replace(chr(8221), "\"")

        return data

    @staticmethod
    def verify_legal_characters(text):
        for char in text:
            if ord(char) > 127:
                print("Bad value {}".format(ord(char)))
                raise AttributeError("Value of {} greater than 126 {}".format(char, ord(char)))
