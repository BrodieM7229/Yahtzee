def create_dice_face(value):
    faces = {
        1: [
            "+-------+",
            "|       |",
            "|   ●   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "| ●     |",
            "|       |",
            "|     ● |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| ●     |",
            "|   ●   |",
            "|     ● |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| ●   ● |",
            "|       |",
            "| ●   ● |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| ●   ● |",
            "|   ●   |",
            "| ●   ● |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| ●   ● |",
            "| ●   ● |",
            "| ●   ● |",
            "+-------+"
        ]
    }
    return faces[value]  # Return the face as a list of strings


# Display all dice faces
def display_all_dice_faces():
    # Prepare to collect the lines for each dice face
    top = []
    middle1 = []
    middle2 = []
    middle3 = []
    bottom = []

    for value in range(1, 7):
        face = create_dice_face(value)  # Get lines for the die face
        top.append(face[0])  # Top line of the dice face
        middle1.append(face[1])  # First middle line of the dice face
        middle2.append(face[2])  # Second middle line of the dice face
        middle3.append(face[3])  # Third middle line of the dice face
        bottom.append(face[4])  # Bottom line of the dice face

    # Print all lines together, ensuring alignment
    print("  ".join(top))
    print("  ".join(middle1))
    print("  ".join(middle2))
    print("  ".join(middle3))
    print("  ".join(bottom))


# Run the function to display all dice faces
display_all_dice_faces()

