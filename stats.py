def get_book_text(filepath):
    with open(filepath)as f:
        file_contents = f.read()
    return file_contents

def words(filepath):
    word_count = 0
    with open(filepath)as f:
        string = f.read()
    words = string.split()
    for i in words:
        word_count += 1
    return word_count

def characters(filepath):
    char_dict = {}
    with open(filepath)as f:
        string = f.read()
    for char in string:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict:
            char_dict[char] += 1
    return char_dict


def sort_dicts(dict):
    dictlst = []
    for key in dict:
        if key.isalpha():
            dictlst.append({"name": key, "num": dict[key]})
    dictlst.sort(key=lambda x: x["num"], reverse=True)
    return dictlst

def print_dict(filepath):
    sorted_chars = sort_dicts(characters(filepath))
    for i in sorted_chars:
        print(f"{i['name']}: {i['num']}")

def format(filepath):
    print(f"""============ BOOKBOT ============
Analysing book found at {filepath}
----------- Word Count ----------
Found {words(filepath)} total words
--------- Character Count -------
          """)
    print_dict(filepath)
