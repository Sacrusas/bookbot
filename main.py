from stats import number_of_words, count_characters, sort_and_print
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    contents = get_book_text(file_path)
    num_of_words = number_of_words(contents)
    dictionary = count_characters(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    print(sort_and_print(dictionary))
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


main()