from types import FunctionType


def read_input(input_file):
    with open(input_file, 'r') as f:
        return [i for i in f.readlines()]


def compute_paper_needed(l: int, w: int, h: int):
    return 2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])

def compute_ribbon_needed(l:int, w:int, h:int):
    return min([2*l + 2*w, 2*w + 2*h, 2*h + 2*l]) + l * w * h


def total_paper_needed(input: list[str]):
    return _compute_total(input, compute_paper_needed)

def total_ribbon_needed(input: list[str]):
    return _compute_total(input, compute_ribbon_needed)

def _compute_total(input:list[str], func: FunctionType):
    total = 0
    for g in input:
        l, w, h = [int(i) for i in g.split('x')]
        total += func(l, w, h)
    return total
