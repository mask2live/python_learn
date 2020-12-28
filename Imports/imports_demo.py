import time
import os

def read_in_file_by_10s(filepath):
    while True:
        with open(filepath, 'r') as f:
            print(f.read())
            time.sleep(5)



import pandas

def csv_pandas(filepath):
    while True:
        if os.path.exists(filepath):
            data = pandas.read_csv(filepath)
            print(data.mean()['st2'])
        else:
            print(f'Not found {filepath}')
        time.sleep(10)


if __name__ == '__main__':

    # read_in_file_by_10s('FileProcessing/test.txt')
    csv_pandas('Imports/temps_today.csv')