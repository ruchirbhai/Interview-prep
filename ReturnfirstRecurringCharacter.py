"""The goal here is to return the first recurring character from the string
'ABCA' -> return 'A'
'BCABA' -> 'B'
'ABC' -> null or None

"""
import sys


def recur_charac(string):
    count = set()
    for s in string:
        if s in count:
            #print(s)
            return s
        else:
            count.add(s)

if __name__ == '__main__':
    recur_charac(string=sys.argv[1])