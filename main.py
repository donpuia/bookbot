import sys

try:
    sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text, count_each_character, print_character_counts

def main(): 
    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = len(book_text.split())
    print(f"Found {num_words} total words")

    letter_count = count_each_character(book_text)
    print("--------- Character Count -------")
    print_character_counts(letter_count)

main()