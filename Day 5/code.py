file = open("input.txt","r")
line = file.readline()

data = list(map(int, line.split(',')))
i = 0
while data[i] != 99:
    if data[i] > 99:
        long_code = str(data[i])
        if len(long_code) == 3:
            long_code = "00" + long_code
        else:
            long_code = "0" + long_code
        if long_code[3] == "0":
            opcode = int(long_code[4])
        else:
            opcode = int(long_code[3:])
        mode_one = int(long_code[2])
        mode_second = int(long_code[1])
        mode_third = int(long_code[0])
        if opcode == 1:
            if mode_third == 0:
                if mode_one == 0 and mode_second == 0:
                    data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
                elif mode_one == 0 and mode_second == 1:
                    data[data[i+3]] = data[data[i+1]] + data[i+2]
                elif mode_one == 1 and mode_second == 0:
                    data[data[i+3]] = data[i+1] + data[data[i+2]]
                elif mode_one == 1 and mode_second == 1:
                    data[data[i+3]] = data[i+1] + data[i+2]
            else:
                if mode_one == 0 and mode_second == 0:
                    data[i+3] = data[data[i+1]] + data[data[i+2]]
                elif mode_one == 0 and mode_second == 1:
                    data[i+3] = data[data[i+1]] + data[i+2]
                elif mode_one == 1 and mode_second == 0:
                    data[i+3] = data[i+1] + data[data[i+2]]
                elif mode_one == 1 and mode_second == 1:
                    data[i+3] = data[i+1] + data[i+2]
            i +=4
        elif opcode == 2:
            if mode_third == 0:
                if mode_one == 0 and mode_second == 0:
                    data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
                elif mode_one == 0 and mode_second == 1:
                    data[data[i+3]] = data[data[i+1]] * data[i+2]
                elif mode_one == 1 and mode_second == 0:
                    data[data[i+3]] = data[i+1] * data[data[i+2]]
                elif mode_one == 1 and mode_second == 1:
                    data[data[i+3]] = data[i+1] * data[i+2]
            else:
                if mode_one == 0 and mode_second == 0:
                    data[i+3] = data[data[i+1]] * data[data[i+2]]
                elif mode_one == 0 and mode_second == 1:
                    data[i+3] = data[data[i+1]] * data[i+2]
                elif mode_one == 1 and mode_second == 0:
                    data[i+3] = data[i+1] * data[data[i+2]]
                elif mode_one == 1 and mode_second == 1:
                    data[i+3] = data[i+1] * data[i+2]
            i +=4
        elif opcode == 4:
            if mode_one == 0:
                print(data[data[i+1]])
            else:
                print(data[i+1])
            i += 2
        elif opcode == 5:
            if mode_one == 0:
                if data[data[i+1]] !=0:
                    if mode_second == 0:
                        i = data[data[i+2]] 
                    else:
                        i = data[i+2]
                else:
                    i += 3
            else:
                if data[i+1] !=0:
                    if mode_second == 0:
                        i = data[data[i+2]] 
                    else:
                        i = data[i+2]
                else:
                    i += 3
        elif opcode == 6:
            if mode_one == 0:
                if data[data[i+1]] == 0:
                    if mode_second == 0:
                        i = data[data[i+2]] 
                    else:
                        i = data[i+2]
                else:
                    i += 3
            else:
                if data[i+1] == 0:
                    if mode_second == 0:
                        i = data[data[i+2]] 
                    else:
                        i = data[i+2]
                else:
                    i += 3
        elif opcode == 7:
            if mode_one == 0:
                if mode_second == 0:
                    if data[data[i+1]] < data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[data[i+1]] < data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            else:
                if mode_second == 0:
                    if data[i+1] < data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[i+1] < data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            i += 4
        elif opcode == 8:
            if mode_one == 0:
                if mode_second == 0:
                    if data[data[i+1]] == data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[data[i+1]] == data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            else:
                if mode_second == 0:
                    if data[i+1] == data[data[i+2]]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
                else:
                    if data[i+1] == data[i+2]:
                        data[data[i+3]] = 1
                    else:
                        data[data[i+3]] = 0
            i += 4
                        
        else:    
            print(i)
            print(data[:i])
    elif data[i] == 1:
        data[data[i+3]] = data[data[i+1]] + data[data[i+2]]
        i += 4
    elif data[i] == 2:
        data[data[i+3]] = data[data[i+1]] * data[data[i+2]]
        i += 4
    elif data[i] == 3:
        take_input = int(input("Give input: "))
        data[data[i+1]]= take_input
        i += 2
    elif data[i] == 4:
        print(data[data[i+1]])
        i += 2
    elif data[i] == 5:
        if data[data[i+1]] !=0:
            i = data[data[i+2]]
        else:
            i += 3
    elif data[i] == 6:
        if data[data[i+1]] == 0:
            i = data[data[i+2]]
        else:
            i += 3
    elif data[i] == 7:
        if data[data[i+1]] < data[data[i+2]]:
            data[data[i+3]] = 1
        else:
            data[data[i+3]] = 0
        i += 4
    elif data[i] == 8:
        if data[data[i+1]] == data[data[i+2]]:
            data[data[i+3]] = 1
        else:
            data[data[i+3]] = 0
        i += 4
file.close()