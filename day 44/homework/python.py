#1
def odd_or_even(arr):
    total = sum(arr)
    
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
    


#2
def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)


#3
def invert(lst):
    result = []
    for x in lst:
        result.append(-x)
    return result

#4
def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
#5
def no_space(x):
    return x.replace(" ", "")


#6
def repeat_str(repeat, string):
    return string * repeat