# Read the content from the first file
first_file_name = "first_file.txt"
with open(first_file_name, "r") as first_file:
    content = first_file.read()

# Convert the content to uppercase
content_upper = content.upper()

# Write the uppercase content to the second file
second_file_name = "second_file.txt"
with open(second_file_name, "w") as second_file:
    second_file.write(content_upper)