def write_to_file(data, file_name):
    with open(file_name, 'w') as f:
        for i in data:
            f.writelines(str(i) + '\n')


def extract_data() -> list:
    with open('agaricus-lepiota.data', 'r') as f:
        tmp = f.read().split('\n')
    return tmp


def form_dictionaries(f_data: list) -> (dict, dict, list, list):
    tmp_p, tmp_e = list(), list()
    p, e = dict(), dict()
    pp, ee = 1, 1
    for i in range(len(f_data)):
        data = f_data[i].replace(',', '')
        if data[0] == 'p':
            p[data] = [pp]
            tmp_p.append(data)
            pp += 1
        else:
            e[data] = [ee]
            tmp_e.append(data)
            ee += 1
    return p, e, tmp_p, tmp_e


def intersect(a_1: str, a_2: str) -> (str, bool):
    tmp = ''
    flag = False
    for i, j in zip(a_1, a_2):
        if i == j and i != '0' and j != '0':
            tmp += i
            flag = True
        else:
            tmp += '0'
    return tmp, flag


def intersection(dct: dict, key_0: str, key_1: str) -> (dict, bool):
    res, flg = intersect(key_0, key_1)
    if not flg:
        return {}, flg
    else:
        return {res: dct[key_0] + dct[key_1]}, flg


def check_hypothesis(hypotheses: dict, hyp_to_check: dict) -> dict:
    # TODO: проверка эквивалетности гипотез
    # TODO: нужно сравнить с гипотезами выше, к множеству родителей добавляется новый родитель, если есть похожие
    # была ли ранее гипотеза? Если была, то добавляем 1 к родителям, если нет, то добавляем к гипотезам
    # ВАЖНО! Списки с номерами родителей нужно предварительно отсортировать!
    pass


# Алгоритм "каждый с каждым"
if __name__ == '__main__':
    #  TODO: К следующему разу получить пересечение первых 10 пересечений
    from_file = extract_data()
    poisonous, edible, list_p, list_e = form_dictionaries(from_file)
    """
    print(f'amount of edible mushrooms: {len(edible)}')
    print(f'amount of poisonous mushrooms: {len(poisonous)}')
    """
    del from_file
    print(intersection(poisonous, list_p[0], list_p[1]))
