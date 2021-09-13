"""
Case-study 'gas station'

Developers:
        Kondrashov M. - 100000000000000000%
        Bikmetov E. -
        Bychkov K. -


"""


with open('azs.txt', 'r', encoding='UTF-8') as F_in:
    all_lines = F_in.readlines()

fillings_max = dict()
fillings_fuels = dict()
for line in all_lines:
    elements_in_line = line.split()
    fillings_max[elements_in_line[0]] = elements_in_line[1]  # {'1': '3', '2': '2', '3': '4'}
    fillings_fuels[elements_in_line[0]] = elements_in_line[2:]  # {'1': ['АИ-80'], '2': ['АИ-92'], '3': ['АИ-92', 'АИ-95', 'АИ-98']}


