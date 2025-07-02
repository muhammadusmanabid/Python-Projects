points = {
'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4,
'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1,
'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1,
'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8,
'Y': 4, 'Z': 10
}

def scrabble():
    player1 = input("Player1: ").upper()
    player2 = input("Player2: ").upper()
    score1 = 0
    score2 = 0

    for letter in player1:
        if letter in points:
            score1 += points[letter]

    for letter in player2:
        if letter in points:
            score2 += points[letter]
    
    if score1 > score2:
        print("Player1 Wins!")
    elif score1 < score2:
        print("Player2 Wins!")
    else:
        print("Tie!")