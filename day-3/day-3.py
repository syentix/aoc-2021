import copy


def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list{list}: List of commands represented by dictionaries
    """
    input_arr = []
    with open(filename, 'r') as f:
        for line in f:
            binary_string = line.strip()
            input_arr.append([int(x) for x in binary_string])
    return input_arr

# Part 1


def get_epsilon_and_delta(binaries):
    delta, epsilon = '', ''
    for i in range(len(binaries[0])):
        one, zero = 0, 0
        for binary in binaries:
            if binary[i] == 0:
                zero += 1
            else:
                one += 1
        if one > zero:
            delta += '1'
            epsilon += '0'
        else:
            delta += '0'
            epsilon += '1'

    return (int(delta, 2), int(epsilon, 2), (int(delta, 2) * int(epsilon, 2)))

# Part 2


def determine_val(binaries: list, o2: bool = True):
    """
    Determines the last list element where condition is true.

    Args:
        binaries (list): List of binaries
        o2 (bool, optional): Determines if to search for o2 condition or co2. Defaults to True.

    Returns:
        str: binary string of result element
    """
    result = copy.deepcopy(binaries)
    i = 0
    while i < len(binaries[0]) and len(result) > 1:
        one, zero = 0, 0
        for binary in result:
            if binary[i] == 0:
                zero += 1
            else:
                one += 1
        if o2:
            if one > zero:
                result = [x for x in result if x[i] == 1]
            elif one == zero:
                result = [x for x in result if x[i] == 1]
            else:
                result = [x for x in result if x[i] == 0]
        else:
            if one > zero:
                result = [x for x in result if x[i] == 0]
            elif one == zero:
                result = [x for x in result if x[i] == 0]
            else:
                result = [x for x in result if x[i] == 1]
        i += 1
    return ''.join([str(x) for x in result[0]])


def determine_o2_co2_vals(binaries: list):
    """
    Determines both values and the product for solution.

    Args:
        binaries (list): List of binaries from Input.

    Returns:
        int: o2 Value
        int: co2 Value
        int: Product of o2 and co2
    """
    o2 = int(determine_val(binaries), 2)
    co2 = int(determine_val(binaries, o2=False), 2)
    return (o2, co2, (o2 * co2))


input_arr = read_file("input.txt")
test_arr = read_file("test.txt")

delta, epsilon, solution_part_1 = get_epsilon_and_delta(input_arr)
o2, co2, solution_part_2 = determine_o2_co2_vals(input_arr)

print(
    f"Solution (Part 1): Delta: {delta}, Epsilon: {epsilon}, Product: {solution_part_1}")
print(f"Solution (Part 2): O2: {o2}, CO2: {co2}, Product: {solution_part_2}")
