import math


def count_fuel(mass):
    fuel = math.floor(mass / 3) - 2
    return fuel


def count_fuel_second(mass, fuel):
    step = count_fuel(mass)
    if step <= 0:
        return fuel
    else:
        fuel += step
        return count_fuel_second(step, fuel)


file = open("input.txt", "r")
lines = file.readlines()
file.close()

total_fuel_first = 0
total_fuel_second = 0

for line in lines:
    mass = int(line)
    total_fuel_first += count_fuel(mass)
    total_fuel_second += count_fuel_second(mass, 0)

print(total_fuel_first)
print(total_fuel_second)
