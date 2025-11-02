
#1) მომხმარებელმა უნდა შეიყვანოს ორი რიცხვი.
#პროგრამამ უნდა დაბეჭდოს შედეგი — True, თუ ორივე დადებითია, ხოლო თუ ერთი მაინც არასწორი იქნება False.

#2) შექმენი ორი ცვლადი ერთი email მეორე password ამ ორივე ცვლადს მიანიჭეთ შესაბამისი მნიშვნელობა. შემდეგ მომხმარებელს შემოატანინე ემაილი და პაროლი. საბოლოოდ დაბეჭდე თუ შენი ემაილი უდრის მომხმარებლის შემოყვანილ ემაილს და შენი პაროლი თუ უდრის მომხმარებლის შემოყვანილ პაროლს.

#3) print(12==13 or 12==12 and 21>20) კომენტარებით მიუწერე რა იქნება შედეგი და თან ახსენი რატომ. არ ნახო შედეგი!


num1 = int(input("type number: "))
num2 = int(input("type number: "))

result = num1 > 0 and num2 > 0

print(result)



email = "giorgi@gmail.com"
password = "12345678"

user_email = input("type your email:")
user_password = input("type your password: ")


print(user_email == user_password)




print(12==13 or 12==12 and 21>20) #კომენტარებით მიუწერე რა იქნება შედეგი და თან ახსენი რატომ. არ ნახო შედეგი! 

#12==13 false რადგან 12 არ უდრის 13 ს.
#12==12 true რადგან უდრის 12 ი 12 ს.
#21>20 true რადგან 21 მეტია 20ზე 

# true and true = true



age = int(input("type your age"))

is_adult = age >= 18

print(is_adult)




role = input("type your role: (admin, moderator, user): ")

print(role == "admin")


#გვაქვს >= <= == > < != 











