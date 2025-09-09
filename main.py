from stats import words_in_string, num_of_each_character, sorted_list_of_dict
import sys

def get_book_text(file):
    with open(file) as f:
        files_contents = f.read()
    return files_contents

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_string = get_book_text(path)
    #print(book_string)
    num_words = words_in_string(book_string)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_characters = sorted_list_of_dict(num_of_each_character(book_string)) 
    for character in list_of_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
if __name__ == '__main__': 
    main()
