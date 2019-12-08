file = open("input.txt", "r")
line = file.readline()
file.close()

data = list(map(int, line.split(',')))
blank = list(data)


def jump_one(data, i, mode):
    if mode == 0:
        return data[data[i + 1]]
    else:
        return data[i + 1]


def jump_two(data, i, mode):
    if mode == 0:
        return data[data[i + 2]]
    else:
        return data[i + 2]


def run_computer(list_of_inputs):
    output = []
    for parameter in list_of_inputs:
        i = 0
        data = list(blank)  # reset the memory

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
                # mode_third = int(long_code[0]) unnecessary, but mentioned in the question

            else:
                opcode = data[i]
                mode_first, mode_second, mode_third = 0, 0, 0

            if opcode == 1:
                data[data[i + 3]] = jump_one(data, i, mode_first) + jump_two(data, i, mode_second)
                i += 4
            elif opcode == 2:
                data[data[i + 3]] = jump_one(data, i, mode_first) * jump_two(data, i, mode_second)
                i += 4
            elif opcode == 3:
                data[data[i + 1]] = parameter
                i += 2
            elif opcode == 4:
                list.append(output, jump_one(data, i, mode_first))
                i += 2
            elif opcode == 5:
                if jump_one(data, i, mode_first) != 0:
                    i = jump_two(data, i, mode_second)
                else:
                    i += 3
            elif opcode == 6:
                if jump_one(data, i, mode_first) == 0:
                    i = jump_two(data, i, mode_second)
                else:
                    i += 3
            elif opcode == 7:
                if jump_one(data, i, mode_first) < jump_two(data, i, mode_second):
                    data[data[i + 3]] = 1
                else:
                    data[data[i + 3]] = 0
                i += 4
            elif opcode == 8:
                if jump_one(data, i, mode_first) == jump_two(data, i, mode_second):
                    data[data[i + 3]] = 1
                else:
                    data[data[i + 3]] = 0
                i += 4
    return output


print(run_computer((1, 5)))
