def write_to_file(data, file_name):
    with open(file_name, 'w') as f:
        for i in data:
            f.writelines(str(i) + ' ' + str(data[i]) + '\n')


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


def intersection(prnts_0: list, prnts_1: list, key_0: str, key_1: str) -> (str, list, bool):
    res, f = intersect(key_0, key_1)
    if not f:
        return {}, [], f
    else:
        return res, prnts_0 + prnts_1, f


def sum_of_parents(p_0, p_1):
    for p in p_1:
        if p not in p_0:
            p_0 += [p]
    p_0.sort()
    return p_0


def check_hypothesis(hypo_s: dict, hyp_to_check: str, hyp_parents: list) -> dict:
    """
    Проверка эквивалетности гипотез
    К множеству родителей добавляется новый родитель, если есть похожие
    была ли ранее гипотеза? Если была, то добавляем 1 к родителям, если нет, то добавляем к гипотезам
    """
    tmp = hypo_s.copy()
    if tmp == {}:
        hypo_s[hyp_to_check] = hyp_parents
    else:
        for h in tmp:
            parents = tmp.get(h)
            if h == hyp_to_check:
                # hypo_s[h] = parents + hyp_parents
                hypo_s[h] = sum_of_parents(parents, hyp_parents)
            else:
                hypo_s[hyp_to_check] = hyp_parents
    return hypo_s