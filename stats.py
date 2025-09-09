def sort_on(character):
    return character["num"]

def sorted_list_of_dict(dictionary):
    list_of_dict = []
    for character in dictionary:
        list_of_dict.append({"char":character,"num":dictionary[character]})
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict 

def words_in_string(string):
    words = string.split()
    num_words = len(words)
    #print(f"{num_words} words found in the document")
    return num_words

def num_of_each_character(string):
    char_dict = {};

    for char in string:
        char = char.lower()
       # print(char)
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
