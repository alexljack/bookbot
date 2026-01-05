import sys
from stats import get_num_words, char_count, dict_sorter

def main():
    if (len(sys.argv) != 2):
         print('Usage: python3 main.py <path_to_book>')
         sys.exit(1)
    # print(sys.argv)
    file_path = sys.argv[1]
    book_content = get_book_text(file_path).lower()
    total = get_num_words(book_content)
    letters = list(book_content)
    letter_dict = char_count(letters)
    sorted_dict = dict_sorter(letter_dict)
    # print(sorted_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
         print(f'{dict['char']}: {dict['num']}')
    print("============= END ===============")

def get_book_text(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()


main()