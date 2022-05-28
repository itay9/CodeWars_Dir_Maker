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

def make_new_dir(newPath):
    if not os.path.exists(newPath):
        os.makedirs(newPath)
        name = newPath.split('/')[-2]
        level = newPath.split('/')[-3]
        lang = newPath.split('/')[-1]
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

def build_url(name,level,lang):
    name = str(name)
    level=str(level)
    lang=str(lang)
    currentPath = os.getcwd()
    url = '\\'.join([currentPath,level,name,lang])
    print(url)

def get_url():
    print('enter url')
    return input()

def get_soup():
    URL = get_url()
    page = requests.get(URL)
    tmp = BeautifulSoup(page.content, "html.parser")
    return tmp
def make_dir():
    soup = get_soup()
    newPath = build_url(get_name_of_kata(soup), get_level_of_kata(soup), get_lang())
    make_new_dir(newPath)


make_dir()

