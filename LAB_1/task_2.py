# TODO Найдите количество книг, которое можно разместить на дискете
amount_of_disk = 1.44  # Mb
amount_of_stranis= 100
amount_of_strok = 50
amount_of_simv = 25
one_simv = 4 #b
ves_of_book = one_simv * amount_of_simv * amount_of_strok * amount_of_stranis
amount_of_disk_bytes = amount_of_disk * 1024 * 1024
amount_of_books = int(amount_of_disk_bytes // ves_of_book)
print("Количество книг, помещающихся на дискету:", amount_of_books)
