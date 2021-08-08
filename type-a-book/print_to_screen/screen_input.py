
class ScreenInput():

    def __init__(self, book_info):
        self.book_info = book_info  # TODO: Delete this if unused

    def book_to_type(self):
        return input("Choose book from above list:").replace(" ", "_")