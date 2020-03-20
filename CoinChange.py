"""Old school cash ergister software. Find how many coins you can get back for change

e.g. : 33 -> 1 quarter(25), 1 nickel(5), 3 pennies(1) [dime 10]

"""
import sys


def num_coins(cents):
    if cents < 1:
        return 0

    coins = [25,10,1]
    coin_number = 0
    for coin in coins:
        coin_number += int(cents/coin)
        cents %= coin
        if cents == 0:
            break

    return coin_number


def min_coins(cents):
    if cents < 1:
        return 0
    # get the answer for the min coins when you have no nickels
    coins = [25,10,1]
    coin_number = 0

    mod_25 = cents % 25
    mod_10 = cents % 10

    if mod_25 >= 10:
        coin_number += int(cents / 10)
        coin_number += mod_10
    else:
        coin_number += int(cents / 25)
        coin_number += mod_25

    return coin_number


if __name__ == '__main__':
    greedy = num_coins(cents=int(sys.argv[1]))
    mini = min_coins(cents=int(sys.argv[1]))
    print('greedy=', greedy, 'and mini =', mini)

