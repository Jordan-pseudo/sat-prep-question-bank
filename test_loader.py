import json

with open("data/questions.json", "r") as f:
    questions = json.load(f)

print("Loaded " + str(len(questions))  + " questions")
print("First question:")
print(questions[0]["question"])
