import os

from src.util.detector import detect_duplicates

DATA_PATH: str = 'data/references.bib'

def load_data(path: str) -> str:
    with open(path, 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    # load the data from the raw file
    data: str = load_data(path=DATA_PATH)

    # detect duplicates in the data
    duplicates = detect_duplicates(data)

    # print the duplicates
    if len(duplicates) == 0:
        print('No duplicates found.')
    else:
        print(f'{len(duplicates)} duplicate{"" if len(duplicates)==1 else "s"} found:')
        for duplicate in duplicates:
            print(f'- {duplicate}')