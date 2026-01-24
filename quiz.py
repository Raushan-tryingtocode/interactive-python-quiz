questions = [{"question": "How many planets in the solar system?",
              "option": ["A. 11", "B. 10", "C. 8", "D. 7"],
              "answer": "C"},
             {"question": "Which is the hottest planet?",
              "option": ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"],
              "answer": "B"},
             {"question": ".Who lays the biggest egg in the animal kingdom?",
              "option": ["A. Elephant", "B. Whale", "C. Ostrich", "D. Lion"],
              "answer": "C"},
             {"question": "How many bones in the human body?",
              "option": ["A. 201", "B. 206", "C. 207", "D. 221"],
              "answer": "B"},
             {"question": ".What is the most abundant gas the earth's atmosphere?",
              "option": ["A. Oxygen", "B. Hydrogen", "C. Nitrogen", "D. Helium"],
              "answer": "C"},
             {"question": "Electric bulb filament is made of .",
              "option": ["A. Copper", "B. Aluminum", "C. Lead", "D. Tungsten"],
              "answer": "D"},
             {"question": "What did James Watt invent?",
              "option": ["A. steam engine", "B. Steam boat",
                         "C. Hot air balloon", "D. Diving bell"],
              "answer": "A"},
             {"question": "When is the World Population Day?",
              "option": ["A. 31 May", "B. 4 October", "C. 10 December", "D. 11 July"],
              "answer": "D"},
             {"question": "The blueness of the sky is mainly due to:",
              "option": ["A. The scattering of sunlight by air molecules", "B. The presence of water vapor", "C. Absorption of blue light by the air", "D. Emission of blue light by the atmosphere"],
              "answer": "A"}]


guesses = []
score = 0

for question in questions:
    print("-----------------------------")
    print(question["question"])
    for opt in question["option"]:
        print(opt)

    while True:
        guess = input("enter you guess (A, B, C or D):").upper()

        if guess in ["A", "B", "C", "D"]:
            break
        print("please enter value A,B,C or D only")

    guesses.append(guess)
    if guess == question["answer"]:
        score += 1
        print("CORRECT ANSWER")
    else:
        print("INCORRECT ANSWER")
        print(f"The {question["answer"]} is the correct answer")

print("------------------------------")
print("-----------RESULT-------------")
print("------------------------------")

print("answer: ", end="\r")
for ans in questions:
    print(ans["answer"], end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}% ")
