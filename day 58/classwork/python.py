names = ["Giorgi", "Nika", "Luka", "Ana"]

last_name = "Sichinava"

full_names = list(map(lambda name: name + " " + last_name, names))

print(full_names)







numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = list(map(lambda x: x if x % 2 == 0 else None, numbers))

even_num = list(filter(lambda x: x is not None, even_num))

print(even_num)
