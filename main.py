from stats import num_words
from stats import count_char

def get_book_text(filepath):
	with open(filepath) as f:
		books_contents = f.read()
	return books_contents

def main():
	contents = get_book_text("books/frankenstein.txt")
	numWords = num_words(contents)
	print(f"Found {numWords} total words")
	char_count = count_char(contents)
	print(char_count)

main()
