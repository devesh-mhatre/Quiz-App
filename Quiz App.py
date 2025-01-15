import random

# Quiz data structure
quiz_data = {
    "Science": [
        {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
        {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "NaCl"], "answer": "H2O"}
    ],
    "History": [
        {"question": "Who was the first President of the United States?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "answer": "George Washington"},
        {"question": "In which year did World War II end?", "options": ["1945", "1939", "1918", "1941"], "answer": "1945"}
    ],
    "Geography": [
        {"question": "What is the capital of France?", "options": ["Madrid", "Berlin", "Paris", "Rome"], "answer": "Paris"},
        {"question": "Which continent is the Sahara Desert located in?", "options": ["Asia", "Africa", "Europe", "Australia"], "answer": "Africa"}
    ]
}

def main_menu():
    print("Welcome to the Quiz Application!")
    print("Choose a category:")
    categories = list(quiz_data.keys())
    for idx, category in enumerate(categories, 1):
        print(f"{idx}. {category}")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Thank you for playing! Goodbye!")
        return False
    elif 1 <= choice <= len(categories):
        selected_category = categories[choice - 1]
        run_quiz(selected_category)
    else:
        print("Invalid choice. Please try again.")
    return True

def run_quiz(category):
    questions = quiz_data[category]
    random.shuffle(questions)
    score = 0

    for question in questions:
        print("\n" + question["question"])
        for idx, option in enumerate(question["options"], 1):
            print(f"{idx}. {option}")
        answer = input("Enter the number of your answer: ")

        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")

    print(f"\nYou scored {score} out of {len(questions)} in the {category} category.")

if __name__ == "__main__":
    while main_menu():
        pass
