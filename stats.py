
def get_num_words(words):
     return len(words.split())

def char_count(letters):
    letter_dict = {}
    for letter in letters:
        if letter not in letter_dict:
            letter_dict[letter] = 1
        else:
            letter_dict[letter] += 1
    return letter_dict

def sort_on(items):
    return items["num"]

def dict_sorter(dict):
    dict_list = []
    for letter in dict:
        if letter.isalpha():
            # dict_list.append({letter: dict[letter]})
            dict_list.append({'char': letter, 'num': dict[letter]})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list