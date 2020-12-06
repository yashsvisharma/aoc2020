# Advent of Code 2020: Day 3
# Yash Sharma
# me@yashsharma.com

# tree or no tree?

# read file into list line by line
with open("input.txt", "r") as file:
    text = file.readlines()

lineCounter = 0
treeCounter = 0
cursor = 0

for line in text:
    if (line[(cursor % 31)] == '#'):
        treeCounter += 1
    cursor += 3

print(treeCounter)
