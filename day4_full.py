import re

sum = 0
with open ("input.txt", "r") as f:
    for line in f:
        counter = 0

        line = re.sub("Card\W+\d+: ", "", line.strip()).split("|")
        winningNums = [int(num) for num in line[0].split()]
        myNums = [int(num) for num in line[1].split()]

        for number in winningNums:
            if number in myNums:
                counter += 1

        score = 1
        for i in range(1, counter):
            score = score * 2

        if counter not in [0, 1]:
            sum += score
        else:
            sum += counter

print(f"Part 1: {sum}")

# Part 2 -- Efficient? Hell no. Does it run? Eventually... ♥
with open ("input.txt", "r") as f:
    cards = []
    card = 1 # I know, I know...
    for line in f:
        cardCount = card
        win = []
        winCount = 0
        line = re.sub("Card\W+\d+: ", "", line.strip()).split("|")
        winningNums = [int(num) for num in line[0].split()]
        myNums = [int(num) for num in line[1].split()]

        for num in winningNums:
            if num in myNums:
                win.append("x")
                winCount = 1

        for winningCard in cards:
            if winningCard == card:
                winCount += 1

        for i in range(winCount):
            addCards = card
            for item in win:
                addCards += 1
                cards.append(addCards)

        card += 1

print(f"Part 2: {len(cards)+card-1}")