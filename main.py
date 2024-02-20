def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    letters_count_dict = count_letters(text)
    letters_count_list = letter_count_sorted(letters_count_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    for item in letters_count_list:
        print(f"The {item["letter"]} character was found {item["count"]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.lower() in letter_counts:
            letter_counts[letter.lower()] += 1
        else:
            letter_counts[letter.lower()] = 1
    return(letter_counts)

def letter_count_sorted(dictionary):
    letter_counts_list = []
    for item in dictionary:
        if item.isalpha():
            letter_counts_list.append({"letter": item, "count":dictionary[item]})
    letter_counts_list.sort(reverse=True, key=lambda item: item["count"])
    return letter_counts_list
        
if __name__ == "__main__":
    main()