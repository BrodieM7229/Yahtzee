DiceList = [1,2,3,4,5]

while True:
    user_input = input("Would you like to roll again? Y/N:")
    if user_input.upper() == 'Y':
        NumberOfDice = int(input("how many dice would you like to re-roll?: "))
        reroll_dice = []
        for i in range(NumberOfDice):
         removed_dice = int(input("which die would you like to re-roll?: "))
         reroll_dice.append(removed_dice)
        print(reroll_dice)
        break
    else:
        break
