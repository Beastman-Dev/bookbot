import re
from collections import Counter

def main ():
	book_to_analyze = "books/frankenstein.txt"
	count_of_words, count_of_characters = read_book(book_to_analyze)
	print(f"--- Begin report of {book_to_analyze} ---")
	print(f"{count_of_words} words found in the document\n")
	for i in count_of_characters:
		print(f"The '{i}' character was found {count_of_characters[i]} times")

def read_book(book_to_analyze):
	# Open the file and read its contents
	with open(book_to_analyze) as f:
		file_contents = f.read()
	count_of_words = word_count(file_contents)
	count_of_characters = character_count(file_contents)
	return count_of_words, count_of_characters

def word_count(file_contents):
	return len(file_contents.split()) # Split the contents of the file by spaces and count the number of words

def character_count(file_contents):
	file_contents = file_contents.lower() # Convert all characters to lowercase
	file_contents = re.sub(r'[^a-z]', '', file_contents) # Remove all non-alphabetic characters
	char_counts = Counter(file_contents) # Count the number of each character
	sorted_char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True)) # Sort the characters by count

	return sorted_char_counts



main()