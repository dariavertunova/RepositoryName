pages = 100
rows_per_page = 50
characters_per_row = 25
bytes_per_character = 4

page_size = rows_per_page * characters_per_row * bytes_per_character
book_size = pages * page_size

diskette_size = 1.44 * 1024 * 1024

number_of_books = diskette_size // book_size

print("Количество книг, помещающихся на дискету:", int(number_of_books))