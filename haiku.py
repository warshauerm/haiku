import sys
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
 
def num_syllables(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]


def parse_input(input_text):
	input_text = input_text.replace('\n',' ')
	sentences = sent_tokenize(input_text)
	return sentences

def haikuize(sentence):
	current_syl_count = 0
	first_line = ""
	second_line = ""
	third_line = ""
	for word in word_tokenize(sentence):
		if current_syl_count < 5:
			current_syl_count += num_syllables(word)
			if current_syl_count > 5:
				return (False, None)
			first_line += (word + " ") 
		elif current_syl_count < 12:
			current_syl_count += num_syllables(word)
			if current_syl_count > 12:
				return (False, None)
			second_line += (word + " ") 
		elif current_syl_count < 17:
			current_syl_count += num_syllables(word)
			if current_syl_count > 17:
				return (False, None)
			third_line += (word + " ")
		else:
			 return (False, None)
	return (True, [first_line, second_line, third_line])



if __name__ == "__main__":
  file_name = str(sys.argv[1])
  f = open (file_name, "r")
  input_text = f.read()
  sentences = parse_input(input_text)
  for sentence in sentences:
  	(is_haiku, haiku) = haikuize(sentence)
  	if is_haiku:
  		for line in haiku:
  			print line

