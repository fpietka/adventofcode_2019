import pytest


def is_six(digit):
    return len(str(digit)) == 6


def have_adjacent(digit):
    data = str(digit)
    for i in range(0, len(data) - 1):
        tested = data[i:i+2]
        if tested[0] == tested[1]:
            return True

    return False


def is_increasing(digit):
    data = str(digit)
    for i in range(0, len(data) - 1):
        tested = data[i:i+2]
        if int(tested[0]) > int(tested[1]):
            return False

    return True


def is_valid(digit):
    return is_six(digit) and have_adjacent(digit) and is_increasing(digit)


########
# PART 1


testdata = (
    [111111, True],
    [223450, False],
    [123789, False],
)


@pytest.mark.parametrize("digit,validity", testdata)
def test_is_valid(digit, validity):
    assert is_valid(digit) == validity


are_valid = 0
for digit in range(136760, 595730):
    if is_valid(digit):
        are_valid += 1

print(are_valid)


########
# PART 2


def have_adjacent_but_not_larger(digit):
    data = str(digit)
    for i in range(0, len(data) - 1):
        tested = data[i:i+2]
        if tested[0] == tested[1]:
            if tested[0] == data[i-1:i] or tested[0] == data[i+2:i+3]:
                pass
            else:
                return True

    return False


def is_valid_final(digit):
    return is_valid(digit) and have_adjacent_but_not_larger(digit)


testdata = (
    [112233, True],
    [123444, False],
    [111122, True],
)


@pytest.mark.parametrize("digit,validity", testdata)
def test_is_valid_final(digit, validity):
    assert is_valid_final(digit) == validity


are_valid = 0
for digit in range(136760, 595730):
    if is_valid_final(digit):
        are_valid += 1

print(are_valid)
