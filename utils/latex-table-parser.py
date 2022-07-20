import re

with open('../table.txt', 'r') as f:
    lines = f.readlines()
    
def parse_pm(string):
    value = float(string.replace(' ', '').replace('$\pm$', '').replace('E', 'e'))
    
    return f'$\pm$ {value}'
    
count = 0
for line in lines:
    for pm in re.findall(r'\(([^()]+)\)', line):
        line = line.replace(pm, parse_pm(pm))
    print(line)