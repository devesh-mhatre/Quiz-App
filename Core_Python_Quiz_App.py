import random

# Quiz data structure
quiz_data = {
    "Variables": [
        {"question": "Which of the following is a valid variable name?", "options": ["2var", "_var", "var-1", "var name"], "answer": "_var"},
        {"question": "What is the default value of a variable in Python?", "options": ["0", "None", "Null", "Undefined"], "answer": "None"},
        {"question": "Which keyword is used to define a variable in Python?", "options": ["let", "var", "define", "None of the above"], "answer": "None of the above"},
        {"question": "What symbol is used to assign a value to a variable?", "options": [":", "=", "->", "=>"], "answer": "="}
    ],
    "Programming Statements": [
        {"question": "Which of the following is not a valid Python statement?", "options": ["print()", "return", "continue", "exit()"], "answer": "exit()"},
        {"question": "What does the 'pass' statement do in Python?", "options": ["Skips execution", "Exits a loop", "Does nothing", "Prints a message"], "answer": "Does nothing"},
        {"question": "Which of these is a compound statement?", "options": ["if", "print", "import", "None"], "answer": "if"},
        {"question": "What is the purpose of the 'break' statement?", "options": ["Stop execution", "Exit a loop", "Skip iteration", "None"], "answer": "Exit a loop"}
    ],
    "Conditional Constructs": [
        {"question": "What does 'elif' mean in Python?", "options": ["Else If", "End If", "Error If", "None"], "answer": "Else If"},
        {"question": "Which keyword is used for checking conditions?", "options": ["check", "if", "while", "switch"], "answer": "if"},
        {"question": "What will 'if True:' do?", "options": ["Run block", "Skip block", "Cause error", "Nothing"], "answer": "Run block"},
        {"question": "How do you write an inline conditional?", "options": ["if ... else", "? ... :", "when ... otherwise", "check ... or"], "answer": "if ... else"}
    ],
    "Functions": [
        {"question": "Which keyword is used to define a function?", "options": ["def", "func", "function", "lambda"], "answer": "def"},
        {"question": "What is a default argument?", "options": ["Mandatory", "Skipped", "Predefined", "Unused"], "answer": "Predefined"},
        {"question": "Can a function return multiple values?", "options": ["Yes", "No", "Only one", "Depends"], "answer": "Yes"},
        {"question": "What does the 'return' statement do?", "options": ["Exits function", "Repeats function", "Continues", "Stops program"], "answer": "Exits function"}
    ],
    "Loops": [
        {"question": "Which loop is used for iterating over sequences?", "options": ["while", "for", "do-while", "foreach"], "answer": "for"},
        {"question": "What does the 'continue' statement do?", "options": ["Exits loop", "Skips iteration", "Ends program", "None"], "answer": "Skips iteration"},
        {"question": "How do you create an infinite loop?", "options": ["while True", "for i in range", "loop forever", "if infinite"], "answer": "while True"},
        {"question": "What will 'break' do in a loop?", "options": ["End loop", "Skip iteration", "Continue loop", "Nothing"], "answer": "End loop"}
    ],
    "Strings": [
        {"question": "Which of these is a valid string in Python?", "options": ["'Hello'", "Hello", "`Hello`", "None"], "answer": "'Hello'"},
        {"question": "What does len() return for 'Python'?", "options": ["5", "6", "7", "None"], "answer": "6"},
        {"question": "Which operator concatenates strings?", "options": ["+", "*", "&", "None"], "answer": "+"},
        {"question": "Which method converts to uppercase?", "options": ["upper()", "capitalize()", "toUpper()", "toupper()"], "answer": "upper()"}
    ],
    "String Methods": [
        {"question": "Which method splits a string?", "options": ["split()", "join()", "divide()", "break()"], "answer": "split()"},
        {"question": "What does strip() remove?", "options": ["Spaces", "Symbols", "Digits", "All"], "answer": "Spaces"},
        {"question": "Which method finds a substring?", "options": ["find()", "index()", "search()", "None"], "answer": "find()"},
        {"question": "Which method joins strings?", "options": ["join()", "concat()", "merge()", "add()"], "answer": "join()"}
    ],
    "Lists": [
        {"question": "How do you create a list in Python?", "options": ["[]", "{}", "()", "<>"], "answer": "[]"},
        {"question": "Which method adds an element?", "options": ["append()", "add()", "push()", "insert()"], "answer": "append()"},
        {"question": "How do you access the last item?", "options": ["list[-1]", "list[0]", "list[last]", "list.end"], "answer": "list[-1]"},
        {"question": "What does list.sort() do?", "options": ["Sorts", "Reverses", "Adds items", "Removes duplicates"], "answer": "Sorts"}
    ],
    "Dictionaries": [
        {"question": "How do you create a dictionary?", "options": ["{}", "[]", "()", "<>"], "answer": "{}"},
        {"question": "What method gets a value by key?", "options": ["get()", "find()", "key()", "value()"], "answer": "get()"},
        {"question": "Can keys be duplicate?", "options": ["Yes", "No", "Sometimes", "Depends"], "answer": "No"},
        {"question": "What does dict.keys() return?", "options": ["Keys", "Values", "Items", "None"], "answer": "Keys"}
    ],
    "Sets": [
        {"question": "How do you create a set?", "options": ["{}", "[]", "set()", "<>"], "answer": "set()"},
        {"question": "What does set.add() do?", "options": ["Adds element", "Deletes element", "Sorts set", "Finds element"], "answer": "Adds element"},
        {"question": "Can sets have duplicate items?", "options": ["Yes", "No", "Sometimes", "Depends"], "answer": "No"},
        {"question": "What does set.union() do?", "options": ["Combines sets", "Finds intersection", "Removes duplicates", "None"], "answer": "Combines sets"}
    ],
    "Exceptions": [
        {"question": "What does 'try' do?", "options": ["Tests code", "Ignores errors", "Handles exceptions", "Ends program"], "answer": "Tests code"},
        {"question": "What keyword handles exceptions?", "options": ["catch", "except", "error", "handle"], "answer": "except"},
        {"question": "What does finally do?", "options": ["Always executes", "Executes on success", "Executes on failure", "Stops program"], "answer": "Always executes"},
        {"question": "What type of error is handled by try-except?", "options": ["SyntaxError", "LogicalError", "RuntimeError", "None"], "answer": "RuntimeError"}
    ]
}

def main_menu():
    print("Welcome to the Python Quiz Application!")
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
