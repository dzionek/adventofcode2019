file = open("inputs/13.txt", "r")
line = file.readline()
file.close()

data = list(map(int, line.split(',')))
blank = list(data)


def jump_one(data, i, mode, base):
    if mode == 0:
        return data[data[i + 1]]
    elif mode == 1:
        return data[i + 1]
    else:
        return data[base + data[i + 1]]


def jump_two(data, i, mode, base):
    if mode == 0:
        return data[data[i + 2]]
    elif mode == 1:
        return data[i + 2]
    else:
        return data[base + data[i + 2]]


def write(pointer, mode, base):
    if mode == 0:
        return pointer
    else:
        return pointer + base


def run_computer(data,list_of_inputs):
    base = 0
    output = []
    data = data + ([0] * 1000000)
    for parameter in list_of_inputs:
        i = 0

        while data[i] != 99:
            if data[i] > 99:
                long_code = str(data[i])

                if len(long_code) == 3:
                    long_code = "00" + long_code
                elif len(long_code) == 4:
                    long_code = "0" + long_code

                if long_code[3] == "0":
                    opcode = int(long_code[4])
                else:
                    opcode = int(long_code[3:])

                mode_first = int(long_code[2])
                mode_second = int(long_code[1])
                mode_third = int(long_code[0])

            else:
                opcode = data[i]
                mode_first, mode_second, mode_third = 0, 0, 0

            if opcode == 1:
                data[write(data[i + 3], mode_third, base)] = jump_one(data, i, mode_first, base) + jump_two(data, i, mode_second, base)
                i += 4
            elif opcode == 2:
                data[write(data[i + 3], mode_third, base)] = jump_one(data, i, mode_first, base) * jump_two(data, i, mode_second, base)
                i += 4
            elif opcode == 3:
                data[write(data[i + 1], mode_first, base)] = parameter
                i += 2
            elif opcode == 4:
                list.append(output, jump_one(data, i, mode_first, base))
                i += 2
            elif opcode == 5:
                if jump_one(data, i, mode_first, base) != 0:
                    i = jump_two(data, i, mode_second, base)
                else:
                    i += 3
            elif opcode == 6:
                if jump_one(data, i, mode_first, base) == 0:
                    i = jump_two(data, i, mode_second, base)
                else:
                    i += 3
            elif opcode == 7:
                if jump_one(data, i, mode_first, base) < jump_two(data, i, mode_second, base):
                    data[write(data[i + 3], mode_third, base)] = 1
                else:
                    data[write(data[i + 3], mode_third, base)] = 0
                i += 4
            elif opcode == 8:
                if jump_one(data, i, mode_first, base) == jump_two(data, i, mode_second, base):
                    data[write(data[i + 3], mode_third, base)] = 1
                else:
                    data[write(data[i + 3], mode_third, base)] = 0
                i += 4
            elif opcode == 9:
                base += jump_one(data, i, mode_first, base)
                i += 2
    return output

grid = []

for y in range(20):
    row = []
    for x in range(40):
        list.append(row, ' ')
    list.append(grid, row)

i = 0
instruction = run_computer(data, [0])
blocks = 0

while i < len(instruction):
    x = instruction[i]
    y = instruction[i+1]
    id = instruction[i+2]

    if id == 0:
        grid[y][x] = 'e'
    elif id == 1:
        grid[y][x] = 'w'
    elif id == 2:
        grid[y][x] = 'b'
        blocks += 1
    elif id == 3:
        grid[y][x] = 'h'
    elif id == 4:
        grid[y][x] = 'X'
    else:
        print('Error while processing the instruction')

    i += 3

print(blocks)

for y in grid:
    row = ''
    for x in y:
        row += x
    print(row)