"""
Case-study 'gas station'

Developers:
        Kondrashov M. - 100000000000000000%
        Bikmetov E. -
        Bychkov K. -


"""
from random import randint
import datetime

tanker_max = {}
tanker_fuel = {}
tankers_queue = {}
with open('azs.txt', 'r', encoding='UTF-8') as F_azs:
    for element in F_azs.readlines():
        s = element.split()
        tanker_max[s[0]] = int(s[1])  # {'1': '3', '2': '2', '3': '4'}
        tanker_fuel[s[0]] = s[2:]  # {'1': ['АИ-80'], '2': ['АИ-92'], '3': ['АИ-92', 'АИ-95', 'АИ-98']}
        tankers_queue[s[0]] = []

car_type = {}
car_liter = {}
with open('input.txt', 'r', encoding='UTF-8') as F_in:
    for element in F_in.readlines():
        s = element.split()
        car_liter[s[0]] = int(s[1])  # {'00:01': 10, '00:04': 45, '00:12': 40, '00:41': 30,
        car_type[s[0]] = s[2]  # {'00:01': 'АИ-80', '00:04': 'АИ-95', '00:12': 'АИ-92', '00:41': 'АИ-98',


def time_to(x):
    """What time does it take to fuel up a car"""
    x = int(x)
    if x % 10 != 0:
        x2 = x // 10 + 1
    else:
        x2 = x // 10
    r = randint(-1, 1)
    if x2 + r != 0:
        return x2 + r
    else:
        return x2


car_time = {}
for keys in car_liter:  # Получаем время на заправу
    car_time[keys] = time_to(
        car_liter[keys])  # {'00:01': 1, '00:04': 5, '00:12': 5, '00:41': 3, '00:54': 4, '01:05': 2,


def end_time(time_1car):
    """Getting a time of end"""
    result = {}
    for key in time_1car:
        tm1 = datetime.timedelta(hours=int(key[:2]), minutes=int(key[3:]))
        tm2 = datetime.timedelta(hours=0, minutes=time_1car[key])
        result[key] = tm1 + tm2
    return result


timings_end = end_time(car_time)  # {'00:01': '0:03:00', '00:04': '0:08:00', '00:12': '0:15:00', '00:41': '0:45:00',


# НО! время не строка!!!!!!!!!!!!!!


def check_places(tankers, time_now):
    """ Функция проходит списки из словаря очереди к колонке, удаляет времена, <= времени прибывшей машины"""
    ctime = datetime.timedelta(hours=int(time_now[:2]), minutes=int(time_now[3:]))
    result = {}
    for key in tankers:
        l1 = tankers[key]
        l2 = []
        for el in l1:
            if ctime >= el:
                pass
            else:
                l2.append(el)
        result[key] = l2
    return result


def main():
    pass



