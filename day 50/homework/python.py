nums = [10, 20, 30, 40]

try:
    i = int(input("შეიყვანე ინდექსი: "))
    print(nums[i])
except IndexError:
    print("ასეთი ინდექსი არ არსებობს")








prices = {"apple": 2, "banana": 3}

try:
    product = input("შეიყვანე პროდუქტი: ")
    print(prices[product])
except KeyError:
    print("ასეთი პროდუქტი ვერ მოიძებნა")




try:
    x = input("შეიყვანე x: ")
    y = input("შეიყვანე y: ")

    x = int(x)
    y = int(y)

    print(x + y)
except ValueError:
    print("მხოლოდ რიცხვები შეიყვანე")
