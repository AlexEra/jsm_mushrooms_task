def write_to_file(data: list, file_name: str) -> None:
    with open(file_name, 'w') as f:
        for i in data:
            f.writelines(str(i) + '\n')


def extract_data() -> (list, list):
    with open('agaricus-lepiota.data', 'r') as f:
        tmp = f.read().split('\n')

    tmp_p, tmp_e = list(), list()
    pp, ee = 1, 1
    for i in range(len(tmp)):
        data = tmp[i].replace(',', '')
        if data[0] == 'p':
            tmp_p.append([data[1:], [pp]])
            pp += 1
        else:
            tmp_e.append([data[1:], [ee]])
            ee += 1
    return tmp_p, tmp_e


def intersect(list_0: list, list_1: list) -> (str, list, bool):
    tmp = ''
    flag = False
    for i, j in zip(list_0[0], list_1[0]):
        if i == j and i != '0' and j != '0' and i != '?' and j != '?':
            tmp += i
            flag = True
        else:
            tmp += '0'
    if flag:
        parents = sum_of_parents(list_0[1], list_1[1])
    else:
        tmp = ''
        parents = []
    return tmp, parents, flag


def v_is_parent_of_y(lst_0, lst_1, idx_0, idx_1):
    parent_flg = False
    if idx_0 != idx_1:
        for i in lst_0:
            if i in lst_1:
                parent_flg = True
                break
    return parent_flg


def nesting(str_0, str_1):
    """
    Проверка вложения - если объект 2 вкладывается в 1, то в нем д.б. все непустые поля (признаки)
    объекта 2
    Нужно пройти по всем объекту
    Или пересечение и сравнение, равен ли результат объекту 2
    :param str_0:
    :param str_1:
    :return:
    """
    for i in range(len(str_1)):
        if str_1[i] != '0' and str_1[i] != '?':
            if str_1[i] != str_0[i]:
                return False
    return True


def sum_of_parents(p_0: list, p_1: list) -> list:
    parents_res = p_0.copy()
    for p in p_1:
        if p not in p_0:
            parents_res.append(p)
    parents_res.sort()
    return parents_res


def add_h(example: list, hpts: list, u_set: list) -> list:
    for y in hpts:
        if nesting(y[0], example[0]):  # если пример вкладывается в гипотезу
            hpts[hpts.index(y)][1] = sum_of_parents(y[1], example[1])
        else:
            break_flg = False
            z, parents_of_z, intersect_flg = intersect(y, example)

            """ проверка на относительную каноничность """
            for v in u_set[0:u_set.index(example)]:
                if v_is_parent_of_y(v[1], y[1], u_set.index(v), hpts.index(y)):  # если v является родителем y
                    break_flg = True
                    break
                else:
                    if nesting(v[0], z):  # если z вкладывается в v
                        break_flg = True
                        break
            if not break_flg:
                if intersect_flg:
                    hpts.append([z, parents_of_z])  # merge_hpts_with_z

    """ проверка на асболютную каноничность """
    for v in u_set[0:u_set.index(example)]:  # TODO: уточнить, проверка ниже проваливается всегда
        if nesting(v[0], example[0]):  # если пример вкладывается хотя бы в один из предыдущих примеров
            return hpts

    """ если соблюдается абс. каноничность, то добавить пример ко множеству гипотез """
    hpts.append(example)
    return hpts


if __name__ == '__main__':
    """ извлечение примеров из файла """
    poisonous, edible = extract_data()

    hypotheses_n = list()

    """ основной цикл по (-)-примерам """
    right_lim = 10
    for x in poisonous[0:right_lim]:
        hypotheses_n = add_h(x.copy(), hypotheses_n, poisonous[0:right_lim])
    write_to_file(hypotheses_n, 'res')
