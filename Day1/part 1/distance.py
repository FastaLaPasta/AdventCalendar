import pandas as pd


def main():
    #Get and Sort Data
    data = pd.read_csv('../Input.csv')
    list1, list2 = sorted(data['list1']), sorted(data['list2'])

    # Calcul the "distance" for every data points on lists
    result = 0
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])

    return result


if __name__ == '__main__':
    print(main())
