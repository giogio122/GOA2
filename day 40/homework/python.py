def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count





def filter_list(l):
    return [x for x in l if isinstance(x, int)]





def solution(text, ending):
    return text.endswith(ending)




def century(year):
    return (year + 99) // 100




def friend(x):
    return [name for name in x if len(name) == 4]



def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague