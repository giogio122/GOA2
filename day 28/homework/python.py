def add_five(num):
    total = num + 5
    return num




def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    if operator == '-':
        return value1 - value2
    if operator == '*':
        return value1 * value2
    if operator == '/':
        result = value1 / value2
        return int(result) if result.is_integer() else result
    



 def repeat_str(repeat, string):
 return string * repeat




def remove_char(s):
    return s[1:-1]



def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)









def make_negative(number):
    if number > 0:
        return -number
    else:
        return number
    







def bool_to_word(boolean):
    if boolean == True :
        return "Yes"
    else:
        return "No"





def multiply(a, b):
    return a * b