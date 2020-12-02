# Advent of Code 2020: Day 1
# Yash Sharma
# me@yashsharma.com

# find 2 nums that sum 2020 and return product

# read file into list of ints called nums
with open("input.txt", "r") as file:
    nums = [int(line) for line in file.readlines()]

#create storage variables
num1 = 0
num2 = 0

#find 2 nums whose sum is 2020
for x in nums:
    for y in nums:
        if (x+y) == 2020:
            num1 = x
            num2 = y

#multipy the 2 nums and get answer
print(num1 * num2)