import re

directories = []
directory_value = {}
with open('input.txt', 'r') as r:
    for line in r:
        line = line.strip()
        #print(line)
        if line.startswith('$') and line.split()[1] == 'cd':
            if line.split()[2].isalpha():
                directories.append(line.split()[2])

with open('input.txt', 'r') as r:
    for line in r:
        current_values = []
        current_directory = 'placeholder'
        line = line.strip().split()
        for directory in directories:
            if line[0].startswith('$') and directory in line:
                current_directory = directory
            else:
                if current_directory not in directory_value.keys():
                    current_values.append(line)
        directory_value[current_directory] = current_values

print(directory_value)          
        


#        elif re.match("\d", line.split()[0]) == True:
#            print('regex hit')
#        print(line.split()[0])       
#            #elif line.split()[0].isnumeric():
#            #    print('True)')
#print(directories)
#for directory in directories:
#    directory_value[directory] = 0
#
#print(directory_value)