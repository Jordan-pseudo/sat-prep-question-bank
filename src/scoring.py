def score_responses(responses):
    total = len(responses)
    correct_count = 0
    topic_stats = {}

    for r in responses:
        is_correct = r["chosen"] == r["correct"]
        if is_correct:
            correct_count += 1

        topic = r.get("topic", "Unknown")
        if topic not in topic_stats:
            topic_stats[topic] = {"correct": 0, "total": 0}

        topic_stats[topic]["total"] += 1
        if is_correct:
            topic_stats[topic]["correct"] += 1

    return correct_count, total, topic_stats
