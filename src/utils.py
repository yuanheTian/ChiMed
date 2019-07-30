import numpy as np
import random
import json
import argparse


def load_data(data_path):
    full_data = []
    with open(data_path, 'r', encoding='utf8') as f:
        for line in f.readlines():
            full_data.append(json.loads(line))
    return full_data


def save_data(data_path, data_list):
    with open(data_path, 'w', encoding='utf8') as f:
        for data in data_list:
            json.dump(data, f, ensure_ascii=False)
            f.write('\n')


def _str2bool(s):
    if s.lower() in ['true', 'yes']:
        return True
    elif s.lower() in ['false', 'no']:
        return False
    else:
        raise argparse.ArgumentTypeError('Wrong bool type!')


def select_two_answers(data_list):
    two_answer_data = []
    for data in data_list:
        answers = data['answers']
        if not len(answers) == 2:
            continue
        two_answer_data.append(data)
    return two_answer_data


def select_one_adopted_one_unadopted_answers(data_list):
    two_answer_data = []
    for data in data_list:
        answers = data['answers']
        if not len(answers) == 2:
            continue
        answer_1 = answers[0]
        answer_2 = answers[1]
        if (answer_1['adopted'] == 'True' and answer_2['adopted'] == 'False') or \
                (answer_1['adopted'] == 'False' and answer_2['adopted'] == 'True'):
            two_answer_data.append(data)
    return two_answer_data


def remove_by_length(datas):
    len_q_list = []
    len_a_list = []
    new_data = []
    for data in datas:
        question = data['question_content']
        answers = data['answers']
        answer_1 = answers[0]['answer']
        answer_2 = answers[1]['answer']

        len_q_list.append(len(question))
        len_a_list.append(len(answer_1))
        len_a_list.append(len(answer_2))

    print('min question length: %d' % min(len_q_list))
    print('min answer length: %d' % min(len_a_list))
    print('max question length: %d' % max(len_q_list))
    print('max answer length: %d' % max(len_a_list))
    min_q_length = np.percentile(len_q_list, 1)
    max_q_length = np.percentile(len_q_list, 99)
    min_a_length = np.percentile(len_a_list, 1)
    max_a_length = np.percentile(len_a_list, 99)

    for data in datas:
        question = data['question_content']
        answers = data['answers']
        answer_1 = answers[0]['answer']
        answer_2 = answers[1]['answer']

        if min_a_length <= len(answer_1) <= max_a_length and \
                min_a_length <= len(answer_2) <= max_a_length and \
                min_q_length <= len(question) <= max_q_length:
            new_data.append(data)
    return new_data


def switch_answers(dataset):
    size = len(dataset)
    random.seed(101)
    for i in range(int(size/2)):
        data = dataset[i]
        answer_1 = data['answers'][0]
        answer_2 = data['answers'][1]
        dataset[i]['answers'] = [answer_2, answer_1]
    random.shuffle(dataset)
