def numbers_around(i, j):
    arr = []
    to_avoid = []
    for k in range(-1, 2):
        for l in range(-1, 2):
            c = lines[i + k][j + l]
            if (i+k, j+l) in to_avoid:
                continue
            if i + k < 0 or i + k >= height or j + l < 0 or j + l >= width:
                continue
            if lines[i + k][j + l].isnumeric():
                num, a = get_number(i + k, j + l)
                arr.append(num)
                to_avoid += a
    return arr


def get_number(row, col):
    # go left from the starting point
    num = []
    avoid = []
    while col >= 0 and lines[row][col].isnumeric():
        col -= 1
    col += 1

    while col < width and lines[row][col].isnumeric():
        num.append(lines[row][col])
        avoid.append((row, col))
        col += 1

    return int(''.join(num)), avoid


with (open("input.txt") as f):
    lines = f.readlines()
    height = len(lines)
    width = len(lines[0]) - 1
    summ = 0
    for i in range(height):
        lines[i] = lines[i].strip()
        for j in range(width):
            c = lines[i][j]
            if c == "*":
                n = numbers_around(i, j)
                if len(n) == 2:
                    summ += n[0] * n[1]
print(
    summ
)