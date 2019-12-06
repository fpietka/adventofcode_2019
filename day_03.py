from math import inf
import pytest


def manhattan(point):
    return abs(point[0]) + abs(point[1])


def get_line_intersection(first, second):
    p0 = first[0]
    p1 = first[1]
    p2 = second[0]
    p3 = second[1]

    s10_x = p1[0] - p0[0]
    s10_y = p1[1] - p0[1]
    s32_x = p3[0] - p2[0]
    s32_y = p3[1] - p2[1]

    denom = s10_x * s32_y - s32_x * s10_y

    if denom == 0:
        return None  # collinear

    denom_is_positive = denom > 0

    s02_x = p0[0] - p2[0]
    s02_y = p0[1] - p2[1]

    s_numer = s10_x * s02_y - s10_y * s02_x

    if (s_numer < 0) == denom_is_positive:
        return None  # no collision

    t_numer = s32_x * s02_y - s32_y * s02_x

    if (t_numer < 0) == denom_is_positive:
        return None  # no collision

    if (s_numer > denom) == denom_is_positive or (t_numer > denom) == denom_is_positive:
        return None  # no collision

    # collision detected
    t = t_numer / denom

    intersection_point = [p0[0] + (t * s10_x), p0[1] + (t * s10_y)]
    return intersection_point


def create_route(directions):
    position = [0, 0]
    lines = []

    for direction in directions:
        current_line = [position.copy()]
        if direction[0] == 'R':
            position[1] += int(direction[1:])
            current_line.append(position.copy())
            lines.append(current_line)
        elif direction[0] == 'L':
            position[1] -= int(direction[1:])
            current_line.append(position.copy())
            lines.append(current_line)
        elif direction[0] == 'U':
            position[0] += int(direction[1:])
            current_line.append(position.copy())
            lines.append(current_line)
        elif direction[0] == 'D':
            position[0] -= int(direction[1:])
            current_line.append(position.copy())
            lines.append(current_line)

    return lines


testdata = [
    (['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
     ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83'],
     159),
    (['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53',
      'R51'],
     ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7'],
     135),
]


def check_intersect(route1, route2, closest=inf):
    for line1 in route1:
        for line2 in route2:
            intersect = get_line_intersection(line1, line2)
            if isinstance(intersect, list):
                closest = min(closest, manhattan(intersect))

    return closest


@pytest.mark.parametrize("route1,route2,expected", testdata)
def test_intersect(route1, route2, expected):
    route1 = create_route(route1)
    route2 = create_route(route2)
    assert check_intersect(route1, route2) == expected


########
# PART 1

try:
    fp = open('day_03_inputs')

    routes = []
    for line in fp:
        routes.append(create_route(line.split(',')))
    print(check_intersect(*routes))
finally:
    fp.close()
