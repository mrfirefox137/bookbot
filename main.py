from stats import num_words
from stats import count_char
from stats import sort_alpha
import sys

def get_book_text(filepath):
	with open(filepath) as f:
		books_contents = f.read()
	return books_contents

def main():
	print("Usage: python3 main.py <path_to_book>")	
	contents = get_book_text(sys.argv[1])
	numWords = num_words(contents)
	char_count = count_char(contents)	
	count_list = sort_alpha(char_count)
	print("\n============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {numWords} total words")
	print("--------- Character Count -------")
	for item in count_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
#	sys.exit(1)
			
main()
