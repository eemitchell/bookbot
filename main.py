from stats import get_book_text
from stats import get_book_word_count
from stats import get_char_count
from stats import sort_chars
import sys

def main():
    #file_path = "./books/frankenstein.txt"
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        file_path = sys.argv[1]
        file_contents = get_book_text(file_path)
        num_words = get_book_word_count(file_contents)

        char_dict = get_char_count(file_contents)
        sorted_list = sort_chars(char_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for item in sorted_list:
            if item["char"].isalpha():
                print(f"{item["char"]}: {item["num"]}")
    
main()