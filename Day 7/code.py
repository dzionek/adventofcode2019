from itertools import permutations
import computer

file = open("input.txt","r")
line = file.readline()
file.close()
data = list(map(int, line.split(',')))
biggest = 0
for permutation in permutations(range(5)):
    output = computer.runComputer(data,permutation)
    if output > biggest:
        biggest = output
print('Answer for part 1: ' + str(biggest))
print('Part 2 will be completed soon.')