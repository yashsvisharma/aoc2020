# Advent of Code 2020: Day 1
# Yash Sharma
# me@yashsharma.com

# find 2 nums that sum 2020 and return product

# read file into list of ints called nums
with open("input.txt", "r") as file:
    nums = [int(line) for line in file.readlines()]

#find 2 nums whose sum is 2020
def solution1():
    for x in nums:
        for y in nums:
            if (x+y) == 2020:
                return(x*y)

#answer part 1
print('Part 1 Solution: ' + str(solution1()))

#find 3 nums whose sum is 2020
def solution2():
    for x in nums:
        for y in nums:
            for z in nums:
                if (x+y+z) == 2020:
                    return(x*y*z)

#answer part 2
print('Part 2 Solution: ' + str(solution2()))