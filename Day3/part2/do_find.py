import re

def treat_data():
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    not_pattern = r"don't\(\)"
    combined_pattern = rf'{do_pattern}|{not_pattern}|{pattern}'
    
    result = 0
    execute_mul = True

    with open('../input.txt', 'r') as file:
        for line in file:
            for match in re.finditer(combined_pattern, line):
                if match.group() == 'do()':
                    execute_mul = True
                elif match.group() == "don't()":
                    execute_mul = False
                else:
                    if execute_mul:
                        x, y = map(int, match.groups())
                        result += x * y
    return result


def main():
    print(treat_data())


if __name__ == '__main__':
    main()
