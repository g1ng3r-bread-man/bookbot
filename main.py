from stats import *
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>  eg. books/frankenstein.txt")
        sys.exit(1)
    global filepath 
    filepath = sys.argv[1]



    format(sys.argv[1])
    


if __name__ == "__main__":
    main()
    

