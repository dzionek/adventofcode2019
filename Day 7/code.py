from itertools import permutations
import computer
import computer2

file = open("input.txt","r")
line = file.readline()
file.close()

data = list(map(int, line.split(',')))

biggest = 0

for permutation in permutations(range(5)):
    output = computer.run_computer(data,permutation)
    if output > biggest:
        biggest = output

print(biggest)

biggest = 0

for permutation in permutations(range(5,10)):
    output = computer2.run_computer(data,permutation)
    if output > biggest:
        biggest = output

print(biggest)