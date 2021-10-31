def intersect(str_0, str_1):
    pass


def v_is_parent_of_y():
    pass


def is_str_in_v():
    pass


def merge_hpts_with_z():
    pass


def merge_hpts_with_x():
    pass


def add_h(example, hpts, u_set, y_parents, exmaple_parents):
    break_flg = False
    for y in hpts:
        if y in example:
            y_parents += exmaple_parents
        else:
            z = intersect(y, example)
            for v in u_set[0:x]:
                flg = v_is_parent_of_y()
                if flg:
                    break_flg = True
                    break
                else:
                    flg = is_str_in_v()  # is_z_in_v
                    if flg:
                        break_flg = True
                        break
    if not break_flg:
        merge_hpts_with_z()
    break_flg = False
    for v in u_set[0:x]:
        flg =  is_str_in_v()  # is_x_in_v
        if flg:
            break_flg = True
            break
    if not break_flg:
        merge_hpts_with_x()


if __name__ == '__main__':
    u_samples = list()
    hypotheses = list()
    for x in u_samples:
        add_h(x, hypotheses, [], [], [])
