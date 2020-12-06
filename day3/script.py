# Advent of Code 2020: Day 3
# Yash Sharma
# me@yashsharma.com

# tree or no tree?

# read file into list line by line
with open("input.txt", "r") as file:
    text = file.readlines()


def detectTrees(right, down):
    treeCounter = 0
    xCursor = 0
    yCursor = 0
    txtLength = len(text)

    for line in range(txtLength/down):
        if(text[yCursor % txtLength][xCursor % 31] == '#'):
            treeCounter += 1
        xCursor += right
        yCursor += down
    return treeCounter


# solution to part 1:
print(detectTrees(3, 1))

# solution to part 2:
print(
    detectTrees(1, 1) *
    detectTrees(3, 1) *
    detectTrees(5, 1) *
    detectTrees(7, 1) *
    detectTrees(1, 2)
)

