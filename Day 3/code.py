file = open("input.txt","r")
lines = file.readlines()

def points(commands):
    wire = set()
    x = 0
    y = 0
    for command in commands:
       length = int(command[1:])
       if command[0] == "R":
            for i in range (length):
                wire.add((x+i+1,y))
            x += length
       if command[0] == "L":
            for i in range (length):
                wire.add((x-i-1,y))
            x -= length
       if command[0] == "U":
            for i in range (length):
                 wire.add((x,y+i+1))
            y += length
       if command[0] == "D":
            for i in range (length):
                 wire.add((x,y-i-1))
            y -= length
    return wire

wire_one = set()
command_one = [x.replace('\n','') for x in (lines[0]).split(',')]
wire_one = points(command_one)
wire_two = set()
command_two = [x.replace('\n','') for x in (lines[1]).split(',')]
wire_two = points(command_two)

intersections = wire_one & wire_two

minimum = abs((intersections.pop())[0]) + abs((intersections.pop())[1])

for point in intersections:
    distance = abs(point[0]) + abs(point[1])
    if distance < minimum:
        minimum = distance
        
print(minimum)

def findPaths(commands):
    x = 0
    y = 0
    k = 0
    paths = set()
    current = (0,0)
    for command in commands:
       length = int(command[1:])
       if command[0] == "R":
            for i in range (length):
               current=(x+i+1,y)
               k += 1
               if current in intersections:
                   paths.add((current,k))
            x += length
       if command[0] == "L":
            for i in range (length):
               current = (x-i-1,y)
               k += 1
               if current in intersections:
                   paths.add((current,k))
            x -= length
       if command[0] == "U":
            for i in range (length):
               current = (x,y+i+1)
               k += 1
               if current in intersections:
                   paths.add((current,k))
            y += length
       if command[0] == "D":
            for i in range (length):
               current = (x,y-i-1)
               k += 1
               if current in intersections:
                   paths.add((current,k))
            y -= length
        
    return paths
paths_one = findPaths(command_one)
paths_two = findPaths(command_two)

minimal_path = float("inf")

for path_one in paths_one:
    for path_two in paths_two:
        if path_one[0] == path_two[0]:
            path = path_one[1] + path_two[1]
            if path < minimal_path:
                minimal_path = path
print(minimal_path)