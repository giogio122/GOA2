#.append() სიის ბოლოში ამატებს ერთ ელემენტს.

nums = [1, 2, 3]
nums.append(4)
print(nums)



names = ["gio", "dato"]
names.append("nika")
print(names)



# clear () სიის ყველა ელემენტს შლის და ცარიელს ტოვებს.

nums = [1, 2, 3]
nums.clear()
print(nums)



words = ["a", "b", "c"]
words.clear()
print(words)






# copy() სიას აკოპირებს ახალ სიას ქმნის.

a = [1, 2, 3]
b = a.copy()
print(b)



names = ["gio", "dato"]
new_names = names.copy()
print(new_names)







# count ითვლის რამდენჯერ გვხვდება ელემენტი სიაში.

nums = [1, 2, 2, 3]
print(nums.count(2))


letters = ["a", "b", "a"]
print(letters.count("a"))





# extend() ერთ სიას ამატებს მეორე სიის ელემენტებს.

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)



names = ["gio"]
names.extend(["dato", "nika"])
print(names)




