student = {
    "name": "Giorgi",
    "hobby": "basketball",
    "height": 184,
    "weight": 70
}


name = student.get("name")
print(name)

student.pop("height")

print(student)










def get_keys_and_values(data):
    keys = data.keys()
    values = data.values()
    return keys, values


student = {
    "name": "Giorgi",
    "hobby": "Football",
    "height": 184,
    "weight": 75
}

result = get_keys_and_values(student)
print(result)











# ვქმნით ლექსიკონს person
person = {
    "name": "Giorgi",
    "age": 17,
    "city": "Tbilisi",
    "height": 184
}

# .items() აბრუნებს key და value წყვილებს
for key, value in person.items():
    print(key, ":", value)  # თითოეული key და value იბეჭდება წყვილად
