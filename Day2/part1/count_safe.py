def main():
    reports = []
    with open('../input.txt', 'r') as file:
        for line in file:
            # map(int, l.split()) transform each string from the list to int, list transform map into list...
            report = list(map(int, line.split()))
            reports.append(report)
        
    count = 0

    for report in reports:
        increasing = True
        decreasing = True
        
        for level in range(len(report) - 1):
            diff = abs(report[level] - report[level + 1])
            # Check if values are in range
            if not (1 <= diff <= 3):
                increasing = decreasing = False
                break
            
            # Check if report is decreasing
            if report[level] >= report[level + 1]:
                increasing = False
            
            # Check if report is increasing
            if report[level] <= report[level + 1]:
                decreasing = False
        if increasing or decreasing:
            count += 1

    return count



if __name__ == '__main__':
    main()
