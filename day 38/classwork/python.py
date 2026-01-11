#Tuple არის მონაცემების კოლექცია, რომელიც მსგავსია list-ის მონაცემების კოლექციის,
# თუმცა list-ის მონაცემების კოლექცია შეიძლება შეიცვალოს, tuple-ის მონაცემები — არა.

names = ("Gio", "Nika", "Luka", "Ana", "Mariam")  #შევქმენით tuples და ჩავწერეთ 5 ელემენტი

result = names[1:-1]  #1 ნიშნავს რომ დაიწყოს მეორე ელემენტიდან, -1 ნიშნავს ბოლო ელემენტის გარეშე

print(result)  #აქ კი ვბეჭდავთ შედეგს


#tuples აქვს 2 მეთოდი როგორც list-ს:

#count ითვლის რამდენჯერ გვხვდება კონკრეტული ელემენტი tuple-ში
#index აბრუნებს ელემენტის index-ს tuple-ში


person = ("Gio", 17)  #შევქმენით tuple სადაც არის 2 ელემენტი და unpacking-ის გამოყენებით ვიღებთ ცალცალკე მონაცემებს.

name, age = person

print(name)
print(age)


colors = ("red", "green", "blue")

a, b, c = colors

print(a)
print(b)
print(c)



x = 5
y = 10

x, y = (y, x)

print(x)
print(y)


data = ("Gio", "Tbilisi", 18, "Student")

name, city, age, status = data

print(name)
print(city)
print(age)
print(status)


numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)
