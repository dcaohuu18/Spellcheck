def open_dict(dict_name):
    dictionary = open(dict_name, "r")
    return (dictionary.read()).split()

def right_or_wrong(word, dict_name): #determine whether the word is correctly spelled or not
    correct_spelling = False 
    index=0
    dictionary = open_dict(dict_name)
    while (correct_spelling == False) and (index < len(dictionary)):
        if word == dictionary[index]:
            correct_spelling = True
        else:
            index = index + 1
    return correct_spelling

def break_string(string): #break the string into characters
    list_of_chars = []
    for c in string:
        list_of_chars.append(c)
    return list_of_chars   

def find_the_distance(list1, list2): #find the edit distance between the wrong and the right words
    distance = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance = distance + 1
    return distance

def the_suitable_distance(word): #what is the suitable edit distance?
    if len(word) <= 4:
        return 1     
    elif 5 <= len(word) <= 8:
        return 2
    elif len(word) > 8:
        return 3

def spell_check(word, dict_name):
    if right_or_wrong(word, dict_name) == False:
        dictionary = open_dict(dict_name)
        for i in dictionary:
            if len(i) > len(word):
                word1 = word + (len(i) - len(word))*" "
                word_char_list = break_string(word1)
                i_char_list = break_string(i)
                right_word = True
                if find_the_distance(word_char_list, i_char_list) <= the_suitable_distance(word):
                    print(i)
            elif len(i) > len(word):
                word_char_list = break_string(word)
                i1 = i + (len(word) - len(i))*" "
                i_char_list = break_string(i)
                if find_the_distance(word_char_list, i_char_list) <= the_suitable_distance(word):
                    print(i)
            elif (len(i) == len(word)):
                word_char_list = break_string(word)
                i_char_list = break_string(i)
                if find_the_distance(word_char_list, i_char_list) <= the_suitable_distance(word):
                    print(i)
    else:
        print(word)

if __name__=="__main__":
    spell_check("th", "1000-dict.txt")
    
    
    
    