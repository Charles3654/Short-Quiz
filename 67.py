from Level import Question


question_Bank = [ 
    "What is the capital of France?\n(a) Rome\n(b) Berlin\n(c) Paris\n(d) Madrid",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Saturn\n(d) Neptune",
    "What is the biggest mammal on Earth?\n(a) Elephant\n(b) Blue Whale\n(c) Giraffe\n(d) Hippopotamus",
    "What city is the 49ers football team based in?\n(a) San Francisco\n(b) Los Angeles\n(c) Seattle\n(d) Denver"
]

Prompt = [
   Question(question_Bank[0], "c"),
   Question(question_Bank[1], "b"),
   Question(question_Bank[2], "b"),
   Question(question_Bank[3], "a"),
]

def run_test(questions):
    Score = 0
    for question in questions:
        answer = input(question.question + "\n")
        if answer.lower() == question.answer:
            Score += 1
            print("\nCorrect! " + str(Score) + " out of 4\n")
        else:
            print("\nWrong! The correct answer was (" + question.answer + "). " + str(Score) + " out of 4\n")
    print("You got " + str(Score) + " out of " + str(len(questions)) + "!")

run_test(Prompt)