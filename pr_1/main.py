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


def check_hypothesis(hypo_s: dict, hyp_to_check: str, hyp_parents: list) -> dict:
    """
    Проверка эквивалетности гипотез
    К множеству родителей добавляется новый родитель, если есть похожие
    была ли ранее гипотеза? Если была, то добавляем 1 к родителям, если нет, то добавляем к гипотезам
    """
    tmp = hypo_s.copy()
    for h in tmp:
        parents = tmp.get(h)
        if h == hyp_to_check:
            hypo_s[h] = parents + hyp_parents
        else:
            hypo_s[hyp_to_check] = hyp_parents
    return hypo_s


if __name__ == '__main__':
    #  TODO: К следующему разу получить пересечение первых 10 примеров
    from_file = extract_data()
    poisonous, edible, list_p, list_e = form_dictionaries(from_file)
    """
    print(f'amount of edible mushrooms: {len(edible)}')
    print(f'amount of poisonous mushrooms: {len(poisonous)}')
    """
    del from_file

    hypotheses = dict()
    res_str, res_parents, flg = intersection(poisonous[list_p[0]], poisonous[list_p[1]],
                                             list_p[0], list_p[1])
    if flg:
        hypotheses[res_str] = res_parents

    # TODO: нужна проверка новой гипотезы, полученной при пересечении предыдущей гипотезы и следующего примера
    for i in range(1, 9):
        res_str, res_parents, flg = intersection(poisonous[list_p[i]], poisonous[list_p[i+1]],
                                                 list_p[i], list_p[i+1])
        if flg:
            hypotheses = check_hypothesis(hypotheses, res_str, res_parents)
    write_to_file(hypotheses, 'res.txt')
