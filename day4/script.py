# Advent of Code 2020: Day 4
# Yash Sharma
# me@yashsharma.com

# read input into program
with open("input.txt", "r") as file:
    text = file.read()
tokens = text.split("\n\n")

# generate passports from token
passports = []
for t in tokens:
    passports.append(t.split())


def processRawPassport(rawPassport): 
    dict = {}
    for info in rawPassport:
        (key, value) = info.split(':')
        dict[key] = value
    return dict    

print(processRawPassport(passports[16]))

def validatePassport(dictInput):
    status = False
    matches = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    if all(elem in dictInput.keys() for elem in matches):
        status = True
    return status

print(validatePassport(processRawPassport(passports[16])))

# validate each passport
numValid = 0

for passport in passports:
    if (validatePassport(processRawPassport(passport))):
        numValid += 1

print(numValid)