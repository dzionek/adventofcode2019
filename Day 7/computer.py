phase_a = 0
phase_b = 0
phase_c = 0
phase_d = 0
phase_e = 0
input = 0
count_inputs = 0
last_output = 0
current_phase = 0

def nextPhase(n):
	global current_phase
	global last_output
	global input
	last_output = n
	if current_phase == phase_a:
		current_phase = phase_b
	elif current_phase == phase_b:
		current_phase = phase_c
	elif current_phase == phase_c:
		current_phase = phase_d
	elif current_phase == phase_d:
		current_phase = phase_e
	input = current_phase
	return None

def nextInput():
	global phase_a
	global phase_b
	global phase_c
	global phase_d
	global phase_e
	global input
	global count_inputs
	global last_output
	global current_phase
	if count_inputs % 2 == 1:
		input = last_output
	count_inputs += 1
	return None

def runComputer(data,permutation):
	global current_phase
	global phase_a
	global phase_b
	global phase_c
	global phase_d
	global phase_e
	global input
	global count_inputs
	global last_output
	phase_a = permutation[0]
	phase_b = permutation[1]
	phase_c = permutation[2]
	phase_d = permutation[3]
	phase_e = permutation[4]
	input = phase_a
	current_phase = phase_a
	count_inputs = 1
	last_output = 0
	while count_inputs<11:
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
							data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
						elif mode_one == 0 and mode_second == 1:
							data[data[i + 3]] = data[data[i + 1]] + data[i + 2]
						elif mode_one == 1 and mode_second == 0:
							data[data[i + 3]] = data[i + 1] + data[data[i + 2]]
						elif mode_one == 1 and mode_second == 1:
							data[data[i + 3]] = data[i + 1] + data[i + 2]
					else:
						if mode_one == 0 and mode_second == 0:
							data[i + 3] = data[data[i + 1]] + data[data[i + 2]]
						elif mode_one == 0 and mode_second == 1:
							data[i + 3] = data[data[i + 1]] + data[i + 2]
						elif mode_one == 1 and mode_second == 0:
							data[i + 3] = data[i + 1] + data[data[i + 2]]
						elif mode_one == 1 and mode_second == 1:
							data[i + 3] = data[i + 1] + data[i + 2]
					i += 4
				elif opcode == 2:
					if mode_third == 0:
						if mode_one == 0 and mode_second == 0:
							data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
						elif mode_one == 0 and mode_second == 1:
							data[data[i + 3]] = data[data[i + 1]] * data[i + 2]
						elif mode_one == 1 and mode_second == 0:
							data[data[i + 3]] = data[i + 1] * data[data[i + 2]]
						elif mode_one == 1 and mode_second == 1:
							data[data[i + 3]] = data[i + 1] * data[i + 2]
					else:
						if mode_one == 0 and mode_second == 0:
							data[i + 3] = data[data[i + 1]] * data[data[i + 2]]
						elif mode_one == 0 and mode_second == 1:
							data[i + 3] = data[data[i + 1]] * data[i + 2]
						elif mode_one == 1 and mode_second == 0:
							data[i + 3] = data[i + 1] * data[data[i + 2]]
						elif mode_one == 1 and mode_second == 1:
							data[i + 3] = data[i + 1] * data[i + 2]
					i += 4
				elif opcode == 4:
					if mode_one == 0:
						nextPhase(data[data[i + 1]])
					else:
						nextPhase(data[data[i + 1]])
					i += 2
				elif opcode == 5:
					if mode_one == 0:
						if data[data[i + 1]] != 0:
							if mode_second == 0:
								i = data[data[i + 2]]
							else:
								i = data[i + 2]
						else:
							i += 3
					else:
						if data[i + 1] != 0:
							if mode_second == 0:
								i = data[data[i + 2]]
							else:
								i = data[i + 2]
						else:
							i += 3
				elif opcode == 6:
					if mode_one == 0:
						if data[data[i + 1]] == 0:
							if mode_second == 0:
								i = data[data[i + 2]]
							else:
								i = data[i + 2]
						else:
							i += 3
					else:
						if data[i + 1] == 0:
							if mode_second == 0:
								i = data[data[i + 2]]
							else:
								i = data[i + 2]
						else:
							i += 3
				elif opcode == 7:
					if mode_one == 0:
						if mode_second == 0:
							if data[data[i + 1]] < data[data[i + 2]]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
						else:
							if data[data[i + 1]] < data[i + 2]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
					else:
						if mode_second == 0:
							if data[i + 1] < data[data[i + 2]]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
						else:
							if data[i + 1] < data[i + 2]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
					i += 4
				elif opcode == 8:
					if mode_one == 0:
						if mode_second == 0:
							if data[data[i + 1]] == data[data[i + 2]]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
						else:
							if data[data[i + 1]] == data[i + 2]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
					else:
						if mode_second == 0:
							if data[i + 1] == data[data[i + 2]]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
						else:
							if data[i + 1] == data[i + 2]:
								data[data[i + 3]] = 1
							else:
								data[data[i + 3]] = 0
					i += 4

				else:
					print(i)
					print(data[:i])
			elif data[i] == 1:
				data[data[i + 3]] = data[data[i + 1]] + data[data[i + 2]]
				i += 4
			elif data[i] == 2:
				data[data[i + 3]] = data[data[i + 1]] * data[data[i + 2]]
				i += 4
			elif data[i] == 3:
				data[data[i + 1]] = input
				nextInput()
				i += 2
			elif data[i] == 4:
				nextPhase(data[data[i + 1]])
				i += 2
			elif data[i] == 5:
				if data[data[i + 1]] != 0:
					i = data[data[i + 2]]
				else:
					i += 3
			elif data[i] == 6:
				if data[data[i + 1]] == 0:
					i = data[data[i + 2]]
				else:
					i += 3
			elif data[i] == 7:
				if data[data[i + 1]] < data[data[i + 2]]:
					data[data[i + 3]] = 1
				else:
					data[data[i + 3]] = 0
				i += 4
			elif data[i] == 8:
				if data[data[i + 1]] == data[data[i + 2]]:
					data[data[i + 3]] = 1
				else:
					data[data[i + 3]] = 0
				i += 4
	return last_output