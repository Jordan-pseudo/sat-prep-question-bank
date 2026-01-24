def ask_question(q, number):
    print("\n" + "=" * 60)
    print(f"Question {number}")
    print(f"Section: {q.get('section')} | Topic: {q.get('topic')} | Difficulty: {q.get('difficulty')}")
    print("-" * 60)
    print(q["question"])
    print()

    choices = q["choices"]
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        ans = input(f"\nYour answer (1-{len(choices)}): ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(choices):
            return choices[int(ans) - 1]
        print("Please type a valid choice number.")
