#შექმენი სეტი სახელად fruits მასში შეინახეთ შესაბამისი 5 მნიშვნელობა. წაშალეთ ერთი ნებისმიერი ხილი, ჩაამატეთ თქვენი საყვარელი ხილი, შექმენით მეორე სეტი სახელად fruits1 შეინახეთ ორი მნიშვნელობა, ეს ორი სეტი ერთმანეთთან გააერთიანეთ და იპოვეთ ამ ორ სეტს შორის განსხვავება.


fruits = {"apple", "banana", "cherry", "date", "elderberry"}
fruits.remove("banana")
fruits.add("grape")
fruits1 = {"orange", "kiwi"}
all_fruits = fruits.union(fruits1)
difference = fruits.difference(fruits1)


#.uptade()ანახლებს მონაცემს
#.clear() ასეუფთავებს dictionary-ს
#.copy() აკოპირებს







person = {
    "name": "giorgi",
    "last_name": "sichinava",
    "age": 17,
    "favorite_sport": "basketball"
}


print(person.keys())

print(person.values())

print(person.items())

