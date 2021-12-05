def read_input(input_file):
    with open(input_file, 'r') as f:
        return [i for i in f.readlines()]


def compute_houses_visited(directions: str):
    houses = {(0, 0)}
    houses.update(_compute_houses(directions))
    return len(houses)

def compute_houses_visited_with_robot(directions: str):
    houses = {(0, 0)}
    houses.update(_compute_houses([s for k, s in enumerate(directions) if k % 2 == 0]))
    houses.update(_compute_houses([s for k, s in enumerate(directions) if k % 2 != 0]))
    return len(houses)

def _compute_houses(directions: str):
    x, y = 0, 0
    houses = set()
    for direction in directions:
        match direction:
            case '>':
                x += 1
            case '<':
                x -= 1
            case '^':
                y += 1
            case 'v':
                y -= 1
        houses.add((x, y))
    return houses
