from utils import *


def intersection_with_check():
    pass


def iterator(str_chck, obj_iter, hpts):
    #TODO: решить проблему расширения obj_iter после пересечения
    for obj in obj_iter:
        hpts = intersection_with_check(obj, str_chck, hpts)
    return hpts


if __name__ == '__main__':
    from_file = extract_data()
    poisonous, edible, list_p, list_e = form_dictionaries(from_file)
    del from_file

    num_of_samples = 10
    hypotheses = dict()
    for i in range(num_of_samples-2):
        hypotheses = intersection_with_check()
        hypotheses = iterator()
        hypotheses = iterator()
