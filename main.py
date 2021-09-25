"""
Case-study 'gas station'
Developers:
        Kondrashov M. - 70%
        Bikmetov E. - 40%
        Bychkov K. - 35%
"""

from random import randint
import datetime

tanker_max = {}
tanker_fuel = {}
tankers_queue = {}
with open('azs.txt', 'r') as F_azs:
    for element in F_azs.readlines():
        s = element.split()
        tanker_max[s[0]] = int(s[1])  # {'1': 3, '2': '2', 3': 4}
        tanker_fuel[s[0]] = s[2:]  # {'1': ['АИ-80'], '2': ['АИ-92'], '3': ['АИ-92', 'АИ-95', 'АИ-98']}
        tankers_queue[s[0]] = []


list_types = []
[[list_types.append(el) for el in tanker_fuel[key] if el not in list_types] for key in tanker_fuel]

dict_types_liters = dict().fromkeys(list_types, 0)
dict_types_cost = {'АИ-80': 97.10, 'АИ-92': 45.02, 'АИ-95': 48.85, 'АИ-98': 56.17}
dict_types_sum = dict().fromkeys(list_types, 0)

car_type = {}
car_liter = {}
with open('input.txt', 'r') as F_in:
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
    car_time[keys] = time_to(car_liter[keys])  # {'00:01': 1, '00:04': 5, '00:12': 5, '00:41': 3, '00:54': 4, '01:05': 2,


def end_time(time_1car):
    result = {}
    for key in time_1car:
        tm1 = datetime.timedelta(hours=int(key[:2]), minutes=int(key[3:]))
        tm2 = datetime.timedelta(hours=0, minutes=time_1car[key])
        result[key] = tm1 + tm2
    return result


timings_end = end_time(car_time)  # {'00:01': '0:03:00', '00:04': '0:08:00', '00:12': '0:15:00', '00:41': '0:45:00',
timings_start = {}


def check_places(tankers, time_now):  # time_now looks like '00:30'
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


def get_place(tankers, types_dict, car_fuel, max_t):
    """Gets a car queue"""
    qd = {}
    for key in types_dict:
        if car_fuel in types_dict[key]:
            qd[key] = len(tankers[key])
    k = ''
    dp = max(qd.values()) + 1
    for key in qd:
        if qd[key] < dp and max_t[key] > qd[key]:
            dp = qd[key]
            k = key
    return [dp, k]

not_served = 0

for key in timings_end:
    tankers_queue_before = tankers_queue.copy()
    tankers_queue = check_places(tankers_queue, key)
    for key2 in tankers_queue_before:
        g = set()
        for i in range(len(tankers_queue_before[key2])):
            if tankers_queue_before[key2][i] not in tankers_queue[key2]:
                tm = str(datetime.time(int(str(tankers_queue_before[key2][i]).split(':')[0]), int(str(tankers_queue_before[key2][i])[:len(str(tankers_queue_before[key2][i])) - 3].split(':')[1])))[:-3]
                print('В  {}  клиент  {} {} {} {}  заправил свой автомобиль и покинул АЗС.'.format(tm, timings_start[tankers_queue_before[key2][i]], car_type[timings_start[tankers_queue_before[key2][i]]], car_liter[timings_start[tankers_queue_before[key2][i]]], car_time[timings_start[tankers_queue_before[key2][i]]]))
                g.add(tankers_queue_before[key2][i])
                for key_2 in tanker_max:
                    print('Автомат №' + key_2 + '  максимальная очередь: ' + str(tanker_max[key_2]) + ' Марки бензина: ' + ' '.join(tanker_fuel[key_2]) + ' ->' + len(set(tankers_queue_before[key_2])-g) * '*')
    l = get_place(tankers_queue, tanker_fuel, car_type[key], tanker_max)
    if l[1] != '':
        print('В  {}  новый клиент:  {} {} {} {} встал в очередь к автомату {} '.format(key, key, car_type[key],car_liter[key], car_time[key],l[1]))
        dict_types_liters[car_type[key]] += int(car_liter[key])
        if l[0] != 0:
            time_of = tankers_queue[l[1]][l[0]-1]+datetime.timedelta(hours=0, minutes=car_time[key])
            timings_start[time_of] = key
            tankers_queue[l[1]].append(time_of)
        else:
            time_of = datetime.timedelta(hours=int(key[:2]), minutes=int(key[3:])) + datetime.timedelta(hours=0,minutes=car_time[key])
            timings_start[time_of] = key
            tankers_queue[l[1]].append(time_of)
    else:
        not_served += 1
        print('В  {}  новый клиент:  {} {} {} {} не смог заправить автомобиль и покинул АЗС. '.format(key, key, car_type[key], car_liter[key], car_time[key]))
    [print('Автомат №' + key3 + '  максимальная очередь: ' + str(tanker_max[key3]) + ' Марки бензина: ' + ' '.join(tanker_fuel[key3]) + ' ->' + len(tankers_queue[key3]) * '*') for key3 in tanker_max]

print('\n'+'_'*64)
print('Количество литров, проданное за сутки по каждой марке бензина:')
[print(key+': '+str(dict_types_liters[key])) for key in dict_types_liters]

for key in dict_types_sum:
    dict_types_sum[key] = dict_types_liters[key]*dict_types_cost[key]

summ = 0
for key in dict_types_sum:
    summ += dict_types_sum[key]
print('\nОбщая сумма продаж за сутки: '+str(round(summ, 2)))
print('\nКоличество клиентов, которые покинули АЗС не заправив автомобиль из-за «скопившейся» очереди: '+str(not_served))
print('_'*64)
