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

    numValid_part1 = 0
    numValid_part2 = 0

    # test every item in list
    for target in (textParsed):
        # get min number
        min = target[0].split('-')[0]
        min = int(min)

        # get max number
        max = target[0].split('-')[1]
        max = int(max)

        # get validation char
        char = target[1][0]

        # get string to validate
        testString = target[2]

        # do actual validation for part 1
        count = 0
        for i in testString:
            if i == char:
                count += 1
        
        if (count >= min) and (count <=max):
            numValid_part1 += 1

        # do validation for part 2
        valid = False
        try:
            if (testString[min-1]) == char:
                valid = not valid

            if (testString[max-1]) == char:
                valid = not valid
        except: continue

        if valid:
            numValid_part2 += 1

    
    print(numValid_part1)
    print(numValid_part2)


validate()