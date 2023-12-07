from itertools import permutations

lines = []
niceNums = []
num = ""
nice = False

with open("input.txt", "r") as f:
    for line in f:
        lines.append (line.strip())

for row in range(len(lines[0])):
    for col in range (len(lines)):
        current = lines[row][col]

        if current.isdigit():
            if col == 0:
                try:
                    niceNums.append(int(num))
                    num = ""
                except:
                    pass

            num += current
            checkRow = [row-1, row, row+1]
            checkCol = [col-1, col, col+1]
            tmpUnique = []
            unique = set()
            permut = permutations(checkRow, len(checkCol))
            
            for comb in permut:
                zipped = zip(comb, checkCol)
                tmpUnique.append(list(zipped))

            for items in tmpUnique:
                for item in items:
                    unique.add(item)

            for item in unique:
                try:
                    checkPos = lines[item[0]][item[1]]
                    
                    if not checkPos.isalnum() and checkPos != ".":
                        nice = True
                except:
                    pass
        else:
            if nice == True:
                niceNums.append(int(num))
                num = ""
                nice = False
            
            elif nice == False:
                num = ""
    
print(sum(niceNums))
