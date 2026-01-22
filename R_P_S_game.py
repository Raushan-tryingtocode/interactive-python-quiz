import random


options = ("Rock", "Paper", "Scissors")
user_score = 0
bot_score = 0


while True:
    user = input("choose your move (Q to quit) : ").capitalize()

    if user == "Q":
        break

    if user not in options:
        print("Invalid choice.Please select either Rock, Paper or Scissors")

    bot_option = random.choice(options)
    print(f"Bot chose : {bot_option}")

    print(bot_option)
    if (user == "Rock" and bot_option == "Scissors") or (user == "Paper" and bot_option == "Rock") or (user == "Scissors" and bot_option == "Paper"):
        print("The user scores 1 point")
        user_score += 1
    elif (user == "Rock" and bot_option == "Paper") or (user == "Paper" and bot_option == "Scissors") or (user == "Scissors" and bot_option == "Rock"):
        print("The bot scores 1 point")
        bot_score += 1
    elif user == bot_option:
        print("That's a tie")


print(f"The User's score is : {user_score}")
print(f"The Bot's score is : {bot_score}")

print("---------------------------------------")
print("---------------Scoreboard--------------")
print("---------------------------------------")

if user_score > bot_score:
    score_1 = user_score - bot_score
    print(f"Ther user is the winner with {score_1} points")
elif user_score < bot_score:
    score_2 = bot_score - user_score
    print(f"Ther bot is the winner with {score_2} points")
elif user_score == bot_score:
    print("It's a tie")

print("---------------------------------------")
