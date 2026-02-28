import random
def random_decision_maker():
    print("\nWelcome to Random Decision Maker\n")
    while True:
        try:
            question = input("Enter your question: ").strip()
            if not question:
                raise ValueError("Empty input try again!")
            break
        except ValueError as e:
            print(e)
    while True:
        try:
            answer = input("Enter your dections with comma: ").split(",")
            if not any(item.strip() for item in answer):
                raise ValueError("Empty input try again!")
            break
        except ValueError as e:
            print(e)
    choice = random.choice(answer)
    print(f"Your dection is: {choice}")

