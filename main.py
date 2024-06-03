def sort_on(dict):
    return dict["num"]

def get_words(file):
    words = file.split()
    return len(words)


def text_to_letters(file):
    letters = {}
    for char in file:
        if not char in letters:
            letters[char] = 1
        else:
            letters[char] += 1

    letters_list = []
    for letter in letters:
        letters_list.append({
            "name": letter,
            "num": letters[letter]
        })
    letters_list.sort(reverse=True, key=sort_on)
    print(letters_list)
    return letters_list

with open("books/frankenstein.txt") as f:
    file = f.read()
    lower_file = file.lower()
    letters = text_to_letters(lower_file)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_words(file)} words found in the document")
    for l in letters:
        if l['name'].isalpha():
            print(f"The {l['name']} character was found {l['num']} times")
    print("--- End report ---")
