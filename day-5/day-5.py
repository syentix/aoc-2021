from dataclasses import dataclass
from collections import Counter
# Read File


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Line:
    a: Point
    b: Point

    def createSeries(self):
        if self.a.x == self.b.x:
            start = self.a.y if self.a.y < self.b.y else self.b.y
            stop = self.a.y if self.a.y > self.b.y else self.b.y
            return [(self.a.x, y) for y in range(start, stop+1)]
        elif self.a.y == self.b.y:
            start = self.a.x if self.a.x < self.b.x else self.b.x
            stop = self.a.x if self.a.x > self.b.x else self.b.x
            return [(x, self.a.y) for x in range(start, stop+1)]


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


def create_all_points(lines):
    result = []
    for line in lines:
        series = line.createSeries()
        if series != None:
            result += series
    return result


def count_intersections(lines) -> int:
    result = 0
    points = create_all_points(lines)
    apperances = Counter(points)
    for val in apperances.values():
        if val >= 2:
            result += 1
    return result


# Part 2

input_lines = read_file("input.txt")
test_lines = read_file("test.txt")

solution_part_1 = count_intersections(input_lines)


print(f"Solution (Part 1): {solution_part_1}")
