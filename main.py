def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

# reads the file and returns the text as a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

# returns the number of words in the text
def count_words(text):
    return len(text.split())

# returns a dictionary with the count of each letter in the text
def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha() and letter.lower() in letter_counts:
            letter_counts[letter.lower()] += 1
        elif letter.isalpha():
            letter_counts[letter.lower()] = 1
    return(letter_counts)

# returns a sorted list of dictionaries with the count of each letter in the text
def sort_letters(dictionary):
    letter_counts_list = []
    for item in dictionary:
        letter_counts_list.append({"letter": item, "count":dictionary[item]})
    letter_counts_list.sort(reverse=True, key=lambda item: item["count"])
    return letter_counts_list

# prints a report with the word count and the count of each letter in the text
def print_report(path):
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    letters_count_dict = count_letters(book_text)
    letters_count_sorted_list = sort_letters(letters_count_dict)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document \n")
    for item in letters_count_sorted_list:
        print(f"The {item["letter"]} character was found {item["count"]} times")
    print("--- End report ---")
    
if __name__ == "__main__":
    main()