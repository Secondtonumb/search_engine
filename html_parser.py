from bs4 import BeautifulSoup

# with open('./raw_data/194502/zh_CN/index/764915/list/index.htm') as f:
#     data = BeautifulSoup(f, 'lxml')
#     print(data.find_all('div', class_='t_jbxx_nr'))
#     print(data.find_all('div', class_='t_grjj_nr'))

# valid_info_tag = ['t_jbxx_nr', 't_grjj_nr']

# IMPORTANT: It seems that valid info are all included in "h1" attribute

def get_professor_name(text):
    """
    INPUT:
    text: title line included professor's name (str)
    --------
    RETURN:
    name: professor's name(str)
    """
    invalid_info = ["大连理工大学教师个人主页系统",
                    "--中文主页",
                    "DALIAN UNIVERSITY OF TECHNOLOGY Personal Homepage",
                    "--Home",
                    " ",                    
                    ","]
    name = text
    for t in invalid_info:
        name = name.replace(t, "")
    return name


def get_valid_info(bs_object):
    '''
    After Observation,we found that valid information are included in "p" tags
    INPUT:beautifulsoup objective
    --------
    RETURN: list of valid info
    '''
    valid_infos = []
    p_tags = bs_object.find_all('p')
    for tag in p_tags:
        for info in tag.stripped_strings:
            info_ = info.replace("\xa0", "")
            info_ = info_.replace("\n", "")
            valid_infos.append(info_)
    valid_infos = str(" ").join(valid_infos)
    valid_infos = valid_infos.replace("\n", "")
    return valid_infos
