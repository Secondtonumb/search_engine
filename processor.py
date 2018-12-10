from bs4 import BeautifulSoup
from tqdm import tqdm
# import re
import os
import argparse
import pickle as pkl
from html_parser import get_professor_name, get_valid_info



parser = argparse.ArgumentParser(description=' ')
parser.add_argument('--raw_file_path',
                    type=str,
                    default='./raw_data/',
                    help='raw_html_file_path',)
parser.add_argument("--output_path",
                    type=str,
                    default='./result/')
args = parser.parse_args()

valid_info_tags = ['t_jbxx_nr', 't_grjj_nr', 't_resume_nr']

def file_extension(path):
    return os.path.splitext(path)[1]

def valid_file_generator(root):
    '''
    INPUT:
    root: dir of all raw_data
    --------
    valid_file_list: list of valid_file_path
    '''
    valid_file_list = []
    fs = os.walk(root)
    for path, d, filelist in fs:
        # print(d)
        for filename in filelist:
            temp_path = os.path.join(path, filename)
            if os.path.isfile(temp_path) and \
               file_extension(temp_path) is '.htm' or '.html':
                valid_file_list.append(temp_path)
    return valid_file_list

if __name__ == "__main__":
    if os.path.isdir(args.raw_file_path) == 0:
        print('raw data dir ERROR')
        exit(1)
    else:
        valid_file_path = valid_file_generator(args.raw_file_path)
        # print(valid_file_path[0: 10])
        result = []

        print("---- Start Parsing ----")
        for ele in tqdm(valid_file_path):
            with open(ele, "r") as raw_html_file:
                soup = BeautifulSoup(raw_html_file, 'lxml')
                title = soup.title.contents[0]
                professor_name = get_professor_name(title)
                valid_info = get_valid_info(soup)
                prof_document = professor_name + " " + valid_info
                result.append(prof_document)

        if not os.path.exists(args.output_path):
            print("Make result directory")
            os.mkdir(args.output_path)
        pkl_file = os.path.join(args.output_path, "result.pkl")
        txt_file = os.path.join(args.output_path, "result.txt")
        
        with open(pkl_file, "wb") as result_pkl:
            pkl.dump(result, result_pkl)
        with open(txt_file, "w") as result_txt:
            items = str("\n").join(result)
            result_txt.write(items)
        print("---- Finished ----")

