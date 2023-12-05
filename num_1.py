from random import randint, shuffle
import time


def bubble(array, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array


K = 100  # Количество элементов списка
spisok = [randint(1, 1000) for __ in range(K)]  # Создал список

start = time.time()  # точка отсчета времени
for _ in range(999):
    shuffle(spisok)
    spisok = sorted(spisok)
end1 = time.time() - start  # время выполнения
print("Среднее время выполнения встроенной функции: %.5f" % (end1 / K))

start = time.time()  # точка отсчета времени
for _ in range(999):
    shuffle(spisok)
    spisok = bubble(spisok, K)
end2 = time.time() - start  # время выполнения
print("Среднее время выполнения моей функции: %.5f" % (end2 / K))

print(
    f"\nВстроенная функция работает примерно в {round(end2 / end1, 1)} раза быстрее сортировки пузырьком"
)
