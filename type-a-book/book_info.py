import os
from glob import glob

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

        return data


    def unit_tests(self):
        assert self.book_list() == ['Peter_Pan']

        assert self.chapter_list("Peter_Pan") == ["00A-Intro",
                                                  "01-Chapter_1",
                                                  "02-Chapter_2",
                                                  "03-Chapter_3"]