file = open("input.txt","r")
line = file.readline()
file.close()
line = line.strip('\n')

def split_list (x):
   return [line[i:i+x] for i in range(0, len(line), x)]

list = split_list(150)

zero_list = [(y,y.count('0')) for y in list]
smallest = float('inf')
for pair in zero_list:
    if pair[1] < smallest:
        smallest = pair[1]
        layer = pair[0]
numbers = layer.count('1')*layer.count('2')
print(numbers)

picture = ''
for i in range (150):
    for layer in list:
        if layer[i] != '2':
            if layer[i] == '0':
                picture += ' '
            else:
                picture += '\u220e'
            break
    if i % 25 == 24:
        picture += '\n'
print(picture)