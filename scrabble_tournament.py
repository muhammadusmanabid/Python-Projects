points = {
'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
'Y': 4, 'Z': 10
}

while True:
    print("Welcome to Scrabble Tournamnet!")
    player1 = input("Player1 Name: ").upper()
    player2 = input("Player2 Name: ").upper()

    score1 = 0
    score2 = 0
    
    total_score1 = 0
    total_score2 = 0
    
    highest_word_score1 = 0
    highest_word_score2 = 0
    
    longest_word_length1 = 0
    longest_word_length2 = 0

    rounds = int(input("How many rounds? ").strip())
    for i in range(rounds):
        player1_words = input(f"{player1}'s word: ").upper()
        player2_words = input(f"{player2}'s word: ").upper()

        for letter in player1_words:
            if letter in points:
                score1 += points[letter]

        for letter in player2_words:
            if letter in points:
                score2 += points[letter]
                
        length1 = len([l for l in player1_words if l in points])
        length2 = len([l for l in player2_words if l in points])
        
        total_score1 = score1
        total_score2 = score2

        if score1 > highest_word_score1:
            highest_word_score1 = score1
        if score2 > highest_word_score2:
            highest_word_score2 = score2

        if length1 > longest_word_length1:
            longest_word_length1 = length1
        if length2 > longest_word_length2:
            longest_word_length2 = length2

        if score1 > score2:
            print(f"{player1} wins Round {i + 1}!")
        elif score2 > score1:
            print(f"{player2} wins Round {i + 1}!")
        else:
            print("Round is Tied!")

    print("Final Results:")
    print(f"{player1} - Total: {total_score1}, Highest Word: {highest_word_score1}, Longest Word: {longest_word_length1}")
    print(f"{player2} - Total: {total_score2}, Highest Word: {highest_word_score2}, Longest Word: {longest_word_length2}")
 
    if total_score1 > total_score2:
        print(f"{player1} wins the Tournament!")
    elif total_score2 > total_score2:
        print(f"{player2} wins the Tournament!")
    else:
        if highest_word_score1 > highest_word_score2:
            print(f"{player1} wins by Highest Word Score!")
        elif highest_word_score2 > highest_word_score1:
            print(f"{player2} wins by Highest Word Score!")
        else:
            if longest_word_length1 > longest_word_length2:
                print(f"{player1} wins by Longest Word!")
            elif longest_word_length2 > longest_word_length1:
                print(f"{player2} wins by Longest Word!")
            else:
                print("It's a draw!")
    
    play_again = input("Want to play again? (Y/N)").strip()

    if play_again != "Y":
        break

        


