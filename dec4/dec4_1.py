score = 0
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip().split(',')
        #print(line)
        current_first_low = 'placeholder'
        current_first_high = 'placeholder'
        current_second_low = 'placeholder'
        current_second_high = 'placeholder'
        #print(line[0])
        first_numbers = line[0].split('-')
        second_numbers = line[1].split('-')
        #print(first_numbers)
        current_first_low = int(first_numbers[0])
        current_first_high = int(first_numbers[1])
        current_second_low = int(second_numbers[0])
        current_second_high = int(second_numbers[1])
        if current_second_low >= current_first_low and current_second_high <= current_first_high:
            score += 1
        elif current_first_low >= current_second_low and current_first_high <= current_second_high:
            score += 1
print(score)

