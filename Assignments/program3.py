questions = [
    {
        "q": "Which keyword is used to create a function in Python?",
        "options": ["A) func", "B) def", "C) function", "D) define"],
        "answer": "B"
    },
    {
        "q": "What is the default return value of a function that doesn't have a return statement?",
        "options": ["A) 0", "B) undefined", "C) None", "D) False"],
        "answer": "C"
    },
    {
        "q": "Which of the following is a correct way to call a function named `my_func`?",
        "options": ["A) call my_func()", "B) my_func[]", "C) my_func()", "D) my_func{}"],
        "answer": "C"
    },
    {
        "q": "What will `print(type(lambda x: x))` output?",
        "options": ["A) <class 'function'>", "B) <class 'lambda'>", "C) <function>", "D) <lambda>"],
        "answer": "A"
    },
    {
        "q": "Which of the following is used to return a value from a function?",
        "options": ["A) return", "B) yield", "C) break", "D) pass"],
        "answer": "A"
    },
    {
        "q": "What is the output of this code?\n\ndef add(a, b=2):\n    return a + b\n\nprint(add(3))",
        "options": ["A) 5", "B) 3", "C) Error", "D) None"],
        "answer": "A"
    },
    {
        "q": "Which type of arguments can be passed using *args?",
        "options": ["A) Only keyword arguments", "B) Variable number of positional arguments", "C) Fixed arguments", "D) Named arguments"],
        "answer": "B"
    },
    {
        "q": "What does the following function return?\n\ndef test():\n    pass",
        "options": ["A) pass", "B) Error", "C) None", "D) 0"],
        "answer": "C"
    },
    {
        "q": "What is the output of this code?\n\ndef outer():\n    def inner():\n        return 'Hello'\n    return inner()\n\nprint(outer())",
        "options": ["A) Hello", "B) inner", "C) outer", "D) Error"],
        "answer": "A"
    },
    {
        "q": "Which of the following best describes recursion?",
        "options": ["A) A function that calls itself", "B) A loop inside a function", "C) A class inside a function", "D) A function that returns another function"],
        "answer": "A"
    }
]

score = 0

for i, key in enumerate(questions):
    print(f"\nQuestion {i+1}: {key['q']}")
    for opt in key['options']:
        print(opt)
    user_ans = input("Your answer (A/B/C/D): ").strip().upper()
    
    if user_ans == key['answer']:
        print("Correct answer ")
        score += 1
    else:
        print(f"Wrong ! Correct answer is {key['answer']}")

print("\n--- Quiz Completed ---")
print(f"Your Score: {score}/10")

if score == 10:
    print(" Excellent! You got 10/10")
elif score >= 6:
    print("Average performance")
elif score >= 4:
    print(" Needs improvement")
else:
    print(" Fail — Keep practicing!")