import jieba
import pickle as pkl
import jieba.analyse

from tqdm import tqdm
from pprint import pprint

with open('./result/result.pkl', 'rb') as input_txt:
    input = pkl.load(input_txt)

dict_ = []  # count all word included in all docs(list)

input = input[4000: 4010]

for item in tqdm(input):
    seg = jieba.lcut(item)  # segmentation for words and save the in list
    for x in seg:
        dict_.append(x)
dict = {}  # dictionary for word counting
for key in dict_:
    dict[key] = dict.get(key, 0) + 1

dict_keys = []  # count unique words
dict_sorted = (sorted(dict.items(), key=lambda d: d[1]))

for item in dict_sorted:
    dict_keys.append(item[0])
# print(dict_keys)
dict_keys = dict_keys[::-1]  # sorted by occurrence frequency


def current_keyword_value(keyword, doc_index, doc):
    value = []
    value.append(doc_index)
    value.append(doc)
    count = doc.count(keyword)
    value.append(count)
    return value

for key_index in tqdm(range(len(dict_keys))):  # key index: keyword index
    count = 0
    for index in range(len(input)):  # index : input infomation index
        related_item_dict = {}
        current_key = dict_keys[key_index]
        related_value = []
        if current_key in input[index]:
            count = count + 1  # related info count + 1
            current_key_occur_times = input[index].count(current_key)
            '''
            每个关键词,与之对应的信息构成一个词典
            词典的每一个项目存的信息为
            key = index + 关键词
            value = [x=(相应文档编号 + 相应文档 + 文档中出现的词的次数) for x in 所有包含的keyword的文档)]
            '''
            value_ele = current_keyword_value(current_key, index, input[index])
            related_value.append(value_ele)
            #  how many time current key occured in this info
            related_item_dict[(key_index, dict_keys[key_index])] = related_value
            #  print(index, key_index)
            print(related_item_dict)
    print("key_index %d  doc_count %d" % (key_index, count))
    print("--------")
# TF-IDF
