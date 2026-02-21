square = lambda x: x ** 2

print(square(5))  



##


multiply = lambda x, y: x * y

print(multiply(3, 4))


##


c_to_f = lambda c: c * 1.8 + 32

print(c_to_f(0))   # 32.0
print(c_to_f(25))  # 77.0

##

is_even = lambda x: x % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False



##



length = lambda text: len(text)

print(length("Python"))  


##


names = ["დათო", "ეკა", "ალექსანდრე", "გია"]

sorted_names = sorted(names, key=lambda x: len(x))

print(sorted_names)




##

points = [(1, 5), (8, 2), (4, 10)]

sorted_points = sorted(points, key=lambda x: x[1])

print(sorted_points)



##



products = [
    {"name": "პური", "price": 1.2},
    {"name": "რძე", "price": 4.5},
    {"name": "ყველი", "price": 12.0}
]

sorted_products = sorted(products, key=lambda x: x["price"])

print(sorted_products)






##




words = ["banana", "Apple", "cherry", "Berry"]

sorted_words = sorted(words, key=lambda x: x.lower())

print(sorted_words)




##



check_age = lambda age: "Adult" if age >= 18 else "Minor"

print(check_age(20))  

print(check_age(15))  




##




check_number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(check_number(5))   # Positive
print(check_number(-3))  # Negative
print(check_number(0))   # Zero


