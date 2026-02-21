#)მიმატება: შექმენი lambda ფუნქცია, რომელიც იღებს ერთ რიცხვს და მას 15-ს უმატებს.
add_15 = lambda x: x + 15

print(add_15(5))  


#გამრავლება: შექმენი lambda ფუნქცია, რომელიც იღებს ორ არგუმენტს (x და y) და აბრუნებს მათ ნამრავლს.

multiply = lambda x, y: x * y

print(multiply(3, 4))



#)ტექსტის შებრუნება: დაწერე lambda, რომელიც მიღებულ სტრიქონს (string) უკუღმა დაწერს (მაგალითად: "Python" -> "nohtyP").

reverse = lambda s: s[::-1]

print(reverse("Python"))



#სიტყვების სიგრძე: გაქვს სია: ["apple", "banana", "cherry", "kiwi"]. დაასორტირე ის სიტყვების სიგრძის მიხედვით.

words = ["apple", "banana", "cherry", "kiwi"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)


#Tuples დალაგება: გაქვს პროდუქტების სია ფასებით: [("Milk", 3), ("Bread", 2), ("Cheese", 5)]. დაასორტირე ეს სია ფასის მიხედვით (ზრდადობით).

products = [("Milk", 3), ("Bread", 2), ("Cheese", 5)]

sorted_products = sorted(products, key=lambda x: x[1])

print(sorted_products)


#ახსენი რა არის lambda და რაში გვჭირდება და რითი განსხვავდება ჩვეულებრივი ფუნქციისგან



#lambda არის პატარა ფუნქცია, რომელსაც არ აქვს სახელი anonymous function ერთ ხაზში იწერება ავტომატურად აბრუნებს შედეგს.






