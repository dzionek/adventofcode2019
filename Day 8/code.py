file = open("input.txt","r")
line = file.readline()
file.close()
line = line.strip('\n')

WIDTH = 25
HEIGHT = 6
PIXELS = WIDTH * HEIGHT

data = [line[i:i+PIXELS] for i in range(0, len(line), PIXELS)]

zero_list = [(y,y.count('0')) for y in data]

smallest = float('inf')

for pair in zero_list:
    if pair[1] < smallest:
        smallest = pair[1]
        layer = pair[0]
numbers = layer.count('1') * layer.count('2')

print(numbers)

picture = ''

for i in range (PIXELS):
    for layer in data:
        if layer[i] != '2':
            if layer[i] == '0':
                picture += ' '
            else:
                picture += '\u220e'
            break
    if i % WIDTH == WIDTH-1:
        picture += '\n'

print(picture)