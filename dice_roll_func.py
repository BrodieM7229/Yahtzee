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