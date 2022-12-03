final_letters = []
input_list = []
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        input_list.append(line)

def make_group():
    current_group = []
    current_group.append(input_list.pop(0))
    current_group.append(input_list.pop(0))
    current_group.append(input_list.pop(0))
    print(current_group)
    return current_group

def crunch():
    group_now = make_group()
    for letter in group_now[0]:
        if letter in group_now[1] and letter in group_now[2]:
            print(letter)
            final_letters.append(letter)
            break
try:
    for number in range(1000):
        crunch()

except:
    IndexError

print(final_letters)
#make_group()

scoring = {
       'a': 1,
       'b': 2,
       'c': 3,
       'd': 4,
       'e': 5,
       'f': 6,
       'g': 7,
       'h': 8,
       'i': 9,
       'j': 10,
       'k': 11,
       'l': 12,
       'm': 13,
       'n': 14,
       'o': 15,
       'p': 16,
       'q': 17,
       'r': 18,
       's': 19,
       't': 20,
       'u': 21,
       'v': 22,
       'w': 23,
       'x': 24,
       'y': 25,
       'z': 26,
       'A': 27,
       'B': 28,
       'C': 29,
       'D': 30,
       'E': 31,
       'F': 32,
       'G': 33,
       'H': 34,
       'I': 35,
       'J': 36,
       'K': 37,
       'L': 38,
       'M': 39,
       'N': 40,
       'O': 41,
       'P': 42,
       'Q': 43,
       'R': 44,
       'S': 45,
       'T': 46,
       'U': 47,
       'V': 48,
       'W': 49,
       'X': 50,
       'Y': 51,
       'Z': 52,
        }
score = 0

for letter in final_letters:
    score += scoring[letter]

print(score)
