disk_size = 1.44 * 1024 * 1024 # объем дискеты в байтах
book_pages = 100 # кол-во страниц
page_rows = 50 # строк на странице
row_symbols = 25 # символов на странице
symbol_size = 4 # размер символа

book_size = book_pages * page_rows * row_symbols * symbol_size # объем книги в байтах
capacity = disk_size // book_size

print("Количество книг, помещающихся на дискету:", int(capacity))
