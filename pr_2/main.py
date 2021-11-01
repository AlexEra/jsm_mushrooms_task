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
        if i == j and i != '0' and j != '0':
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


def v_is_parent_of_y(lst_0, lst_1):
    parent_flg = False
    for i in lst_0:
        if i in lst_1:
            parent_flg = True
            break
    return parent_flg


def partial_nesting(str_0, str_1):
    flg = False
    for i, j in zip(str_0, str_1):
        if i == j and i != 0 and j != 0:
            flg = True
            break
    return flg


def sum_of_parents(p_0: list, p_1: list) -> list:
    parents_res = p_0.copy()
    for p in p_1:
        if p not in parents_res:
            parents_res.append(p)
    parents_res.sort()
    return parents_res


def add_h(example: list, hpts: list, u_set: list) -> list:
    break_flg = False
    intersect_flg = False
    z, parents_of_z = '', list()
    for y in hpts:
        if partial_nesting(example[0], y[0]):
            hpts[hpts.index(y)][1] = sum_of_parents(y[1], example[1])
        else:
            z, parents_of_z, intersect_flg = intersect(y, example)
            for v in u_set[0:u_set.index(example)]:
                flg = v_is_parent_of_y(v[1], y[1])
                if flg:
                    break_flg = True
                    break
                else:
                    if partial_nesting(z, v[0]):  # is_z_in_v
                        break_flg = True
                        break
    if not break_flg:
        if intersect_flg:
            hpts.append([z, parents_of_z])  # merge_hpts_with_z

    break_flg = False
    for v in u_set[0:u_set.index(example)]:
        if partial_nesting(example[0], v[0]):  # is_x_in_v
            break_flg = True
            break
    if not break_flg:
        hpts.append(example)  # merge_hpts_with_x
    return hpts


if __name__ == '__main__':
    poisonous, edible = extract_data()

    hypotheses = list()
    for x in poisonous[0:100]:
        hypotheses = add_h(x, hypotheses, poisonous[0:100])
    write_to_file(hypotheses, 'res')
