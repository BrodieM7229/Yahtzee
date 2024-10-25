from collections import Counter
from random import randint

def roll_dice(dice:int=5, dice_list:list=None) -> list:
    """
    Roll a given number of dice and append them to a list of dice that have
    already been rolled (ie, re-rolling dice for Yahtzee).

    :param dice: Number of dice to roll.
    :param dice_list: Dice that have already been rolled.

    :return: List of pre-rolled dice and new dice.
    """
    if not dice_list:
        dice_list = []
    for i in range(dice):
        dice_list.append(randint(1,6))
    return dice_list

def full_house(dice_list):
    count = Counter(dice_list)

    sort_dice = {}
    for dice, frequency in count.items():
        sort_dice[dice] = frequency

    print(sort_dice)

    value_2 = 2
    value_3 = 3

    if value_2 in sort_dice.values():
        if value_3 in sort_dice.values():
            fullhouse = True
        else:
            fullhouse = False
    else:
        fullhouse = False

    if fullhouse == True:
        return "You earned 25 points"
    else:
        return "You can't do a full house"

def chance(dice_list: list):
    return sum(dice_list)

def three_of_kind(dice_list: list):
    if dice_list.count(6) >= 3:
        return 18
    if dice_list.count(5) >= 3:
        return 15
    if dice_list.count(4) >= 3:
        return 12
    if dice_list.count(3) >= 3:
        return 9
    if dice_list.count(2) >= 3:
        return 6
    if dice_list.count(1) >= 3:
        return 3
    return 0

def four_of_kind(dice_list: list):
    if dice_list.count(6) >= 4:
        return 24
    if dice_list.count(5) >= 4:
        return 20
    if dice_list.count(4) >= 4:
        return 16
    if dice_list.count(3) >= 4:
        return 12
    if dice_list.count(2) >= 4:
        return 8
    if dice_list.count(1) >= 4:
        return 4
    return 0




def sum_1(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 1:
            return print(sort_dices[1] * 1)

def sum_2(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 2:
            return print(sort_dices[2] * 2)

def sum_3(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 3:
            return print(sort_dices[3] * 3)

def sum_4(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 4:
            return print(sort_dices[4] * 4)

def sum_5(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 5:
            return print(sort_dices[5] * 5)

def sum_6(dice_list):
    count = Counter(dice_list)
    sort_dices = {}
    for dice, frequency in count.items():
        sort_dices[dice] = frequency

    for k,v in sort_dices.items():
        if k == 6:
            return print(sort_dices[6] * 6)

def yahtzee(dice_list: list) -> int:
    yahtzees = [
        [1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3],
        [4,4,4,4,4],
        [5,5,5,5,5],
        [6,6,6,6,6]
    ]
    if sorted(dice_list) in yahtzees:
        if roll.count(1) == 6:
            print("YAHTZEE")
            return 50
        if dice_list.count(2) == 6:
            print("YAHTZEE")
            return 100
        return 0