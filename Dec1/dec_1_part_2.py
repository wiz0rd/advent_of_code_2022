current_high_score = 0
current_score = 0
all_scores = []

with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        if line != '':
            current_score += int(line)
        elif line == '':
            all_scores.append(int(current_score))
            if current_score > current_high_score:
                current_high_score = current_score
                #all_scores.append(int(current_high_score))
            current_score = 0
           
print(current_high_score)

top_3_scores = []

#print(all_scores.pop(max(all_scores)))
top_3_scores.append(max(all_scores))
all_scores.remove(max(all_scores))
top_3_scores.append(max(all_scores))
all_scores.remove(max(all_scores))
top_3_scores.append(max(all_scores))
all_scores.remove(max(all_scores))
print(top_3_scores)

#print(69289+68005+55717)

print(all_scores)
