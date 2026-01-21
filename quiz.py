import json
import random

QUESTIONS_PATH = "data/questions.json"
NUM_QUESTIONS = 5

def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def ask_question(q, number):
    print("\n" + "=" * 60)
    print("Question" + str(number))
    print("Section: " + str(q.get('section'))+ " | Topic: " + str(q.get('topic')) + " | Difficulty: " + str(q.get('difficulty')))
    print("-" * 60)
    print(q["question"])
    print()

    choices = q["choices"]
    for i, choice in enumerate(choices, start=1):
        print(str(i) + "." + str(choice))

    while True:
        ans = input("\nYour answer (1-4): ").strip()
        if ans in {"1", "2", "3", "4"}:
            return choices[int(ans) - 1]
        print("Please type 1, 2, 3, or 4.")

def main():
    questions = load_questions(QUESTIONS_PATH)

    if len(questions) < NUM_QUESTIONS:
        raise ValueError("Need at least" + str(NUM_QUESTIONS) + "questions, but found" + str(len(questions)) + ".")

    selected = random.sample(questions, k=NUM_QUESTIONS)

    responses = []
    for idx, q in enumerate(selected, start=1):
        user_choice = ask_question(q, idx)
        responses.append({
            "id": q["id"],
            "topic": q.get("topic"),
            "chosen": user_choice,
            "correct": q["answer"]
        })

    print("\n" + "=" * 60)
    print("Quiz complete! (Scoring comes tomorrow.)")
    print("Your responses were recorded.")
    print("=" * 60)

    for r in responses:
        print("Q"+ str(r['id'])+ " | Topic: " + str(r['topic']) +" | You chose: " + str(r['chosen']))

if __name__ == "__main__":
    main()
