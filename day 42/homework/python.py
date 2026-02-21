
freands_goa = {"nika", "gega", "giorgi", "sandro", "saba"}


freands = {"Nika", "Gurami", "Gabreili", "Andria", "Jaba"}


all_freands = list(freands_goa) + list(freands)


difference_goa = [f for f in freands_goa if f not in freands]
difference_before = [f for f in freands if f not in freands_goa]


print("გოაში გაცნობილი მეგობრები:", freands_goa)
print("გოამდე გაცნობილი მეგობრები:", freands)
print("ყველა მეგობარი ერთად:", all_freands)
print("გოაში გაცნობილი, მაგრამ ადრე არა:", difference_goa)
print("ადრე გაცნობილი, მაგრამ გოაში არა:", difference_before)





cars = {"BMW X5", "Audi A6", "Mercedes C-Class", "Toyota Camry", "Honda Civic"}


cars.remove("Toyota Camry")  


cars.add("Lamborghini Aventador")

print(cars)





person = {
    "Name": "Giorgi",
    "გვარი": "Sichinava",
    "Best_Car": "Lamborghini Aventador",
    "best programing academy": "GOAacademy"
}


print(person["Best_Car"])



