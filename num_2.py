import os

str_path = "./num_2_input.txt"
if not os.path.exists(str_path):
    print("Файла нет")
    exit()

with open(str_path, "r", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

sorted_list = sorted(lines, key=lambda x: x.count("а"), reverse=True)
print(sorted_list)
