def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2

##


def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    
##

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

##



def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)




##


def reverse_seq(n):
    return list(range(n, 0, -1))