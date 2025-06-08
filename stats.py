
def words(e):
    word_count = 0
    with open("/home/vyper5612/bootdotdev/bookbot/bookbot/books/frankenstein.txt")as f:
        string = f.read()
    words = string.split()
    for i in words:
        word_count += 1
    print(f"{word_count} words found in the document")
    return 

def characters(e):
    char_list = []
    dict_list = []
    with open("/home/vyper5612/bootdotdev/bookbot/bookbot/books/frankenstein.txt")as f:
        string = f.read()
    words = string.split()
    for i in words:
        for e in i:
            new_dict = {}
            if e not in char_list:
                char_list.append(e)
                new_dict["name"] = e
                new_dict["num"] = 1
            if e in char_list:
                new_dict["num"] += 1
            dict_list.append(new_dict)
            print(dict_list)
                
    # for a in char_list:
    #     print(f"{a} {word_dict[f"{a}"]}")
    return 


def sort_dicts(dict):
    return dict["num"]
    
def sort_text(e):
    list_dict = [characters(e)]
    for i in characters(e):
         sorted_dict = list_dict.sort(reverse=True, key=sort_dicts)
         print(sorted_dict)

    
sort_text(2)
    
