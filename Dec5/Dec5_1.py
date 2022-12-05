## this section was hand jammed - just shows the initial crate configuration
blocks = {
    1:['D','H','N','Q','T','W','V','B'],
    2:['D','W','B'],
    3:['T','S','Q','W','J','C'],
    4:['F','J','R','N','Z','T','P'],
    5:['G','P','V','J','M','S','T'],
    6:['B','W','F','T','N'],
    7:['B','L','D','Q','F','H','V','N'],
    8:['H','P','F','R'],
    9:['Z','S','M','B','L','N','P','H']
}

## this section works the magic of moving the crates
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip().split()
        for number in range(int(line[1])):
            blocks[int(line[5])].append(blocks[int(line[3])].pop())

## this section just gets the output in the desired state            
top_blocks = []    
for k, v in blocks.items():
    top_blocks.append(v[-1])
    
print('ANSWER:' + ''.join(top_blocks))