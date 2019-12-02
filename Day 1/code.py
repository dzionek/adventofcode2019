import math

total_fuel_first = 0
total_fuel_second = 0

def countFuel(mass):
    fuel = math.floor(mass/3) - 2
    return fuel

def countFuelSecond(mass, fuel):
    step = math.floor(mass/3) - 2
    if step <= 0:
        return fuel
    else:
        fuel += step
        return countFuelSecond(step, fuel)

file = open("input.txt","r")
lines = file.readlines()

for line in lines:
    mass = int(line)
    total_fuel_first += countFuel(mass)
    total_fuel_second += countFuelSecond(mass, 0)
    
file.close()

print(total_fuel_first)
print(total_fuel_second)