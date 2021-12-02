def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list{dict}: List of commands represented by dictionaries
    """
    input_arr = []
    with open(filename, 'r') as f:
        for line in f:
            command = line.strip().split(" ")
            input_arr.append({
                "command": command[0],
                "val": int(command[1])
            })
    return input_arr

# Part 1


def calc_position(instructions):
    """
    Calculates the position of submarine after instructions.

    Args:
        instructions (list{dict}): List of all instructions.

    Returns:
        int: horizontal coordinate of submarine
        int: vertical coordinate of submarine (depth)
        int: product of both coordinates
    """
    horizontal = 0
    depth = 0
    for instruction in instructions:
        command = instruction["command"]
        val = instruction["val"]
        if command == "forward":
            horizontal += val
        elif command == "down":
            depth += val
        else:
            depth -= val
    return (horizontal, depth, horizontal * depth)

# Part 2


def calc_position_with_aim(instructions):
    """
    Calculates the position of submarine after instructions with aim.

    Args:
        instructions (list{dict}): List of all instructions.

    Returns:
        int: horizontal coordinate of submarine
        int: vertical coordinate of submarine (depth)
        int: product of both coordinates
    """
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        command = instruction["command"]
        val = instruction["val"]
        if command == "forward":
            horizontal += val
            depth += (aim * val)
        elif command == "down":
            aim += val
        else:
            aim -= val
    return (horizontal, depth, horizontal * depth)


input_arr = read_file("input.txt")
test_arr = read_file("test.txt")

x_part1, y_part1, solution_part_1 = calc_position(input_arr)
x_part2, y_part2, solution_part_2 = calc_position_with_aim(input_arr)

print(
    f"Solution (Part 1): Horizontal: {x_part1}, Depth: {y_part1}, Product: {solution_part_1}")
print(
    f"Solution (Part 2): Horizontal: {x_part2}, Depth: {y_part2}, Product: {solution_part_2}")
