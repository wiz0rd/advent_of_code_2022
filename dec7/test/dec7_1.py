import subprocess
import re
import os
wd = os.getcwd()

print(os.getcwd())
with open("input.txt", 'r') as r:
    for line in r:
        line = line.strip()
        result = re.match("[0-9]", line)
        if result:
            line = line.split()
            line = '_'.join(line)
            print(line)
            subprocess.run(["touch " + line], shell=True)
        elif line.startswith("dir"):
            subprocess.run(["mkdir " + line.split()[1]], shell=True)
        elif line.startswith("$ cd"):
            line = line.split()
            wd = os.getcwd()
            os.chdir(wd + "/" + line[2])