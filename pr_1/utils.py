def write_to_file(data: (list, tuple, dict), file_name: str) -> None:
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
        s_p = sum_of_parents(prnts_0, prnts_1)
        return res, s_p, f


def sum_of_parents(p_0: list, p_1: list) -> list:
    parents_res = p_0.copy()
    for p in p_1:
        if p not in parents_res:
            parents_res.append(p)
    parents_res.sort()
    return parents_res


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
        if hyp_to_check in tmp:
            hypo_s[hyp_to_check] = sum_of_parents(tmp.get(hyp_to_check), hyp_parents)
        else:
            hypo_s[hyp_to_check] = hyp_parents
    return hypo_s


def intersection_with_checking(pr_0: list, pr_1: list, str_0: str, str_1: str, hs: dict) -> dict:
    rs, parents, _ = intersection(pr_0, pr_1, str_0, str_1)
    hs = check_hypothesis(hs, rs, parents)
    return hs


def iterator(str_chck: str, lst_par: list, obj_iter: dict, hpts: dict, lim_for_iterations=-1) -> dict:
    if lim_for_iterations == -1:
        for obj_str in obj_iter:
            hpts = intersection_with_checking(obj_iter[obj_str], lst_par, obj_str, str_chck, hpts)
        return hpts
    elif lim_for_iterations > 0:
        count = 0
        for obj_str in obj_iter:
            hpts = intersection_with_checking(obj_iter[obj_str], lst_par, obj_str, str_chck, hpts)
            count += 1
            if count > lim_for_iterations:
                break
        return hpts
