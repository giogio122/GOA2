word = input("type any word: ")


print(word.lower())


print(word.upper())


print(word.capitalize())






sentence1 = input("type any proposal: ")
sentence2 = input("type any proposal: ")
sentence3 = input("type any proposal: ")

#  პირველი წინადადება — lower()
print(sentence1.lower())

# მეორე წინადადება — upper()
print(sentence2.upper())

#  მესამე წინადადება — capitalize()
print(sentence3.capitalize())







my_name = "giorgi"


user_name = input("type your name: ")


if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")








sentence = "gAmArJoBa me var GiorgI"


result = sentence.capitalize()

print(result)





text = "Hello World"

index = text.find("o")

print(index)





words = ["hello", "world", "python", "goa"]

for word in words:
    print(word.upper())
