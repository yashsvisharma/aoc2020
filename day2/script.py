# Advent of Code 2020: Day 2
# Yash Sharma
# me@yashsharma.com

# validate strings based on provided rules

# read file into list of ints called nums
with open("input.txt", "r") as file:
    text = [str(line) for line in file.readlines()]

#create valid pw counter
textParsed = []

for entry in text:
    textParsed.append(entry.split())

def validate():

    valid = 0

    # get min number
    min = textParsed[1][0].split('-')[0]
    print(min)

    # get max number
    max = textParsed[1][0].split('-')[1]
    print(max)

    # get validation char
    char = textParsed[1][1][0]
    print(char)

    # get string to validate
    testString = textParsed[1][2]
    print(testString)

    # test for char reps
    count = 0
    for i in testString:
        if i == char:
            count = count + 1
    
    # is it valid?
    if (count >= min) and (count <=max):
        valid += 1

    print(valid)


validate()