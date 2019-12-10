import math

file = open("inputs/10.txt","r")
lines = [line.strip('\n') for line in file.readlines()]
file.close()

asteroids = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            asteroids.add((x,y))


def angle(a,b):
    return math.atan2(b[1]-a[1], b[0]-a[0])

def sign(a):
    if a > 0:
        return 1
    elif a == 0:
        return  0
    else:
        return -1


def dist(a,b):
    return math.sqrt((b[1] - a[1])**2 + (b[0] - a[0])**2)


def sort(lst):
    collected = set()
    for (a,b,c) in lst:
        collected.add(b)
    slope_points = []
    for slope in collected:
        same_slope_list = [(a,b,c) for (a,b,c) in lst if b == slope]
        list.append(slope_points, _minimum(same_slope_list))
    return [(b,c) for (a,b,c) in slope_points]


def _minimum(lst):
    return min(lst, key=lambda t: t[0])


def make_sequence(lst):
    lst = [sublst[1] for sublst in sorted(lst)]
    return lst


biggest = 0

for a in asteroids:
    first_quadrant = sort([(dist(a, b), angle(a, b), b) for b in asteroids if b[0] > a[0] and b[1] < a[1]])
    second_quadrant = sort([(dist(a, b), angle(a, b), b) for b in asteroids if b[0] > a[0] and b[1] > a[1]])
    third_quadrant = sort([(dist(a, b), angle(a, b), b) for b in asteroids if b[0] < a[0] and b[1] > a[1]])
    fourth_quadrant = sort([(dist(a, a), angle(a, b), b) for b in asteroids if b[0] < a[0] and b[1] < a[1]])

    x_fixed_y_above = sort([(dist(a, b), sign(b[1] - a[1]), b) for b in asteroids if b[0] == a[0] and b[1] < a[1]])
    x_fixed_y_below = sort([(dist(a, b), sign(b[1] - a[1]), b) for b in asteroids if b[0] == a[0] and b[1] > a[1]])

    y_fixed_x_left = sort([(dist(a, b), sign(b[0] - a[0]), b) for b in asteroids if b[1] == a[1] and b[0] < a[0]])
    y_fixed_x_right = sort([(dist(a, b), sign(b[0] - a[0]), b) for b in asteroids if b[1] == a[1]and b[0] > a[0]])

    observed = len(first_quadrant) + len(second_quadrant) + len(third_quadrant) + len(fourth_quadrant) \
               + len(x_fixed_y_above) + len(x_fixed_y_below) + len(y_fixed_x_left) + len(y_fixed_x_right)

    if observed > biggest:
        biggest = observed
        monitoring = a
        a_first, a_second, a_third, a_fourth = first_quadrant, second_quadrant, third_quadrant, fourth_quadrant
        a_y_above, a_y_below, a_x_left, a_x_right = x_fixed_y_above, x_fixed_y_below, y_fixed_x_left, y_fixed_x_right

print(f'The point {monitoring} can detect the most - {biggest}')


sequence = list(dict.fromkeys(make_sequence(a_y_above) + make_sequence(a_first) + make_sequence(a_x_right) + make_sequence(a_second) \
           + make_sequence(a_y_below) + make_sequence(a_third) + make_sequence(a_x_left) + make_sequence(a_fourth)))

print(f'The point {sequence[199]} will be the 200th vaporized point, so {100*sequence[199][0] + sequence[199][1]}')
