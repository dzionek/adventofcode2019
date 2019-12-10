def run_computer(data, phases):
    a, b, c, d, e = phases[0], phases[1], phases[2], phases[3], phases[4]
    a_output = run_program(data, [a, 0])
    b_output = run_program(data, [b, a_output])
    c_output = run_program(data, [c, b_output])
    d_output = run_program(data, [d, c_output])
    e_output = run_program(data, [e, d_output])
    return e_output


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


def run_program(data, list_of_inputs):
    i = 0
    input_number = 0
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
            data[data[i + 1]] = list_of_inputs[input_number]
            input_number += 1
            i += 2
        elif opcode == 4:
            output = jump_one(data, i, mode_first)
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
