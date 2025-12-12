# Count words from a string arg
# return integer of the word count

def get_num_words(book):
    return len(book.split())

# do word count of each character from a string
# return a dictionary, pairing up each letter with its count

def get_chars_dict(book):
    book = book.lower()
    ans_dict = {}
    for char in book:
        if char in ans_dict:
            ans_dict[char] += 1
        else:
            ans_dict[char] = 1
    return ans_dict

# takes the dictionary of characters 
# and their counts and returns a sorted list of dictionaries

def sort_on(items):
    return items["num"]

def sorted_list_of_dict( dict_arg ):
    ans_list = []

    for i in dict_arg:
        ans_list.append({"char":i,"num":dict_arg[i]})

    ans_list.sort(reverse=True,key=sort_on)
    return ans_list

#sorted_list_of_dict( {'t': 29493, 'h': 19176, 'e': 44538} )





