def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letter(text)
    print(f"{num_words} words found in the document")
    print(letter_count)



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




  

None

main()