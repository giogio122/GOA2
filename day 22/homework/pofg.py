#ომენტარებით ახსენით რას აკეთებს len ფუნქცია. და მოიყვანეთ მაგალითი.

#len ითვლის რაოდენობას და აბრუნებს რიცხვს.

#name = ["Giorgi, "Nika, "Saba"]
#print(len(names))   



my_list = [10, "Giorgi", True, 5.5, "Red", 99]

my_list[4] = "Sichinava"

print(my_list)



friends = ["nika", "aleqsi", "zura", "gabrieli"]

friends[1] = 7   
friends[3] = 17  

print(friends)





numbers = list(range(1, 21))

for i in range(len(numbers)):
    if i % 2 == 0:  
        print(numbers[i])

