#Tuple არის მონაცემების კოლექცია, რომელიც ერთხელ რომ შექმნი აღარ იცვლება, ხოლო List არის მონაცემების კოლექცია, რომლის შეცვლაც ყოველთვის შეგიძლია.

names = ("Gio", "Nika", "Luka", "Ana", "Mariam") #შევქმენი tuples და გადავეცი 5 ელემენტი

result = names[1:-1]  #1 ნიშნავს რო ვიწყებთ მეორე ელემენტიდან -1 ვჩერდებით ბოლო ელემენტზე 

print(result)  #აქ კი ვპრინტავთ შედეგს



#tuples აქვს 2 მეთოდი რადგან უცვლელია, პირველი არის:

#count ითვლის რამდენჯერ გვხვდება კონკრეტული ელემენტი tuple-ში
#მეორე არის index აბრუნებს რომელ index-ზე დგას ელემენტი.


person = ("Gio", 17)  #შევქმენი tuple სადაც არის 2 ელემენტი და unpacking ით დავშალეთ ცვლადებად და ბოლოს დავპრინტეთ.

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


