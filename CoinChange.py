"""Old school cash ergister software. Find how many coins you can get back for change

e.g. : 33 -> 1 quarter(25), 1 nickel(5), 3 pennies(1) [dime 10]

"""
import sys


def num_coins(cents):
    if cents < 1:
        return 0

    coins = [25,10,5,1]
    coin_number = 0
    for coin in coins:
        coin_number += int(cents/coin)
        cents %= coin
        if cents == 0:
            break

    return coin_number

if __name__ == '__main__':
    print(num_coins(cents=int(sys.argv[1])))
