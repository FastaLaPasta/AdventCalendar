import re

def treat_data():
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    not_pattern = r"don't\(\)"
    result = 0

    with open('../test.txt', 'r') as file:
        for line in file:
            uncorrupteds = re.findall(pattern, line)
            for case in uncorrupteds:
                x, y = map(int, case)
                result += x * y
    return result


def main():
    print(treat_data())


if __name__ == '__main__':
    main()
