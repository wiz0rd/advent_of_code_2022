total_score = 0
round_score = 0

with open('input.txt', 'r') as r:

    for line in r:
        line = line.strip().split()
        #print(line)

        if line[0] == 'A': #ROCK OPPONENT

            if line[1] == 'X': #NEED TO LOSE
                total_score += 3 
            elif line[1] == 'Y': #NEED TO DRAW
                total_score += (1+3)
            elif line[1] == 'Z': #NEED TO WIN
                total_score += (2+6)
        elif line[0] == 'B': #PAPER OPPONENT

            if line[1] == 'X': #NEED TO LOSE
                total_score += 1
            elif line[1] == 'Y': #NEED TO DRAW
                total_score += (2+3)
            elif line[1] == 'Z': #NEED TO WIN
                total_score += (3+6)
        elif line[0] == 'C': #SCISSORS OPPONENT

            if line[1] == 'X': #NEED TO LOSE
                total_score += 2
            elif line[1] == 'Y': #NEED TO DRAW
                total_score += (3+3)
            elif line[1] == 'Z': #NEED TO WIN
                total_score += (1+6)
print(total_score)
