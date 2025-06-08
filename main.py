from stats import words
from stats import characters
def get_book_text(f):
    with open("/home/vyper5612/bootdotdev/bookbot/bookbot/books/frankenstein.txt")as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(1))
    return


words(1)
characters(1)

