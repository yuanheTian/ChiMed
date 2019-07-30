import os
import json
import argparse
import copy
from tqdm import tqdm
from os import path
import random
from utils import *

DATA_DIR = '../data'
URL_DIR = '../urls'


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

    random.seed(101)
    random.shuffle(all_qa_data)
    save_data(path.join(DATA_DIR, 'ChiMed.json'), all_qa_data)


def build_relevancy_dataset(build_same_dataset):
    corpus_data_list = load_data(path.join(DATA_DIR, 'ChiMed.json'))
    data_id_dir = path.join(URL_DIR, 'ChiMed-QA2')
    relevancy_dir = os.path.join(DATA_DIR, 'ChiMed-QA2')
    if not os.path.exists(relevancy_dir):
        os.mkdir(relevancy_dir)

    id2index = {corpus_data_list[i]['id']: i for i in range(len(corpus_data_list))}

    if build_same_dataset:
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
    else:
        random.seed(101)
        adoption_dir = os.path.join(DATA_DIR, 'ChiMed-QA1')
        train_data_path = os.path.join(adoption_dir, 'train.adoption.json')
        dev_data_path = os.path.join(adoption_dir, 'dev.adoption.json')
        test_data_path = os.path.join(adoption_dir, 'test.adoption.json')

        data_path_dict = {'train': train_data_path, 'dev': dev_data_path, 'test': test_data_path}

        for data_flag, data_path in data_path_dict.items():
            try:
                data_list = load_data(data_path)
            except FileNotFoundError:
                raise FileNotFoundError('Please build adoption prediction dataset before building relevancy prediction dataset.')

            max_len = len(data_list)
            for i, data in enumerate(data_list):
                negative_sample = random.sample(range(max_len), 1)[0]
                while negative_sample == i:
                    negative_sample = random.sample(range(max_len), 1)[0]

                answer_index = 0 if data_list[negative_sample]['answers'][0]['adopted'] == 'True' else 1

                if data['answers'][0]['adopted'] == 'True':
                    data['answers'][0]['relevancy'] = 'True'
                    data['answers'][1] = copy.deepcopy(data_list[negative_sample]['answers'][answer_index])
                    data['answers'][1]['relevancy'] = 'False'
                    data['answers'][1]['q_id'] = data_list[negative_sample]['id']
                else:
                    data['answers'][0] = copy.deepcopy(data_list[negative_sample]['answers'][answer_index])
                    data['answers'][0]['relevancy'] = 'False'
                    data['answers'][0]['q_id'] = data_list[negative_sample]['id']
                    data['answers'][1]['relevancy'] = 'True'
            save_data(os.path.join(relevancy_dir, data_flag + '.relevancy.json'), data_list)


def build_adoption_dataset(build_same_dataset):
    corpus_data_list = load_data(path.join(DATA_DIR, 'ChiMed.json'))
    data_id_dir = path.join(URL_DIR, 'ChiMed-QA1')
    adoption_dir = os.path.join(DATA_DIR, 'ChiMed-QA1')
    if not os.path.exists(adoption_dir):
        os.mkdir(adoption_dir)

    id2index = {corpus_data_list[i]['id']: i for i in range(len(corpus_data_list))}

    if build_same_dataset:
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
    else:
        print('# of data: %d' % len(corpus_data_list))
        print('selecting two-answer questions ...')
        all_data = select_two_answers(corpus_data_list)
        print('# of two answer data: %d' % len(all_data))
        print('removing questions that are too long or too short ...')
        all_data = remove_by_length(all_data)
        print('# of questions after removing by length: %d' % len(all_data))

        print('selecting questions with exactly one adopted and one unadopted answers ...')
        all_data = select_one_adopted_one_unadopted_answers(all_data)

        size = len(all_data)
        train_size = int(size * 0.8)
        dev_size = int(size * 0.9)

        train_set = all_data[:train_size]
        dev_set = all_data[train_size: dev_size]
        test_set = all_data[dev_size:]

        switch_answers(train_set)
        switch_answers(dev_set)
        switch_answers(test_set)

        save_data(os.path.join(adoption_dir, 'train.adoption.json'), train_set)
        save_data(os.path.join(adoption_dir, 'dev.adoption.json'), dev_set)
        save_data(os.path.join(adoption_dir, 'test.adoption.json'), test_set)


def build_dataset(data_flag, build_same_dataset=False):
    if data_flag == 'corpus':
        build_corpus()
    elif data_flag == 'relevancy':
        build_relevancy_dataset(build_same_dataset)
    elif data_flag == 'adoption':
        build_adoption_dataset(build_same_dataset)
    elif data_flag == 'all':
        build_corpus()
        build_adoption_dataset(build_same_dataset)
        build_relevancy_dataset(build_same_dataset)
    else:
        raise ValueError('Wrong data flag %s. Must be one of \'all\', \'corpus\', \'relevancy\', and \'adoption\'.' % data_flag)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_flag', required=True, type=str, default='all', help='The type of dataset you want to build. '
                                                                     'It should be one of \'all\', \'corpus\', \'relevancy\', '
                                                                     'and \'adoption\'.')
    parser.add_argument('--same_dataset', defaut=False, type=_str2bool, help='Keep it false if you don\'t get the urls '
                                                                             'from us')

    args = parser.parse_args()
    data_flag = args.data_flag
    print('data flag: %s' % data_flag)

    build_dataset(data_flag, args.same_dataset)

