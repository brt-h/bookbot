print("hello world")    

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    book_count = count_words(book_text)
    print(book_text)
    print(book_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    word_count = len(text.split())
    print(f"The file contains {word_count} words.")

if __name__ == "__main__":
    main()