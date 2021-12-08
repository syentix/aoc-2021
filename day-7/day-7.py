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
            stripped = line.strip()
            points = stripped.split(' -> ')
            [a, b] = points[0].split(',')
            [x, y] = points[1].split(',')
            point1 = Point(int(a), int(b))
            point2 = Point(int(x), int(y))
            lines.append(Line(point1, point2))
    return lines

# Part 1


# Part 2
input_lines = read_file("input.txt")
test_lines = read_file("test.txt")

#solution_part_1 = count_intersections(input_lines)


#print(f"Solution (Part 1): {solution_part_1}")
