def read_input(input_file):
    with open(input_file, 'r') as f:
        return [i for i in f.readlines()]

def _compute(input_list):
    floors = [0]
    for i in input_list:
        floors.append(floors[-1] + (1 if i == "(" else -1))
    return floors

def compute_floor(input_list):
    return _compute(input_list)[-1]

def compute_basement(input_list):
    return _compute(input_list).index(-1)