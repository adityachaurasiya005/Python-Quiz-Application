questions = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".java", ".py", ".cpp", ".html"],
        "answer": "2"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
         "answer": "3"
    },
    {
        "question": "Which data type is used to store True or False?",
        "options": ["int", "bool", "float", "str"],
        "answer": "2"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["for", "switch", "match", "goto"],
        "answer": "1"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "2"
    },
    {
        "question": "What is the output of len('Python')?",
        "options": ["5", "6", "7", "8"],
        "answer": "2"
    },
    {
        "question": "Which keyword is used to exit a loop?",
        "options": ["continue", "stop", "break", "return"],
        "answer": "3"
    },
    {
        "question": "Which data structure stores keyvalue pairs?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "3"
    },
    {
        "question": "Which function is used to take input from the user?",
        "options": ["print()", "scan()", "input()", "read()"],
        "answer": "3"
    },
    {
        "question": "Which function displays output on the screen?",
        "options": ["echo()", "display()", "print()", "show()"],
        "answer": "3"
    }
]
def start_quiz():
    score = 0
    print("Starting quiz...")
    for i,q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")

        for idx, opt in enumerate(q['options'],1):
            print(f"    {idx}. {opt}")
        user_ans = input("Your answer: ").strip()

        if user_ans == q['answer']:
            print("Correct!!")
            score += 1
        else:
            print(f"Correct answer: {q['options'][int(q['answer'])-1]}")
        print("-"*30)
    percentage = (score*100)/len(questions)
    print("\nQuiz completed!!")
    print(f"Score: {score}\n")
    print(f"Percentage: {percentage:.2f}")
    if score >= 8:
        print("Grade: Excellent")
    elif score >= 6:
        print("Score: Good")
    elif score >= 4:
        print("Need improvement")
    else:
        print("Fail")
    with open("score.txt", "a") as f:
        f.write(f"{score}\n")


def view_highscore():
    try:
        score = 0
        with open("score.txt","r") as f:
            data = f.readlines()
            for i,line in enumerate(data,1):
                line = int(line)
                print(f"Attempt {i}: {line}")
                if line>score:
                    score = line
        print(f"Your highest score is {score}")
    except FileNotFoundError:
        print("No High Score yet")


def add_question():
    while True:
        if input("Do you want to add a question(y/n): ").lower() == "y":
            question = input("Enter the question: ").strip()
            if not question:
                print("Question can't be empty")
                return
            options = []
            for i in range(4):
                option = input(f"Enter option:").strip()
                if not option:
                    print("Option can't be empty")
                    return
                options.append(option)
            while True:
                answer = input("Enter the correct option (1-4): ")
                if answer in ["1","2","3","4"]:
                    questions.append (
                        {
                            "question" : question,
                            "options" : options,
                            "answer" : answer
                        }
                    )
                    return
                else:
                    print("Enter valid input")
        else:
            print("No questions added")
            return



def menu():
    while True:
        print("------Quiz Game------\n")
        print("1. Start Quiz")
        print("2. View High Score")
        print("3. Add Question")
        print("4. Exit")
        print("\n")
        
        match input("Enter your choice: "):
            case "1": start_quiz()
            case "2": view_highscore()
            case "3": add_question()
            case "4": 
                print("Quiz ended successfully.")
                return
            case _: 
                print("Enter a valid choice")
                
menu()