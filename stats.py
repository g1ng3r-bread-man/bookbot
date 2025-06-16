
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

    with open("/home/vyper5612/bootdotdev/bookbot/bookbot/books/frankenstein.txt")as f:
        string = f.read()
    words = string.split()
    for i in words:        
        for e in i:
            p = e.lower()

            new_dict = dict(char=p, num=1)
            print(new_dict)





    return 


def sort_dicts(dict):
    return dict["num"]
    
def sort_text(e):
    list_dict = [characters(e)]
    for i in characters(e):
         sorted_dict = list_dict.sort(reverse=True, key=sort_dicts)
         print(sorted_dict)


characters(4)
