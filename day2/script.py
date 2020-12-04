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

    numValid = 0

    # test every item in list
    for target in (textParsed):
        # get min number
        min = target[0].split('-')[0]

        # get max number
        max = target[0].split('-')[1]

        # get validation char
        char = target[1][0]

        # get string to validate
        testString = target[2]

        # do actual validation
        count = 0
        for i in testString:
            if i == char:
                count += 1
        
        if (count >= int(min)) and (count <=int(max)):
            numValid += 1
    
    print(numValid)


validate()