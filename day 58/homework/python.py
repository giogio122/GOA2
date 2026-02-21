nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, nums))

print(doubled)




words = ["apple", "banana", "cherry"]

capitalized = list(map(lambda w: w.capitalize(), words))

print(capitalized)




nums = [10, 20, 30, 40]

increased = list(map(lambda x: x + 5, nums))


filtered = list(filter(lambda x: x > 30, increased))

print(increased)
print(filtered)






words = ["cat", "dog", "elephant", "ant"]

result = list(filter(lambda w: len(w) <= 3, words))

print(result)




nums = [2, 3, 4, 5, 6]

even_nums = list(filter(lambda x: x % 2 == 0, nums))

print(even_nums)