from bs4 import BeautifulSoup
'''
Website Denoising Module
'''
# It seems that valid info are all included in "p" attribute
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
            info_ = info_.replace("&nbsp", "")
            info_ = info_.replace("\n", "")
            info_ = info_.replace("电子邮箱：", "")
            if len(info_) > 200: # To clear unknown long hash list 
                info_ = ""
            valid_infos.append(info_)
    valid_infos = str(" ").join(valid_infos)
    valid_infos = valid_infos.replace("\n", "")
    return valid_infos
