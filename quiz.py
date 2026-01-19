questions = (("1.How many planets in the solar system?"),
             ("2.Which is the hottest planet?"),
             ("3.Who lays the biggest egg in the animal kingdom?"),
             ("4.How many bones in the human body?"),
             ("5.What is the most abundant gas the earth's atmosphere?"),
             ("6.Electric bulb filament is made of ."),
             ("7.What did James Watt invent?"),
             ("8. When is the World Population Day?"),
             ("9.The blueness of the sky is mainly due to:"))

options = (("A. 11", "B. 10", "C. 8", "D. 7"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"),
           ("A. Elephant", "B. Whale", "C. Ostrich", "D. Lion"),
           ("A. 201", "B. 206", "C. 207", "D. 221"),
           ("A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Helium"),
           ("A. Copper", "B. Aluminum", "C. Lead", "D. Tungsten"),
           ("A. steam engine", "B. Steam boat",
            "C. Hot air balloon", "D. Diving bell"),
           ("A. 31 May", "B. 4 October", "C. 10 December", "D. 11 July"),
           ("A. The scattering of sunlight by air molecules", "B. The presence of water vapor", "C. Absorption of blue light by the air", "D. Emission of blue light by the atmosphere"))

answers = ("C", "B", "C", "B", "C", "D", "A", "D", "A")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    while True:
        guess = input("enter you guess (A, B, C or D):").upper()

        if guess in ["A", "B", "C", "D"]:
            break
        print("please enter value A,B,C or D only")

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT ANSWER")
    else:
        print("INCORRECT ANSWER")
        print(f"The {answers[question_num]} is the correct answer")
    question_num += 1

print("------------------------------")
print("------------RESULT------------")
print("------------------------------")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}% ")
