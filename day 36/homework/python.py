
#1
def count_positives_sum_negatives(arr):
    if not arr:
        return []
    
    count_pos = 0
    sum_neg = 0
    
    for x in arr:
        if x > 0:
            count_pos += 1
        elif x < 0:
            sum_neg += x
    
    return [count_pos, sum_neg]


#2
def opposite(number):
    return -number

#3
def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total

#4
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
    


#5
def greet():
    return "hello world!"


#6
def repeat_str(repeat, string):
    return string * repeat


#7
def string_to_number(s):
    return int(s)

#8
def remove_char(s):
    return s[1:-1]


#9
def sum_array(arr):
    if not arr or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)



#10
def make_negative(number):
    if number > 0:
        return -number
    else:
        return number
    

#11
def solution(string):
    return string[::-1]

#12
def number_to_string(num):
    return str(num)

#13
def even_or_odd(number):
    if number % 2 == 0 :
        return "Even"
    else:
        return "Odd"
    

#14
def bool_to_word(boolean):
    if boolean == True :
        return "Yes"
    else:
        return "No"

#15
def multiply(a, b):
    return a * b


#16
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


#17
def century(year):
    return (year + 99) // 100


#18
def solution(text, ending):
       return text.endswith(ending)

#19
def filter_list(l):
    return [x for x in l if isinstance(x, int)]


#20
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count
