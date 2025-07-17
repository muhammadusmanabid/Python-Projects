import random

def calculate_digital_root(num):
    steps = []
    while num >= 10:
        char_sum = 0
        digit_list = []
        digits = str(num)
        # convertt str into digit to store and sum
        for char in digits:
            digit = int(char)
            digit_list.append(digit)
            char_sum += digit

        # list of steps
        str_list = ""
        for i in range(len(digit_list)):
            str_list += str(digit_list[i])
            if i < len(digit_list) - 1:
                str_list += " + "
        str_list += " = " + str(char_sum)
        steps.append(str_list)
        num = char_sum
    return num, steps
    
def is_specialNum(num):
    digit_sum = 0
    digit_product = 1
    order_num = str(num)
    reversed_num = order_num[::-1]

    if order_num == reversed_num:
        return True
    
    for char in order_num:
        digit = int(char)
        digit_sum += digit
        digit_product *= digit
    
    if digit_sum == digit_product:
        return True
    else:
        return False
    
def play_round(round, score):
    if round == 1:
        num = random.randint(100, 199)
    elif round == 2:
        num = random.randint(200, 299)
    else:
        num = random.randint(300, 399)
    
    print(f"Round: {round}: The number is: {num}")

    predicted_root = int(input("Predicts the digital root: "))
    actual_root, steps = calculate_digital_root(num)
    
    if predicted_root == actual_root:
        print("You predict the correct digital root!")
        score += 5
    for step in steps:
        print(step)

    guessed_special = input("The number is special (y/n)").strip().lower()
    actual_special = is_specialNum(num)

    if (guessed_special == "y" and actual_special == True) or (guessed_special == "n" and actual_special == False):
        print("You guess the correct special number!")
        score += 3

    return score

def play_game():
    print("Welcome to the Game!")
    score = 0
    for round in range(1, 4):
        print(f"Starting round {round}")

        score = play_round(round, score)

    print("The Game is Over!")
    print(f"You finals score is {score} out f 24")

play_game()