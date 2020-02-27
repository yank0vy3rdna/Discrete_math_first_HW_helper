author = '''
    author: yank0vy3rdna.ru
'''

from tabulate import tabulate
import copy

print(author)

data = {}
# inp = '021153411005200420000003100250005052142000444022525003102040300030005005400410052403100400501000105425210100000000401000005240000000532205300000'


# inp = '000011044005000003051045000000050230000052000542100500010000130200102140000001012313455010101404410002210044002501340000043404104005550200344030'
r = ''
print(
    'Введи свою таблицу графа построчно, заменяя все пропуски нулями(по 12 символов в строке): ')
for i in range(12):
    while True:
        inpstr = input('E' + str(i + 1) + ': ')
        if len(inpstr) == 12:
            r += inpstr
            break


# print(r)
def countNums(d: dict):
    counter = 0
    for i in d.keys():
        if d[i] > 0:
            counter += 1
    return counter


def printIter(d: dict, counts: dict, sorted_keys: list, answ: list,
              iteration: int):
    print()
    print('Iteration #' + str(iteration + 1))
    print()
    print()
    dataforprint = []
    k = 0
    for i in d.keys():
        dataforprint.append([i])
        for j in d[i].keys():
            if d[i][j] != 0 or int(i[1:]) == int(j[1:]):
                dataforprint[k].append(d[i][j])
            else:
                dataforprint[k].append(' ')
        dataforprint[k].append(counts[i])
        k += 1
    keys = list(d.keys()) + ['counts']
    print(tabulate(dataforprint, headers=keys, tablefmt="grid"))
    answforprint = []
    for i in sorted_keys:
        if i in answ:
            answforprint.append('phi' + str(iteration + 1))
        else:
            answforprint.append('')
    print(tabulate([sorted_keys, answforprint]))


for i in range(12):
    data['E' + str(i + 1)] = {}
    for j in range(12):
        data['E' + str(i + 1)]['E' + str(j + 1)] = int(inp[i * 12 + j])

answ = []
datas = []
countslist = []
sorted_keys_list = []


def rec(dictionary, iteration):
    global datas
    global answ
    global countslist
    global sorted_keys_list
    datas.append(copy.deepcopy(dictionary))
    counts = {}
    for i in dictionary.keys():
        counts[i] = countNums(dictionary[i])
    countslist.append(copy.deepcopy(counts))
    sorted_keys = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
    sorted_keys_list.append(sorted_keys)
    answ.append([sorted_keys[0]])
    last_count = counts[sorted_keys[0]]
    for i in sorted_keys[1:]:
        flag = True
        for j in answ[iteration].copy():
            if dictionary[j][i] != 0:
                flag = False
                break
        if flag:
            answ[iteration].append(i)
            last_count = counts[i]

    for i in answ[iteration]:
        dictionary.pop(i)
    for i in dictionary.keys():
        for j in answ[iteration]:
            dictionary[i].pop(j)
    if len(dictionary.keys()) != 0:
        return rec(dictionary, iteration + 1)
    return iteration


c = rec(data, 0) + 1

# for i in datas:
#     print(i)
for i in range(c):
    printIter(datas[i], countslist[i], sorted_keys_list[i], answ[i], i)

print()
print('Answer: ')
print()
for i in range(c):
    print('phi', str(i + 1), ' = ', sorted(answ[i], key=lambda x: int(x[1:])))
    print()
