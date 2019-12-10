file = open("inputs/02.txt","r")
line = file.readline()
file.close()

input = list(map(int, line.split(',')))
blank = list(input)

i = 0
while input[i] != 99:
    if input[i] == 1:
        input[input[i+3]] = input[input[i+1]] + input[input[i+2]]

    elif input[i] == 2:
        input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
    i += 4
    
print(input[0])

for noun in range (100):
    for verb in range (100):
        input = list(blank)
        i = 0
        input[1] = noun
        input [2] = verb
        while input[i] != 99:
            if input[i] == 1:
                input[input[i+3]] = input[input[i+1]] + input[input[i+2]]

            elif input[i] == 2:
                input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
            i += 4
        if input[0] == 19690720:
            break
    if input[0] == 19690720:
        break
    
print(100*noun + verb)
