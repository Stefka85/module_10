# Импорты необходимых модулей и функций

import time
from datetime import datetime
from threading import Thread

# Объявление функции write_words
def write_words(word_count, file_name):
# word_count - количество записываемых слов
# file_name - название файла, куда будут записываться слова
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i+1}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')
    return write_words

# Взятие текущего времени
time_start_1 = datetime.now()

# Запуск функций с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

# Взятие текущего времени
time_stop_1 = datetime.now()
time_res_1 = time_stop_1 - time_start_1

# Вывод разницы начала и конца работы функций
print(f'Время работы функций {time_res_1}')

# Взятие текущего времени
time_start_2 = datetime.now()

# Создание и запуск потоков с аргументами из задачи
first_thread = Thread(target=write_words, args=(10,'example1.txt'))
second_thread = Thread(target=write_words, args=(30,'example2.txt'))
third_thread = Thread(target=write_words, args=(200,'example3.txt'))
fourth_thread = Thread(target=write_words, args=(100,'example4.txt'))

first_thread.start()
second_thread.start()
third_thread.start()
fourth_thread.start()

first_thread.join()
second_thread.join()
third_thread.join()
fourth_thread.join()


# Взятие текущего времени
time_stop_2 = datetime.now()
time_res_2 = time_stop_2 - time_start_2
print(f'Время работы потков {time_res_2}')

# Вывод разницы начала и конца работы потоков
print(f'Потоки быстрее функций на {time_res_1 - time_res_2} секунд')
