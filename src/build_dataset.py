import os
import json
import argparse
import random
import numpy as np
import copy
from tqdm import tqdm
from os import path
from numpy import array
from tabulate import tabulate

DATA_DIR = '../data'
URL_DIR = '../urls'


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


def build_corpus():
    id_dict = {}
    if not os.path.exists(DATA_DIR):
        os.mkdir(DATA_DIR)

    original_data_dir = os.path.join(DATA_DIR, 'original')
    file_list = os.listdir(original_data_dir)
    file_list.sort()
    all_qa_data = []

    for file_name in tqdm(file_list):
        if file_name.endswith('.json'):
            file_path = os.path.join(original_data_dir, file_name)
            with open(file_path, 'r', encoding='utf8') as f:
                datas = json.loads(f.readline())['data']
            for data in datas:
                data_id = data['id']
                if data_id not in id_dict:
                    id_dict[data_id] = 0
                    all_qa_data.append(data)

    save_data(path.join(DATA_DIR, 'ChiMed.json'), all_qa_data)


def build_relevancy_dataset():
    corpus_data_list = load_data(path.join(DATA_DIR, 'ChiMed.json'))
    data_id_dir = path.join(URL_DIR, 'ChiMed-QA2')
    relevancy_dir = os.path.join(DATA_DIR, 'ChiMed-QA2')
    if not os.path.exists(relevancy_dir):
        os.mkdir(relevancy_dir)

    id2index = {corpus_data_list[i]['id']: i for i in range(len(corpus_data_list))}

    for flag in ['train', 'dev', 'test']:
        data_id_file = path.join(data_id_dir, flag + '.relevancy.json')
        data_id_list = load_data(data_id_file)

        for data_id in data_id_list:
            q_id = data_id['q_id']
            relevant_q = corpus_data_list[id2index[q_id]]

            data_id['question_content'] = relevant_q['question_content']

            answer_info_list = data_id['answers']
            for answer_info in answer_info_list:
                mid = answer_info['mid']
                if 'q_id' in answer_info:
                    irrelevant_q = corpus_data_list[id2index[answer_info['q_id']]]
                    for answer in irrelevant_q['answers']:
                        if answer['mid'] == mid:
                            answer_info['answer'] = answer['answer']
                else:
                    for answer in relevant_q['answers']:
                        if answer['mid'] == mid:
                            answer_info['answer'] = answer['answer']

        save_data(path.join(relevancy_dir, flag + '.relevancy.json'), data_id_list)


def build_adoption_dataset():
    corpus_data_list = load_data(path.join(DATA_DIR, 'ChiMed.json'))
    data_id_dir = path.join(URL_DIR, 'ChiMed-QA1')
    adoption_dir = os.path.join(DATA_DIR, 'ChiMed-QA1')
    if not os.path.exists(adoption_dir):
        os.mkdir(adoption_dir)

    id2index = {corpus_data_list[i]['id']: i for i in range(len(corpus_data_list))}

    for flag in ['train', 'dev', 'test']:
        data_id_file = path.join(data_id_dir, flag + '.adoption.json')
        data_id_list = load_data(data_id_file)

        for data_id in data_id_list:
            q_id = data_id['q_id']
            q = corpus_data_list[id2index[q_id]]

            data_id['question_content'] = q['question_content']

            answer_info_list = data_id['answers']
            for answer_info in answer_info_list:
                mid = answer_info['mid']
                for answer in q['answers']:
                    if answer['mid'] == mid:
                        answer_info['answer'] = answer['answer']

        save_data(path.join(adoption_dir, flag + '.adoption.json'), data_id_list)


def build_dataset(data_flag):
    if data_flag == 'corpus':
        build_corpus()
    elif data_flag == 'relevancy':
        build_relevancy_dataset()
    elif data_flag == 'adoption':
        build_adoption_dataset()
    else:
        raise ValueError('Wrong data flag %s. Must be one of \'corpus\', \'relevancy\', and \'adoption\'.' % data_flag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_flag', required=True, type=str, help='The type of dataset you want to build. '
                                                                     'It should be one of \'corpus\', \'relevancy\', '
                                                                     'and \'adoption\'.')

    args = parser.parse_args()
    data_flag = args.data_flag
    print('data flag: %s' % data_flag)

    build_dataset(data_flag)

