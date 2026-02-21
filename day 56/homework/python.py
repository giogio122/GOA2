
def solution(s):
    result = ""

    for ch in s:
        if ch.isupper():
            result += " " + ch
        else:
            result += ch

    return result




def array_diff(a, b):
    return [x for x in a if x not in b]





def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"
    




def filter_list(l):
    return [x for x in l if type(x) == int]





def is_square(n):    
    if n < 0:
        return False
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n







def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 == 1:
            return num
        



    
def string_transformer(s):
    return " ".join(s.swapcase().split()[::-1])