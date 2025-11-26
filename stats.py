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
	count_list = []
	for key in char_count:
		temp_dict = {"char": key, "num": char_count[key]}
		#print(temp_dict)
		count_list.append(temp_dict)
		#print(count_list)
	count_list.sort(reverse = True, key = sort_on)
	return count_list

def sort_on(items):
	return(items["num"])
	  
