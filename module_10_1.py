from threading import Thread
import time


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Прекрасное слово № {i + 1}\n")
            time.sleep(0.01)


time_start = time.time()
wr_1 = write_words(10, 'example1.txt')
wr_2 = write_words(30, 'example2.txt')
wr_3 = write_words(200, 'example3.txt')
wr_4 = write_words(100, 'example4.txt')
time_end = time.time()
time_res1 = time_end - time_start
print('Работа потоков, вариант № 1: ', round(time_res1, 3))

time_start = time.time()
wr_5 = Thread(target=write_words, args=(10, 'example5.txt'))
wr_6 = Thread(target=write_words, args=(30, 'example6.txt'))
wr_7 = Thread(target=write_words, args=(200, 'example7.txt'))
wr_8 = Thread(target=write_words, args=(100, 'example8.txt'))

wr_5.start()
wr_6.start()
wr_7.start()
wr_8.start()
time_end = time.time()
time_res2 = time_end - time_start
print('Работа потоков, вариант № 2 ', round(time_res2, 3))

bonus_time = time_res1 / time_res2
print(f'Использование потоков сокращает время исполнения в данном примере с time.sleep(0.01) в {bonus_time:.2f} раз!')
print(f'В данном примере без time.sleep(0.01) примерно в 1.7 раз (каждые запуск по разному)')
