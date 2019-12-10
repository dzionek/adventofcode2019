def run_computer(data, phases):
    a, b, c, d, e = phases[0], phases[1], phases[2], phases[3], phases[4]
    pointer_a, pointer_b, pointer_c, pointer_d, pointer_e = 0, 0, 0, 0, 0
    e_output = 0
    data_a, data_b, data_c, data_d, data_e = list(data), list(data), list(data), list(data), list(data)
    initial = True
    while True:

        if initial:
            a_second_input = [a, e_output]
        else:
            a_second_input = [e_output]

        a_run = run_program(data_a, a_second_input, pointer_a)

        if a_run is None:
            return e_output

        a_output, data_a, pointer_a = a_run[0], a_run[1], a_run[2]

        if initial:
            b_second_input = [b, a_output]
        else:
            b_second_input = [a_output]

        b_run = run_program(data_b, b_second_input, pointer_b)

        if b_run is None:
            return e_output

        b_output, data_b, pointer_b = b_run[0], b_run[1], b_run[2]

        if initial:
            c_second_input = [c, b_output]
        else:
            c_second_input = [b_output]

        c_run = run_program(data_c, c_second_input, pointer_c)

        if c_run is None:
            return e_output

        c_output, data_c, pointer_c = c_run[0], c_run[1], c_run[2]

        if initial:
            d_second_input = [d, c_output]
        else:
            d_second_input = [c_output]

        d_run = run_program(data_d, d_second_input, pointer_d)

        if d_run is None:
            return e_output

        d_output, data_d, pointer_d = d_run[0], d_run[1], d_run[2]

        if initial:
            e_second_input = [e, d_output]
            initial = False
        else:
            e_second_input = [d_output]

        e_run = run_program(data_e, e_second_input, pointer_e)

        if e_run is None:
            return e_output

        e_output, data_e, pointer_e = e_run[0], e_run[1], e_run[2]


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


def run_program(data, list_of_inputs, i):
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
            pointer = i
            return (output, data, pointer)
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
