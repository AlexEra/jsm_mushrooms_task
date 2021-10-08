import numpy as np


def extract_data():
    with open('agaricus-lepiota.data', 'r') as f:
        tmp = f.read().split('\n')
    data = list()
    p = list()
    e = list()
    for i in range(len(tmp)):
        data.append(tmp[i].split(','))
        if data[i][0] == 'p':
            p.append(data[i])
        else:
            e.append(data[i])
    return data, p, e


def write_to_file(data, file_name):
    with open(file_name, 'w') as f:
        for i in data:
            f.writelines(str(i) + '\n')


def intersect(a_1, a_2):
    # TODO: add flag of empty intersection
    tmp = list()
    for i, j in zip(a_1, a_2):
        if i == j and i != '0' and j != '0':
            tmp.append(i)
        else:
            tmp.append('0')
    return tmp


def equal_hyp(a_0, a_1):  # TODO: check for equal of hypothesis!
    # была ли ранее гипотеза? Если была, то добавляем 1 к родителям, если нет, то добавляем к гипотезам
    if a_0 == a_1 and a_0 != '0' and a_1 != '0':
        return a_1
    else:
        return '0'


# Алгоритм "каждый с каждым"
# TODO: массив примеров: [примеры и родители], + и -
# в родители записывается номер индекса (глобальный?)
# нужно сравнить с гипотезами выше, к множеству родителей добавляется новый родитель, если есть похожие -> equal_hyp


# проще сделать так: [[пример: str], [родитель: str]], суммируем строки, так проще
# родитель будет объявляться с длиной, соответствующей числу (+)-примеров и (-)-примеров, индексы независимы!
if __name__ == '__main__':
    #  К следующему разу получить пересечение первых 10 пересечений
    from_file, poisonous, edible = extract_data()
    """
    print(f'amount of edible mushrooms: {len(edible)}')
    print(f'amount of poisonous mushrooms: {len(poisonous)}')
    """

    # parents = np.zeros((len(from_file), len(from_file[0])))  # not need
    parents = [[i+1] for i in range(len(from_file))]
    print(intersect(from_file[2], from_file[5]))
