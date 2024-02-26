import csv

class Library:

        def __init__(self, book_library, book_shelf, book_title, book_author, book_description, book_type, book_year):
                self.library = book_library
                self.shelf = book_shelf
                self.title_book = book_title
                self.author_book = book_author
                self.description_book = book_description
                self.type_book = book_type
                self.year_book = book_year
        
# library_name = [book_library,[book_shelf]]
library_name = [["central_library",["cl-1","cl-2","cl-3","cl-4","cl-5","cl-6"]],
                 ["north_library",["nl-1","nl-2","nl-3","nl-4","nl-5"]] ,
                 ["school_library",["sl-1", "sl-2", "sl-3"]]]





