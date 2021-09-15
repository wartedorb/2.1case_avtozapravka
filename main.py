"""
Case-study 'gas station'

Developers:
        Kondrashov M. - 100000000000000000%
        Bikmetov E. -
        Bychkov K. -


"""
import random
from datetime import time

with open('azs.txt', 'r', encoding='UTF-8') as F_in:
    all_lines = F_in.readlines()

fillings_max = dict()
fillings_fuels = dict()
for line in all_lines:
    elements_in_line = line.split()
    fillings_max[elements_in_line[0]] = elements_in_line[1]  # {'1': '3', '2': '2', '3': '4'}
    fillings_fuels[elements_in_line[0]] = elements_in_line[2:]  # {'1': ['АИ-80'], '2': ['АИ-92'], '3': ['АИ-92', 'АИ-95', 'АИ-98']}


with open('input.txt', 'r', encoding='UTF-8') as F_in2:
    all_lines_2 = F_in2.readlines()


cars_info = dict()
for line in all_lines_2:
    elements_in_line_2 = line.split()
    cars_info[elements_in_line_2[0]] = elements_in_line_2[1:]  # {'00:01': ['10', 'АИ-80'], '00:04': ['45', 'АИ-95'], '00:12': ['40', 'АИ-92'],...


def time_to(x):
    """What time does it take to fuel up a car"""
    x = int(x)
    if x % 10 != 0:
        x2 = x // 10 + 1
    else:
        x2 = x // 10
    r = random.randint(-1, 1)
    if x2 + r != 0:
        return x2 + r
    else:
        return x2











