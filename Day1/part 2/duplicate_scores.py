import pandas as pd


def main():
    #Get and count occurences in Data
    data = pd.read_csv('../Input.csv')
    duplicate = data['list2'].value_counts()

    # Map counts to 'list1' and multiply each 'list1' value by its corresponding count in 'list2'
    data['result'] = data['list1'] * data['list1'].map(duplicate)
    return (sum(data['result'].dropna()))


if __name__ == '__main__':
    main()
