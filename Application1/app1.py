import json
from difflib import SequenceMatcher, get_close_matches

from .data_from_db import Dictionary_Database


## get data from json file
def getData(filePath):

    # load(open(file))
    return json.load(open(filePath, 'r'))
    ## another way -- loads(String)
    # with open(filePath, 'r') as f:
    #     content = f.read();

    # return json.loads(content) 


# format the diaplay of sentence in the data
def list2String(l: list):
    s = ""
    for string in l:
        s = s + string + " "
    return s


# format the display of choices in matcher
def list2String2(l: list):
    s = ""
    for string in l:
        s = s + string + ", "
    return s[0:len(s)-2]


# judge the input word wether in data
# the input will consider to convert lowercase
# the input will consider to match all keys in data by ratio, maybe input mistake
def translate(data, word):

    if word not in data and word.lower() in data:
        confirm = input(f'Oh, let me see, do you want to enter {word.lower()}? (Y is yes, N is no)')
        if confirm.lower() == 'y':
            return list2String(data[word.lower()])
        else:
            return f'Not found {word} in data.'
    elif word not in data and word.upper() in data:
        confirm = input(f'Oh, let me see, do you want to enter {word.upper()}? (Y is yes, N is no)')
        if confirm.lower() == 'y':
            return list2String(data[word.upper()])
        else:
            return f'Not found {word} in data.'
    elif word in data:
        return list2String(data[word])
    else:
        # match to wrong input
        closest = get_closest_match(data, word, 4, 0.6)
        contain = get_contains_match(data, word)
        choices: set = set(closest) | set(contain)
        if len(choices) > 0:
            if len(choices) == 1:        
                confirm = input(f'Oh, let me see, do you want to enter {choices[0]}? (Y is yes, N is no)')
                if confirm.lower() == 'y':
                    return list2String(data[choices[0]])
                else:
                    return f'Not found {word} in data.'
            else:
                confirm = input(f'Oh, let me see, do you want to enter ({list2String2(choices)})? (copy it or write new one): ')
                if confirm not in data:
                    return translate(data, confirm)
                return list2String(data[confirm])             
        else :
           return f'Not found {word} in data.'     


def translate_from_db(word):
    db = Dictionary_Database("root", 'Lmy_131724', '42.194.218.246', 'dbtest')

    result = db.query_by_word(word)
    if result == None:
        return f'Not found {word} in database.'
    return result;


# call the specified method in difflib
def get_closest_match(data: dict, word, n, cutoff):
    targets = get_close_matches(word, data.keys(), n, cutoff)
    return targets


def get_contains_match(data: dict, word):
    contain_list = []
    for key in data.keys():
        if word.lower() in key.lower() and len(key)-len(word) < 3:
            contain_list.append(key)
    return contain_list


# old version of get_closest_match()
def get_closest_match_old(data: dict, word):
    target = ""
    ratio = 0
    for w in data:
        if SequenceMatcher(None, word, w).ratio() > ratio:
            target = w
            ratio = SequenceMatcher(None, word, w).ratio()
    
    return [target, ratio]


def application1():

    data = getData("Application1/data.json")

    word = input('Enter a word: ')

    result = translate(data, word)

    print(result)


def application2():
    word = input('Enter a word: ')

    result = translate_from_db(word)

    print(result)


if __name__ == '__main__':
    # application1()

    application2()

    # print(SequenceMatcher(None, 'ABA', 'aba').ratio())
