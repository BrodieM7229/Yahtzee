dice_1 = 3
dice_2 = 1
dice_3 = 5
dice_4 = 3
dice_5 = 3

numbers = [1, 2, 3, 4, 5]

from collections import Counter

dice_list = [dice_1, dice_2, dice_3, dice_4, dice_5]
count = Counter(dice_list)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 1:
        print(sort_dices[1] * 1)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 2:
        print(sort_dices[2] * 2)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 3:
        print(sort_dices[3] * 3)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 4:
        print(sort_dices[4] * 4)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 5:
        print(sort_dices[5] * 5)

sort_dices = {}
for dice, frequency in count.items():
    sort_dices[dice] = frequency
for k,v in sort_dices.items():
    if k == 6:
        print(sort_dices[6] * 6)