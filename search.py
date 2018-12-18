import pickle as pkl
import pandas as pd
import numpy as np
import re

with open('./result/db.pkl', 'rb') as input_pkl:
    df = pkl.load(input_pkl)
with open('./result/result.pkl', 'rb') as doc_pkl:
    doc = pkl.load(doc_pkl)

kw = input("Input the word you want to search ")

a = df[df['keywords']==kw]

def highlight_text(highlight_string, list_res):
    for idx in range(len(list_res)):
        item = list_res[idx]
        match_str = re.finditer(highlight_string, item)
        item_highlighted = u""
        last_end = 0
        for it in match_str:
            it = it.regs[0]
            item_highlighted += item[last_end:it[0]] + "\033[0;31m" + highlight_string + "\033[0m"
            last_end = it[1]
        item_highlighted += item[last_end:]
        list_res[idx] = item_highlighted
    for item in list_res:
        print(item)

if len(a) == 0:
    print("Couldn't find string " + "\033[0;31m" + kw + "\033[0m")
else:
    print(str(len(a))+"results totally")
    for x in np.array(a['docs']):
        highlight_text(kw, [doc[x]])
        print('finish')
