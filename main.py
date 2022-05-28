import os

import requests
from bs4 import BeautifulSoup

languages = {
    1:"Python",
    2:"Java",
    3:"JavaScript",
    4:"C++"
}

def get_data_by_class(bs_soup,cls):
    result = bs_soup.find(class_=cls)
    return result.get_text()

def make_new_dir(name,level,lang):
    # print(newPath)
    name = str(name)
    level = str(level)
    lang = str(lang)
    currentPath = os.getcwd()
    newPath = '\\'.join([currentPath, level, name, lang])
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        print('dir',name,'in level',level,'with',lang,'has been created')

def get_name_of_kata(soup):
    cls = "ml-2 mb-3"
    return  get_data_by_class(soup,cls)

def get_lang():
    print("choose language")
    for lang in languages:
        print('{}: {}'.format(lang,languages[lang]))
    return languages[int(input())]

def get_level_of_kata(soup):
    #todo
    cls = "inner-small-hex is-extra-wide"
    return get_data_by_class(soup,cls).split()[0]

def get_url():
    print('enter url')
    return input()

def make_link_txt_file(url,path):
    text_file = open(path+"\\link.txt", "w")
    text_file.write(url)
    text_file.close()


def get_soup(URL):
    page = requests.get(URL)
    tmp = BeautifulSoup(page.content, "html.parser")
    return tmp
def make_dir():
    URL = get_url()
    soup = get_soup(URL)
    name = get_name_of_kata(soup)
    level = get_level_of_kata(soup)
    make_new_dir (name , level, get_lang())
    currentPath = os.getcwd()
    path = '\\'.join([currentPath, level, name,])
    make_link_txt_file(URL,path)


make_dir()

