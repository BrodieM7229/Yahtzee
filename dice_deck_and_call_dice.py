import random

def create_dice_face(value):
    faces = {
        1: """
    +-------+
    |       |
    |   ●   |
    |       |
    +-------+
    """,
        2: """
    +-------+
    | ●     |
    |       |
    |     ● |
    +-------+
    """,
        3: """
    +-------+
    | ●     |
    |   ●   |
    |     ● |
    +-------+
    """,
        4: """
    +-------+
    | ●   ● |
    |       |
    | ●   ● |
    +-------+
    """,
        5: """
    +-------+
    | ●   ● |
    |   ●   |
    | ●   ● |
    +-------+
    """,
        6: """
    +-------+
    | ●   ● |
    | ●   ● |
    | ●   ● |
    +-------+
    """
    }
    return faces[value]

def roll_dice():
    value = random.randint(1, 6)  # Generate a random number between 1 and 6
    return create_dice_face(value)  # Call the function to get the dice face

print("Rolling the dice.....")
print(roll_dice())