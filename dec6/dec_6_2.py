## gets the input into a list ##
all_characters = []
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        line = list(line)
        for character in line:
            all_characters.append(character)
            
score = 0        
## defines a function to perform a round, pull four characters and check if the characters values are different, any score but 4 = differing characters
def pull_four_characters():
    char_count = 0
    fourteen_characters = []
    for character in all_characters[0:14]:
        fourteen_characters.append(character)
    for character in fourteen_characters:
        char_count += fourteen_characters.count(character)
    if char_count == 14:
        print(fourteen_characters)
        print("Winner!")
        return "STOP"
    else:
        all_characters.pop(0)
        global score 
        score += 1
## builds a while loop to execute the function until a value of 4 is found ##        
while pull_four_characters() != "STOP":
    pull_four_characters()

## prints the score ##
