def number_of_words(book_text):
    count = 0
    words = book_text.split()
    for word in words:
        count += 1
    return count

def count_characters(text):
    char_dict = {}
    new_text = text.lower()
    for char in new_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_and_print(char_dict):
    sorted_items = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    for key, item in sorted_items:
        if key.isalpha():
            print(f"{key}: {item}")

