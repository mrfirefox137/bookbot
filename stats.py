def num_words(contents):                                                        
    words = contents.split()                                                    
    numWords = len(words)                                                       
    return numWords

def count_char(contents):
	unique = set(contents.lower())
	#print(unique)
	unique_dict = {}
	for char in unique:
		count = contents.count(char) + contents.count(char.upper())
		unique_dict[char] = count
	return unique_dict

def sort_alpha(char_count):
	 
	

	  
