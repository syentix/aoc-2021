def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list: List of depths
    """
    input_arr = []
    with open(filename, 'r') as f:
        for line in f:
            input_arr.append(int(line.strip()))
    return input_arr

# Part 1


def find_increases(depths):
    """
    Adds up all increases in depths.

    Args:
        depths (list{int}): List of all depths measured

    Returns:
        int: Number of increases
    """
    increases = 0
    for i, depth in enumerate(depths):
        if i == 0:
            continue
        # else
        if depth > depths[i - 1]:
            increases += 1
    return increases


def find_sum_measurements_increases(depths):
    increases = 0
    for i in range(len(depths)):
        a = sum(depths[i:i+3])
        b = sum(depths[i+1:i+1+3])
        if b > a:
            increases += 1
    return increases


input_arr = read_file("input.txt")
test_arr = read_file("test.txt")
solution_part_1 = find_increases(input_arr)
solution_part_2 = find_sum_measurements_increases(input_arr)

print(f"Number of increases (Part 1): {solution_part_1}")
print(f"Number of sum increases (Part 2): {solution_part_2}")
