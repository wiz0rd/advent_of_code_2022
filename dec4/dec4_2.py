score = 0
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip().split(',')
        current_first_low = 'placeholder'
        current_first_high = 'placeholder'
        current_second_low = 'placeholder'
        current_second_high = 'placeholder'
        first_numbers = line[0].split('-')
        second_numbers = line[1].split('-')
        #print(first_numbers)
        current_first_low = int(first_numbers[0])
        current_first_high = int(first_numbers[1])
        current_second_low = int(second_numbers[0])
        current_second_high = int(second_numbers[1])
        current_first_list = []
        current_second_list = []
        for number in range(current_first_low - 1, current_first_high):
            current_first_list.append(number)
        print('first list')
        print(current_first_list)
        for number in range(current_second_low - 1, current_second_high):
            current_second_list.append(number)
        print('second list')
        print(current_second_list)
        for number in current_first_list:
            if number in current_second_list:
                score += 1
                break
print(score)
