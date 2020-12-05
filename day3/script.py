# Advent of Code 2020: Day 3
# Yash Sharma
# me@yashsharma.com

# tree or no tree?

# read file into list line by line
with open("input.txt", "r") as file:
    text = [str(line) for line in file.readlines()]

textParsed = []
for entry in text:
    textParsed.append(entry.split())

print(textParsed)