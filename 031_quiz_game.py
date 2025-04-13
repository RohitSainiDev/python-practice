questions = (
    "1. How many hearts does an octopus have?",
    "2. Which of these foods essentially never spoils?",
    "3. By how much can the Eiffel Tower grow in summer heat?",
    "4. What approximate percentage of DNA do humans share with bananas?",
    "5. On which planet is a day longer than its year?",
)

options = (
    ("a. One", "b. Two", "c. Three", "d. Four"),
    ("a. Dried Rice", "b. Honey", "c. Pickled Onions", "d. Salted Cod"),
    ("a. 15 cm", "b. 1 cm", "c. 1 meter", "d. 5 meters"),
    ("a. 5-10%", "b. 20-30%", "c. 90-95%", "d. 50-60%"),
    ("a. Mars", "b. Jupiter", "c. Venus", "d. Mercury"),
)

guesses = []
score = 0
question_num = 0
answers = ("C", "B", "A", "D", "C")

for question in questions:
    print("--------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter your option (a,b,c,d): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Yay! Correct Answer")
        score += 1
    else:
        print(f"Incorrect! {answers[question_num]} is the correct answer.")

    question_num += 1

print("--------------------------------------------------------------------")
print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("--------------------------------------------------------------------")

print("--------------------------------------------------------------------")
print("Guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()
print("--------------------------------------------------------------------")

score = int(score / question_num * 100)
print(f"Your score is {score}%")
