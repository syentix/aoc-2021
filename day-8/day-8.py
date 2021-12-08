# Read File

def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list{list}: List of commands represented by dictionaries
    """
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            # Do something
            pass
    return lines

# Part 1


# Part 2


input_lines = read_file("input.txt")
test_lines = read_file("test.txt")

#solution_part_1 = count_intersections(input_lines)


#print(f"Solution (Part 1): {solution_part_1}")
