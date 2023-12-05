import os

str_path = "./num_3_input.txt"
if not os.path.exists(str_path):
    print("Файла нет")
    exit()

with open(str_path, "r", encoding="utf-8") as file:
    lines = [line.rstrip().split(" ") for line in file]
# print('Лист: ', lines)

dct = {lines[i][0]: lines[i][1] for i in range(len(lines))}
print("Словарь: ", dct)

dct1 = dict([(x[0], x[1]) for x in sorted(dct.items(), key=lambda x: x[0])])
print("dct1: ", dct1)

dct2 = dict(
    [(x[0], x[1]) for x in sorted(dct1.items(), key=lambda x: x[1], reverse=True)]
)
print("dct2: ", dct2)

# Недоразумение
# sorted_dict = [(v[0], v[1]) for v in sorted(dct.items(), key=lambda v: (v[1], v[0]))]
# print("Отсортированный словарь: ", sorted_dict)
