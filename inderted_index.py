import jieba
import jieba.analyse
import pickle as pkl
import numpy as np
from tqdm import tqdm
import pandas as pd
from pprint import pprint

keywords_candidate_number = 5

with open('./result/result.pkl', 'rb') as input_txt:
    input = pkl.load(input_txt)
input = np.array(input, dtype=str)
# input = input[0: 10]
# print(len(input))
# print(len(input[0: 1000]))
keywords = np.zeros((len(input), keywords_candidate_number), dtype='<U16')
weights = np.zeros((len(input), keywords_candidate_number), dtype=np.float16)

# print(keywords.shape, keywords.dtype)
# print(weights.shape, weights.dtype)

for i in tqdm(range(len(input))):
    item = input[i]
    key_word_tuple = jieba.analyse.extract_tags(item,
                                                topK=keywords_candidate_number,
                                                withWeight=True)
    # key_word_array = [list(x) for x in key_word_tuple]
    # print(key_word_array)
    # print(keywords[i].shape)
    temp1 = [x[0] for x in key_word_tuple]
    keywords[i, 0: len(temp1)] = temp1
    weights[i, 0: len(temp1)] = [x[1] for x in key_word_tuple]
    # print([x[0] for x in key_word_tuple])
    # print([x[1] for x in key_word_tuple])
# print(keywords)'
# print(weights)

input_index = np.arange(len(input)).repeat(keywords_candidate_number)
df = pd.DataFrame({"keywords": keywords.ravel(),
                   "weights": weights.ravel(),
                   "docs": input_index})
# df = df.groupby(["keywords", "weights"], sort=True).apply(lambda x: print(x))
df_Group_by_keywords = df.groupby(["keywords"], sort=True)

# each里面存着当前的keywords，each_df里面存着当前keyword所对应的dataframe(需要sort)
# print(df_new)
flag = 0

df_new = pd.concat([each_df.sort_values(by=["weights"], ascending=False) \
                    for _, each_df in df_Group_by_keywords],
                   ignore_index=True)
# print(df_new)


pprint(input[2422])
pprint(input[2420])
pprint(input[2750])
pprint(input[2752])
