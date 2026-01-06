#პარამეტრი არის პარამეტრი არის ცვლადი, რომელსაც ვწერთ ფუნქციის განსაზღვრისას და ის გამოიყენება ფუნქციის შიგნით მონაცემის მისაღებად.~



def sum_numbers(a, b):
    return a + b


result = sum_numbers(5, 7)
print(result)   # 12





def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")






#რა არის ამ კოდში ერორი არ შეამოწმოთ თქვენით იფიქრეთ:
def hello(name):
    print("gamarjoba",name)
hello("nika","saba")


#აქ ერორი ისააა რომ ფუნქცია მხოლოდ ერთ სახელს იღებს და გამოძახებისას 2 გამოვიძახეთ და გამოვა error..