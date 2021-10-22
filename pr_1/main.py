from utils import *


if __name__ == '__main__':
    from_file = extract_data()
    poisonous, edible, list_p, list_e = form_dictionaries(from_file)
    del from_file

    num_of_samples = 10
    hypotheses = dict()
    for i in range(1, num_of_samples-2):
        hypotheses = intersection_with_checking(poisonous[list_p[i]], poisonous[list_p[i-1]],
                                                list_p[i], list_p[i-1], hypotheses)
        hypotheses = iterator(list_p[i+1], poisonous[list_p[i+1]], hypotheses.copy(), hypotheses)
        hypotheses = iterator(list_p[i+2], poisonous[list_p[i+2]], poisonous, hypotheses, lim_for_iterations=i+1)
    write_to_file(hypotheses, 'output.txt')
