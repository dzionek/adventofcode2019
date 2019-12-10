from itertools import permutations
import day07_part1
import day07_part2

file = open("inputs/07.txt","r")
line = file.readline()
file.close()

data = list(map(int, line.split(',')))

biggest = 0

for permutation in permutations(range(5)):
    output = day07_part1.run_computer(data,permutation)
    if output > biggest:
        biggest = output

print(biggest)

biggest = 0

for permutation in permutations(range(5,10)):
    output = day07_part2.run_computer(data,permutation)
    if output > biggest:
        biggest = output

print(biggest)
