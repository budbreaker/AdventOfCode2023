from enum import Enum


class State(Enum):
    INITIAL = 1
    FIRST_DIGIT = 2
    NEXT_DIGIT = 3
    READ = 4


def check_touching(i, j):
    is_touching = False
    for k in range(-1, 2):
        for l in range(-1, 2):
            if i + k < 0 or i + k >= height or j + l < 0 or j + l >= width:
                continue
            if is_special(lines[i + k][j + l]):
                is_touching = True
                break
        if is_touching:
            break
    return is_touching


def is_special(c):
    return c in "!@#$%^&*()-+?_=,<>/"


with (open("input.txt") as f):
    lines = f.readlines()
    height = len(lines)
    width = len(lines[0]) - 1
    state = State.INITIAL
    num = []
    summ = 0
    touching = False
    for i in range(height):
        lines[i] = lines[i].strip()
        for j in range(width):
            c = lines[i][j]
            if state == State.INITIAL:
                if c.isnumeric():
                    state = State.FIRST_DIGIT
                    num = [c]
                    touching = check_touching(i, j)
                else:
                    state = State.READ
            elif state == State.FIRST_DIGIT:
                if c.isnumeric():
                    num.append(c)
                    state = State.NEXT_DIGIT
                    if not touching:
                        touching = check_touching(i, j)
                else:
                    if touching:
                        summ += int(''.join(num))
                    state = State.READ
            elif state == State.NEXT_DIGIT:
                if c.isnumeric():
                    num.append(c)
                    if not touching:
                        touching = check_touching(i, j)
                else:
                    if touching:
                        summ += int(''.join(num))
                    state = State.READ
            elif state == State.READ:
                if c.isnumeric():
                    state = State.FIRST_DIGIT
                    num = [c]
                    touching = check_touching(i, j)
                else:
                    pass

print(summ)
