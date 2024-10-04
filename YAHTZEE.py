def yahtzee(roll:list):
    yahtzees = [
        [1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3],
        [4,4,4,4,4],
        [5,5,5,5,5],
        [6,6,6,6,6]
    ]
    if roll in yahtzees:
        print("YAHTZEE")
        return 50
    else:
        return 0
