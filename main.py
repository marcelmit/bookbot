def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letter(text)
    list_of_dictionaries = convert(letter_count)
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for kv in list_of_dictionaries:
        character = kv["character"]
        value = kv["value"]
        print(f"The \"{character}\" character was found {value} times")
    print("--- End report ---")
    
        
def convert(dictionary):
    return [{"character":key, "value":value} for key, value in dictionary.items()]


def sort_on(dictionary):
    return dictionary["value"]


def count_letter(text):
    single_dict = {}
    single_character = list(text.lower())
    only_alphabet = [sub for sub in single_character if sub.isalpha()]
    for character in only_alphabet:
        if character in single_dict:
            single_dict[character] += 1
        else: single_dict[character] = 1
    return single_dict
    
      
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


main()