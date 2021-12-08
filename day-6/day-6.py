# Read File

def read_file(filename):
    """
    Reads in Test File line by line and adds to list

    Args:
        filename (string): Filename/Filepath

    Returns:
        list{list}: List of lanternfish
    """
    with open(filename, 'r') as f:
        line = f.readline()
        return [int(x) for x in line.split(',')]

# Part 1


def simulate_lanternfish_growth(lanternfish, days):
    for _ in range(1, days+1):
        for i, x in enumerate(lanternfish):
            if x == 0:
                lanternfish[i] = 6
                lanternfish.append(9)
            else:
                lanternfish[i] -= 1
    return len(lanternfish)


# Part 2
input_lanternfish = read_file("input.txt")
test_lanternfish = read_file("test.txt")


solution_part_1 = simulate_lanternfish_growth(test_lanternfish, days=80)
#solution_part_2 = simulate_lanternfish_growth(test_lanternfish, days=256)


print(f"Solution (Part 1): {solution_part_1}")
#print(f"Solution (Part 2): {solution_part_2}")
