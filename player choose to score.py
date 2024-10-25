results = {}
yahtzee_scoring_options = [
    "Aces (Ones)",
    "Twos",
    "Threes",
    "Fours",
    "Fives",
    "Sixes",
    "Three of a Kind",
    "Four of a Kind",
    "Full House",
    "Small Straight",
    "Large Straight",
    "Yahtzee",
    "Chance"
]

def player_turn(results):
    trial1 = True
    trial2 = True
    while trial1:
        ask = input("(roll/score) Would You like to roll again or score now? ")
        if ask == 'roll':
            """put the rolling again code here"""
            trial1 = False

        elif ask == 'score':
            while trial2:
                print("here are your options:")
                for score in yahtzee_scoring_options:
                    print(f"-{score}")

                question = input("How would you like to score your points")
                if question == "Yahtzee":
                    new_score = yahtzee(dice_list)
                    results[question] = new_score

                    trial1 = False
                    trial2 = False

                elif question in yahtzee_scoring_options:
                    yahtzee_scoring_options.remove(question)
                    if question == "Aces":
                        new_score = sum_1(dice_list)

                    elif question == "Twos":
                        new_score = sum_2(dice_list)

                    elif question == "Threes":
                        new_score = sum_3(dice_list)

                    elif question == "Fours":
                        new_score = sum_4(dice_list)

                    elif question == "Fives":
                        new_score = sum_5(dice_list)

                    elif question == "Sixes":
                        new_score = sum_6(dice_list)

                    elif question == "Three of a Kind":
                        new_score = three_of_kind(dice_list)

                    elif question == "Four of a Kind":
                        new_score = four_of_kind(dice_list)

                    elif question == "Full House":
                        new_score = full_house(dice_list)

                    elif question == "Small Straight":
                        new_score = small_straight(dice_list)

                    elif question == "Large Straight":
                        new_score = large_straight(dice_list)

                    elif question == "Chance":
                        new_score = chance(dice_list)

                    results[question] = new_score

                    trial1 = False
                    trial2 = False

    else:
        print("input either 'roll' or 'score'")
        continue


