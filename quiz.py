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

def score_responses(responses):
    total = len(responses)
    correct_count = 0
    topic_stats = {}

    for r in responses:
        is_correct = r["chosen"] == r["correct"]
        if is_correct:
            correct_count += 1

        topic = r["topic"]
        if topic not in topic_stats:
            topic_stats[topic] = {"correct": 0, "total": 0}

        topic_stats[topic]["total"] += 1
        if is_correct:
            topic_stats[topic]["correct"] += 1

    return correct_count, total, topic_stats


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
            "correct": q["answer"],
            "explanation": q.get("explanation")
        })

    print("\n" + "=" * 60)
    for r in responses:
        print("Q"+ str(r['id'])+ " | Topic: " + str(r['topic']) +" | You chose: " + str(r['chosen']))

    correct, total, topic_stats = score_responses(responses)
    accuracy = (correct / total) * 100
    print("\n" + "=" * 60)
    print("Quiz Results")
    print("=" * 60)
    print(f"Score: {correct} / {total}")
    print(f"Accuracy: {accuracy:.1f}%\n")

    print("Performance by Topic:")
    for topic, stats in topic_stats.items():
        topic_accuracy = (stats["correct"] / stats["total"]) * 100
        print(f"- {topic}: {topic_accuracy:.1f}% ({stats['correct']}/{stats['total']})")
    
    print("\nReview:")
    for r in responses:
        if r["chosen"] != r["correct"]:
            print("-" * 60)
            print(f"Question ID {r['id']}")
            print(f"Your answer: {r['chosen']}")
            print(f"Correct answer: {r['correct']}")
            print(f"Explanation: {r['explanation']}")

if __name__ == "__main__":
    main()
