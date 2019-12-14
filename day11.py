file = open("inputs/11.txt", "r")
line = file.readline()
file.close()

data = list(map(int, line.split(',')))

def robot(output, area, positions, current_position, painted):

    if output[0] == 0:
        area[current_position[1][0]][current_position[1][1]] = ' ' # black
    else:
        area[current_position[1][0]][current_position[1][1]] = '\u220e' # white

    painted.add((current_position[1][0], current_position[1][1]))

    if output[1] == 0: #turn left
        current_position = ((current_position[0] + 1) % 4, current_position[1])
    else: #turn right
        current_position = ((current_position[0] - 1) % 4, current_position[1])

    if positions[current_position[0]] == 'right':
        current_position = (current_position[0], (current_position[1][0], current_position[1][1] + 1))
    elif positions[current_position[0]] == 'left':
        current_position = (current_position[0], (current_position[1][0], current_position[1][1] - 1))
    elif positions[current_position[0]] == 'up':
        current_position = (current_position[0], (current_position[1][0] - 1, current_position[1][1]))
    elif positions[current_position[0]] == 'down':
        current_position = (current_position[0], (current_position[1][0] + 1, current_position[1][1]))
    else:
        print('Error with going forward')


    if area[current_position[1][0]][current_position[1][1]] == ' ':
        return (0, area, positions, current_position, painted)
    else:
        return (1, area, positions, current_position, painted)



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


def run_computer(data, parameter):
    base = 0
    output = []
    data = data + ([0] * 1000000)
    i = 0

    area = []
    for y in range(101):
        row = []
        for x in range(71):
            list.append(row, ' ')
        list.append(area, row)

    positions = ['up', 'left', 'down', 'right']
    current_position = (0, (20, 20))
    painted = set()

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
            if len(output) == 2:
                robot_output = robot(output, area, positions, current_position, painted)
                parameter, area, positions, current_position, painted = robot_output[0], robot_output[1], robot_output[2], robot_output[3], robot_output[4]
                output = []
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
    return (area, painted)


def part_one(data):
    return len(run_computer(data, 0)[1])


def part_two(data):
    area = run_computer(data, 1)[0]
    text = ''
    for y in range(len(area)):
        line = ''
        for x in range(21, len(area[y])):
            line += area[y][x]
        if '\u220e' in line:
            text += line + '\n'
    return text

print(part_one(data))
print(part_two(data))