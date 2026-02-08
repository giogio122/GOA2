def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result



def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    



def between(a,b):
    return list(range(a, b + 1))




def double_char(s):
    result = ''
    for char in s:
        result += char * 2
    return result