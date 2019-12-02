from math import floor
import pytest


def get_fuel(mass):
    return floor(mass / 3) - 2


########
# PART 1

testdata = [
    (12, 2),
    (14, 2),
    (1969, 654),
    (100756, 33583),
]


@pytest.mark.parametrize("mass,expected", testdata)
def test_get_fuel(mass, expected):
    assert get_fuel(mass) == expected


total_fuel = 0

try:
    fp = open('day_01_inputs')

    for mass in fp:
        total_fuel += get_fuel(int(mass))
finally:
    fp.close()

print(total_fuel)


########
# PART 2

def get_fuel_with_mass(mass):
    total_fuel = 0
    fuel = 0
    while True:
        fuel = floor(mass / 3) - 2
        if fuel <= 0:
            break
        else:
            total_fuel += fuel
            mass = fuel

    return total_fuel


testdata = [
    (14, 2),
    (1969, 966),
    (100756, 50346),
]


@pytest.mark.parametrize("mass,expected", testdata)
def test_get_fuel_with_mass(mass, expected):
    assert get_fuel_with_mass(mass) == expected


total_fuel = 0

try:
    fp = open('day_01_inputs')

    for mass in fp:
        total_fuel += get_fuel_with_mass(int(mass))
finally:
    fp.close()

print(total_fuel)
