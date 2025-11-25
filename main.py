from stats import num_words

def get_book_text(filepath):
	with open(filepath) as f:
		books_contents = f.read()
	return books_contents

def main():
	contents = get_book_text("books/frankenstein.txt")
	numWords = num_words(contents)
	print(f"Found {numWords} total words")


main()
