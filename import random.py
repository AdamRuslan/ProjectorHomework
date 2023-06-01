import random

# Generate and append random numbers to the files
for i in range(26):
    file_name = chr(ord('A') + i) + ".txt"
    random_number = random.randint(1, 100)
    
    with open(file_name, "a") as file:
        file.write(str(random_number) + "\n")

# Create the summary file
summary_file_name = "summary.txt"
with open(summary_file_name, "w") as summary_file:
    for i in range(26):
        file_name = chr(ord('A') + i) + ".txt"
        with open(file_name, "r") as file:
            number = file.readline().strip()
            summary_file.write(f"{file_name}: {number}\n")
