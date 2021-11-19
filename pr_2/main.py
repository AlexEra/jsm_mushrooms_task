import time


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
        # if i == j and i != '0' and j != '0' and i != '?' and j != '?':
        if i == j:
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


def add_h() -> int:
    x_idx = u_set.index(x)
    hpts_len = len(hypotheses_p)
    for y in hypotheses_p[0:hpts_len]:
        if nesting(x[0], y[0]):  # если гипотеза вкладывается в пример
            hypotheses_p[hypotheses_p.index(y)][1] = sum_of_parents(y[1], x[1])
        else:
            break_flg = False
            z, parents_of_z, intersect_flg = intersect(y, x)

            """ проверка на относительную каноничность """
            if intersect_flg:
                count = 0
                while count < x_idx:
                    v = u_set[count]
                    # если v является родителем y ИЛИ z вкладывается в v
                    if count == 0 and hypotheses_p.index(y) == 0:
                        count += 1
                        continue
                    if v[1][0] in y[1] or nesting(v[0], z):
                        break_flg = True
                        break
                    count += 1
                if not break_flg:
                    hypotheses_p.append([z, parents_of_z])  # merge_hpts_with_z

    """ проверка на асболютную каноничность """
    count = 0
    while count < x_idx:
        v = u_set[count][0]
        # если пример вкладывается хотя бы в один из предыдущих примеров
        if nesting(v, x[0]):
            return 0
        count += 1

    """ если соблюдается абс. каноничность, то добавить пример ко множеству гипотез """
    hypotheses_p.append(x)


if __name__ == '__main__':
    """ извлечение примеров из файла """
    poisonous, edible = extract_data()

    hypotheses_p = list()

    """ основной цикл по (-)-примерам """
    right_lim = 5
    u_set = poisonous[0:right_lim]
    t_begin = time.time()  # for time test
    for x in u_set:
        add_h()

    print(f"dt = {time.time() - t_begin}")  # for time test
    write_to_file(hypotheses_p, 'res')
