def main():
    with open('../input.txt', 'r') as file:
        result = [line.strip() for line in file]

    word = 'XMAS'
    count = 0
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]

    for y in range(len(result)):
        for x in range(len(result[y])):
            if result[y][x] == word[0]:
                for dy, dx in directions:
                    found = True
                    for i in range(1, len(word)):
                        ny, nx = y + i * dy, x + i * dx
                        if not (0 <= ny < len(result) and 0 <= nx < len(result[ny]) and result[ny][nx] == word[i]):
                            found = False
                            break
                    if found:
                        count += 1

    print("Count of 'XMAS':", count)


if __name__ == '__main__':
    main()
