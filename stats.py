def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
    
def count_each_character(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def print_character_counts(letter_count):
    sorted_items = sorted(letter_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in sorted_items:
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")