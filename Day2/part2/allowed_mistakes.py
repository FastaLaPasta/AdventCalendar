
def get_data():
    results=[]
    with open('../input.txt', 'r') as file:
        for line in file:
            data = list(map(int, line.split()))
            results.append(data)
    return results



def is_good_sequence(sequence, allow_removal=0):
    for index in range(len(sequence) - 1):
        # Check if the difference between following elements is not between 1 and 3
        if not 1 <= sequence[index] - sequence[index + 1] <= 3:
            # If removal, try removing one of the two elements at the mismatch
            return allow_removal and any(
                is_good_sequence(sequence[start - 1:start] + sequence[start + 1:])
                for start in (index, index + 1)
            )
    return True


if __name__ == '__main__':
    data = get_data()
    for allow_removal in (0, 1):
        print(sum(
            is_good_sequence(seq, allow_removal) or is_good_sequence(seq[::-1], allow_removal)
            for seq in data
        ))
