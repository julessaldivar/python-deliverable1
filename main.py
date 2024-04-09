name = input("Welcome to GC mini golf! What is your name? ")
number_holes = int(input(f"Hi, {name}! Would you like to play 3 or 6 holes today? "))
if number_holes == 3:
    number_putts1 = int(input("How many putts for hole 1? (par is 3) "))
    number_putts2 = int(input("How many putts for hole 2? (par is 3) "))
    number_putts3 = int(input("How many putts for hole 3? (par is 3) "))
    score = sum([number_putts1,number_putts2,number_putts3]) - 9
    if score >= 1:
        print(f"Nice try, {name}... Your total score was: +{score}")
    if score <= -1:
        print(f"Great job, {name}! Your total score was: {score}")
    elif score == 0:
        print(f"Good game, {name}. Your total score was 0.")

if number_holes == 6:
    number_putts1 = int(input("How many putts for hole 1? (par is 3) "))
    number_putts2 = int(input("How many putts for hole 2? (par is 3) "))
    number_putts3 = int(input("How many putts for hole 3? (par is 3) "))
    number_putts4 = int(input("How many putts for hole 4? (par is 3) "))
    number_putts5 = int(input("How many putts for hole 5? (par is 3) "))
    number_putts6 = int(input("How many putts for hole 6? (par is 3) "))
    score = sum([number_putts1,number_putts2,number_putts3,number_putts4,number_putts5,number_putts6]) - 18
    print(score)
    if score >= 1:
        print(f"Nice try, {name}... Your total score was: +{score}")
    if score <= -1:
        print(f"Great job, {name}! Your total score was: {score}")
    elif score == 0:
        print(f"Good game, {name}. Your total score was 0.")
