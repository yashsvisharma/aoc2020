# Advent of Code 2020: Day 4
# Yash Sharma
# me@yashsharma.com

# read input into program
with open("input.txt", "r") as file:
    text = file.read()
textBlocks = text.split("\n\n")

ppList = []
ppDict = {}

# place all items in list
for passport in textBlocks:
    ppList.append(passport.split())

# ppList has all passports now
print(len(ppList))


for ppAtribute in ppList[0]:
    (key, val) = ppAtribute.split(':')
    ppDict[key] = val

print(ppDict)

def processPP(passport):
    validPP = False

    # checks if 8 items exist
    if (len(passport) == 8):
        validPP = not validPP
        return validPP
    
    # check if all exist ecept cid
    matches = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    if all(elem in passport.keys() for elem in matches):
        validPP = not validPP
        return validPP
