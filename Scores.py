import csv

# Read data from the previous CSV file
with open('game_results.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    scores = {}
    for row in reader:
        player = row[0]
        score = int(row[1])
        if player in scores:
            scores[player] = max(scores[player], score)
        else:
            scores[player] = score

# Sort scores in descending order
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

# Create a new CSV file with high scores
with open('high_scores.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Player name', 'Highest score'])
    for player, score in sorted_scores:
        writer.writerow([player, score])

print("High scores CSV file has been created.")