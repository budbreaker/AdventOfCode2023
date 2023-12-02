map = {
    "zero": "z0ro",
    "one": "o1e",
    "two": "t2o",
    "three": "t3ree",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne",
}


def replaceWordsWithDigits(line):
    # scan the string and replace words with digits
    for i in range(len(line)):
        for j in range(i, len(line)):
            if line[i:j] in map:
                line = line.replace(line[i:j], str(map[line[i:j]]), 1)
                return replaceWordsWithDigits(line)
    return line


with open("input.txt") as f:
    lines = f.readlines()
    summ = 0
    for line in lines:
        line.strip()
        line += 'z'
        firstDigit = False
        numString = []
        print(line)
        line = replaceWordsWithDigits(line)
        print(line)
        for i in range(len(line)):
            if not firstDigit and '0' <= line[i] <= '9':
                numString.append(line[i])
                firstDigit = True
            if '0' <= line[i] <= '9':
                lastDigit = line[i]

        numString.append(lastDigit)
        num = int(''.join(numString))
        print(num)
        print()

        summ += num
    print(summ)
