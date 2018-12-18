import jieba
import jieba.analyse
import pickle as pkl
import numpy as np
from tqdm import tqdm
import pandas as pd

# Define how many keywords to be extracted from docs
keywords_candidate_number = 5

with open('./result/result.pkl', 'rb') as input_txt:
    input = pkl.load(input_txt)
input = np.array(input, dtype=str)
# Initial of keywords and weights ndarray
keywords = np.zeros((len(input), keywords_candidate_number), dtype='<U16')
weights = np.zeros((len(input), keywords_candidate_number), dtype=np.float16)

for i in tqdm(range(len(input))):
    item = input[i]  # metadata
    key_word_tuple = jieba.analyse.extract_tags(item,
                                                topK=keywords_candidate_number,
                                                withWeight=True)
    extracted_words = [x[0] for x in key_word_tuple]
    keywords[i, 0: len(extracted_words)] = extracted_words
    weights[i, 0: len(extracted_words)] = [x[1] for x in key_word_tuple]


input_index = np.arange(len(input)).repeat(keywords_candidate_number)
df = pd.DataFrame({"keywords": keywords.ravel(),
                   "weights": weights.ravel(),
                   "docs": input_index})
# df = df.groupby(["keywords", "weights"], sort=True).apply(lambda x: print(x))
'''
1. Group by keywords, which separate different keywords apart
2. For each keywords, sort the DataFrame return from <class df.groupby>
   by weights in descending order
3. Concatenate all sorted DataFrame info one, which have the same column
   as original
'''
df_Group_by_keywords = df.groupby(["keywords"], sort=True)
flag = 0
df_new = pd.concat([each_df.sort_values(by=["weights"], ascending=False) \
                    for _, each_df in df_Group_by_keywords],
                   ignore_index=True)

# answer = df_new[df_new['keywords'] == "高等教育"]
# print(answer)

with open('./result/db.pkl', 'wb') as output_pkl:
    pkl.dump(df_new, output_pkl)
