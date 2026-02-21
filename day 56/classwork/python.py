def spin_words(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])  # Reverse the word
        else:
            result.append(word)
    return " ".join(result)




def xo(s):
    count_x = 0
    count_o = 0
    for char in s.lower():
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1
    return count_x == count_o






def find_short(s):
    words = s.split()
    l = float('inf') 
    for word in words:
        if len(word) < l:
            l = len(word)
    return l




def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        return sum(range(a, b + 1))
    else:
        return sum(range(b, a + 1))
    


def to_camel_case(text):
    words = text.replace('-', '_').split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])