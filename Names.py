import csv
import random

players = ["Josh", "Luke", "Kate", "Mark", "Mary"]

# Simulate 100 rounds for each player
game_results = []
for player in players:
    for _ in range(100):
        score = random.randint(0, 1000)
        game_results.append((player, score))

# Save the results to a CSV file
csv_file_name = "game_results.csv"
with open(csv_file_name, "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Player name", "Score"])
    writer.writerows(game_results)