#index error ჩნდება მაშინ როდესაც სიის ელემენტში იძახებ ისეთ ელემენტს რომელიც არ არსებობს.


#value error როდესაც მნიშველობა არასწორადაა გადაცემული.


#type error როცა არასწორი ტიპის მონაცემებს შორის ოპერაციას ვაკეტებთ.



#key error vროცა dictionary-ში ისეთ key-ს ითხოვ, რომელიც არ არსებობს

#ZeroDivisionError არის შეცდომა, რომელიც ხდება მაშინ, როცა ცდილობ რიცხვი ნულზე გაყო.




a = 5
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Division by zero is not allowed!")



