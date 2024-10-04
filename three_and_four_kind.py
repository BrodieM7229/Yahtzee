def three_of_kind(roll:list):
    if roll.count(6) >= 3:
        return 18
    if roll.count(5) >= 3:
        return 15
    if roll.count(4) >= 3:
        return 12
    if roll.count(3) >= 3:
        return 9
    if roll.count(2) >= 3:
        return 6
    if roll.count(1) >= 3:
        return 3
    return 0

def four_of_kind(roll:list):
    if roll.count(6) >= 4:
        return 24
    if roll.count(5) >= 4:
        return 20
    if roll.count(4) >= 4:
        return 16
    if roll.count(3) >= 4:
        return 12
    if roll.count(2) >= 4:
        return 8
    if roll.count(1) >= 4:
        return 4
    return 0

