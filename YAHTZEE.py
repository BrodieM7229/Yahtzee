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
        if roll.count(1) >= 6:
            print("YAHTZEE")
            return 50
        if roll.count(2) >= 6:
            print("YAHTZEE")
            return 100
        return 0
        
