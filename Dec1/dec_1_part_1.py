current_high_score = 0
current_score = 0

with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        if line != '':
            current_score += int(line)
        elif line == '':
            if current_score > current_high_score:
                current_high_score = current_score
            current_score = 0

print(current_high_score)


