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
    current_question = 0
    for question in questions:
         while True:
            answer = input(question.question + "\n").lower().strip()
            if answer not in ['a', 'b', 'c', 'd']:
                print("Input not valid. Please enter a, b, c, or d. ")
            else: 
                break

         if answer.lower() == question.answer:   
            Score += 1
            current_question += 1
            print("\nCorrect! " + str(Score) + " out of " + str(current_question))
         else:
             current_question += 1
             print("\nWrong! The correct answer was (" + question.answer + "). " + str(Score) + " out of " + str(current_question) + "\n")

    percentage = (Score / len(questions)) * 100

    print("You got " + str(Score) + " out of " + str(len(questions)) + "! " + str(percentage) + "%")

run_test(Prompt)