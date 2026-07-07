quiz_question=[
    {
    "question":"What is the capital of France?",
    "option":["a)Paris","b)London","c)Rome"],
    "answer":"a"
    },
    {
    "question":"What is the largest planet in our solar system?",
    "option":["a)Earth","b)Jupitar","c)Mars"],
    "answer":"b"
    }
]
def history(quiz_question):
    question(quiz_question)
def science(quiz_question):
    question(quiz_question)
def geography(quiz_question):
    question(quiz_question)
def question(quiz_question):
    for q in quiz_question:
        print(q["question"])
        for choice in q["option"]:
            print(choice)
        while True:
            choice=input("Enter you choice: ").lower()
            if choice =="a" or choice=="b" or choice=="c":
                if choice==q["answer"]:
                    print("Correct!")
                    break
                else:
                    print("Incorrect!")
                    break
            else:
                print("Invalid option!")

menu="\t\t\tQuiz Challenge\n\t\t\tCategories\n1. History\n2. Science\n3. Geography\n4. Exit"
while True:
    print(menu)
    choice=input("Enter you choice: ")
    if choice.isdigit():
        if choice=="1":
            history(quiz_question)
        elif choice=="2":
            science(quiz_question)
        elif choice=="3":
            geography(quiz_question)
        elif choice=="4":
            print("Exit")
            break
        else:
            print("Invalid choice!")
    else:
        print("It must be a digit!")

