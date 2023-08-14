questions = ("Which cricket team has won most ICC Cricktet world cup titles?: ",
            "Which of the following country did not won the ICC cricket world cup(50 over format)title so far?: ",
            "Which of the following indian player have got first Man of the Tournament award in the ICC cricket world cup?: ",
            "When was the first world cup started?: ",
            "Who was the first indian captain to win ICC World cup? : ")

options = (("A. WI", "B. IND", "C. ENG", "D. AUS"),
            ("A. SA", "B. NZ", "C. ENG", "D. Both A and B"),
            ("A. Sachin Tendulkar", "B. Mohinder Amarnath", "C. MS Dhoni", "D. Yuvaraj singh"),
            ("A. 1975", "B. 1983", "C. 1979", "D. 1972"),
            ("A. Sachin Tendulkar", "B. Kapil Dev", "C. MS Dhoni", "D.None of these"))

answers = ("D", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
