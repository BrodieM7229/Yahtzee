def small_straight(roll:list) -> int:
    """
    Identify if a roll of five dice has four dice in order.

    :param roll: The dice that have been rolled.

    :return: Score of your roll.
    """
    small_straights = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
    ]

    # Check if the first (or last) 4 dice match a small straight.
    if (sorted(roll)[:-1] in small_straights or
            sorted(roll)[1:] in small_straights):
        return 30
    else:
        return 0


def large_straight(roll:list) -> int:
    """
    Identify if a roll of five dice has all five dice in order.

    :param roll: The dice that have been rolled.

    :return: Score of your roll.
    """
    straights = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6],
    ]

    # Check if the roll matches a straight variant.
    if sorted(roll) in straights:
        return 40
    else:
        return 0