import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        # print('Начал чтение файл:', name)
        for line in file:
            if len(line) == 0:
                break
            all_data.append(line)
    return

def main1():
    start = datetime.now()
    for n in range(1, 5):
        read_info(f'./file {n}.txt')
    end = datetime.now()
    print(end - start, '(линейный)')

def main2():
    start = datetime.now()
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(end - start, '(многопроцессный)')


if __name__ == '__main__':
    main1()
    main2()
