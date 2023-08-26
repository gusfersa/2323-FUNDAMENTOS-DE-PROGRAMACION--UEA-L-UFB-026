import random

# Create a 4x4 matrix with hidden values
rows = 4
cols = 4
matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
revealed_matrix = [[' ' for _ in range(cols)] for _ in range(rows)]

# Game loop
while True:
    # Display the revealed matrix
    for row in revealed_matrix:
        print(' | '.join(map(str, row)))
        print('-' * (cols * 4 - 1))

    # Get player input
    row_choice = int(input("Choose a row (0-3): "))
    col_choice = int(input("Choose a column (0-3): "))

    # Reveal the selected tile
    revealed_matrix[row_choice][col_choice] = matrix[row_choice][col_choice]

    # Display the updated revealed matrix
    for row in revealed_matrix:
        print(' | '.join(map(str, row)))
        print('-' * (cols * 4 - 1))

    modify = input("Do you want to modify this value? (yes/no): ")
    if modify.lower() == 'yes':
        new_value = int(input("Enter a new value: "))
        matrix[row_choice][col_choice] = new_value

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        for row in matrix:
            print(' | '.join(map(str, row)))
            print('-' * (cols * 4 - 1))
        print(matrix)
        break

print("Thanks for playing!")