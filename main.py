"""
Case-study 'gas station'

Developers:
        Kondrashov M. - 100000000000000000%
        Bikmetov E. -
        Bychkov K. -


"""
import random
import datetime

with open('azs.txt', 'r', encoding='UTF-8') as F_in:
    all_lines = F_in.readlines()

fillings_maxnfuels = dict()
fillings_fuels = dict()
tanks = []
for line in all_lines:
    elements_in_line = line.split()
    fillings_maxnfuels[elements_in_line[0]] = elements_in_line[1:]  # {'1': ['3', 'АИ-80'], '2': ['2', 'АИ-92'], '3': ['4', 'АИ-92', 'АИ-95', 'АИ-98']}
    tanks.append(elements_in_line[0])
print(tanks)
q = dict().fromkeys(tanks)

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

timings = dict()

def dict_oftimings(element, filtime, result):
    """Makes a dict {time_start: time_end}"""
    hrs1 = int(element[:2])
    mins1 = int(element[3:])
    tm1 = datetime.timedelta(hours=hrs1, minutes=mins1)
    tm2 = datetime.timedelta(hours=0, minutes=filtime)
    res_time = tm1 + tm2
    result[element] = str(res_time)





def information(cars_info):
    """Main"""
    res = dict()
    for el in cars_info:
        whole = int(time_to(cars_info[el][0]))
        dict_oftimings(el, whole, res)
        print('В {} новый клиент: {} {} {} {} встал в очередь к автомату №{}'.format(el, '-', '-', '-', str(whole), '-'))
    print(res)
information(cars_info)














