import re
sum = 0

#  Part 1:
with open ("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        nums = re.findall("\d", line)
        sum += int(nums[0] + nums[-1])

print(f"Total sum part 1: {sum}")

# Part 2:
sum = 0
numDict = {"oneight": 18, "twone": 21, "zerone": "01", "threeight": 38, "sevenine": 79, "fiveight": 58, "eightwo": 82, "eighthree": 83, 
           "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

with open ("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        for key in numDict.keys():
            if key in line:
                line = line.replace(key, str(numDict[key]))
        
        nums = re.findall("\d", line)
        sum += int(nums[0] + nums[-1])

print(f"Total sum part 2: {sum}")
