"""The goal here is to return the first recurring character from the string
'ABCA' -> return 'A'
'BCABA' -> 'B'
'ABC' -> null or None

"""
import sys


def recur_charac_set(string):
    count = set()
    for s in string:
        if s in count:
            #print(s)
            return s
        else:
            count.add(s)
    return None

def recur_charac_dict(string):
    count = {}
    for s in string:
        if s in count:
            #count[s] += 1
            return s
        else:
            count[s] = 1
    return None

if __name__ == '__main__':
    print(recur_charac_dict(string=sys.argv[1]))