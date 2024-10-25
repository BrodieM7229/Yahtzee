def yahtzee(roll:list) -> int:
    yahtzees = [
        [1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3],
        [4,4,4,4,4],
        [5,5,5,5,5],
        [6,6,6,6,6]
    ]
    if sorted(roll) in yahtzees:
        print("YAHTZEE")
        return 50
    else:
        return 0
