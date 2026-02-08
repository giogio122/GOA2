def unusual_five():
    return len("hello")



#



def reverse_seq(n):
    return list(range(n, 0, -1))



#



def array_diff(a, b):
    return [x for x in a if x not in b]



#



def no_space(x):
    return x.replace(" ", "")



#


def reverse_words(s):
    return " ".join(s.split()[::-1])
