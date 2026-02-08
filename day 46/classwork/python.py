numbers = [3, 5, 10, 15, 20, 30, 33, 45, 50]
result = [x for x in numbers if x % 3 == 0 and x % 5 == 0]



#შექმენით სია სადაც გექნებათ მოცემული სახელები, შემდეგ ახალ სიაში ჩაამატეთ ისეთი სახელები სახელები რომლის სიმბოლოების რაოდენობაც არის ლუწი რიცხვი

names = ["Giorgi", "Nika", "Ana", "Luka", "Sandro", "saba"]
result = [name for name in names if len(name) % 2 == 0]




#list comprehension არის მოკლე გზა ახალი სიის შესაქმნელად ძველი სიიდან



