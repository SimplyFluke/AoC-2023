# Part 1:
sum = 0
colors = {"blue": 14, "red": 12, "green": 13}

with open ("input.txt", "r") as f:
    for line in f:
        line = line.strip().replace(",", "").replace(":", ";").split(";")
        game_id = (int(line[0].replace("Game ", "")))
        passed = True
        
        for item in line:
            item = item.lstrip().split(" ")
            colorCount = {"blue": 0, "red": 0, "green": 0}
            
            for color in colors.keys():
                try:
                    checkColor = item.index(color)
                    colorCount[color] = int(item[checkColor-1])
                except:
                    pass
            
            for key in colors:
                if colors[key] < colorCount[key]:
                    passed = False  
        
        if passed:
            sum += int(game_id)

print(f"Sum part 1: {sum}")


# Part 2:
sum = 0

with open ("input.txt", "r") as f:
    for line in f:
        colorCount = {"blue": 0, "red": 0, "green": 0}
        line = line.strip().replace(",", "").replace(":", ";").split(";")
        game_id = (int(line[0].replace("Game ", "")))

        for item in line:
            item = item.lstrip().split(" ")
            for color in colorCount.keys():
                try:
                    checkColor = item.index(color)
                    if colorCount[color] < int(item[checkColor-1]):
                        colorCount[color] = int(item[checkColor-1])
                except:
                    pass
        
        sum += (colorCount["blue"]*colorCount["red"]*colorCount["green"])

print(f"Sum part 2: {sum}")