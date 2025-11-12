# შექმენი ცვლადი სადაც შეინახავ შენს სახელს შემდეგ გადაუარე for ციკლით ცვლადს და გამოიტანე შენი სახელი  ცალ-ცალკე


name = "giorgi"

for i in name:
    print(i)


#შექმენი for ციკლი სადაც გამოიტან კენტ რიცხვებს 1 დან 300 ამდე.

for i in range(1, 301, 2):
    print(i)

# შექმენი for ციკლი სადაც გამოიტან ლუწ რიცხვებს 1 დან 200 ამდე.

for i in range(2, 201, 2):
    print(i)

#გამოიტანე შენი სახელი 20 ჯერ for ციკლის დახმარებით.
for i in range(20):
    print("Giorgi")




#5) შექმენით ცვლადი სახელად correct_password სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს შემოატანინეთ პაროლი, სანამ ეს პაროლი არ იქნება correct_password-ის ტოლი, თავიდან შემოატანინეთ პაროლი.



correct_password = "giogio3212"

password = input("type password ")

while password != correct_password:
    print("incorrect!")
    password = input("type password ")

print("correct")

