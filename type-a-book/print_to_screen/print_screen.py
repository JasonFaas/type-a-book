
class PrintScreen():

    def __init__(self, book_info):
        self.book_info = book_info

    def book_list(self):
        print("Books:")
        print("\t" + "\n\t".join(self.book_info.book_list()).replace("_", " "))

    def chapter_list(self, book_chapters):
        print("\nChapters")
        for chapter in book_chapters:
            print("\t" + chapter)
