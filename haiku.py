import sys
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize, WhitespaceTokenizer
import curses
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import string

d = cmudict.dict()  

def num_syllables(word):
	# if word in string.punctuation:
	# 	return 0
	word = word.translate(None, string.punctuation)
	try:
		return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]][0]
	except KeyError:
		return 18


def parse_input(input_text):
	input_text = input_text.replace('\n',' ')
	sentences = sent_tokenize(input_text)
	return sentences

def haikuize(sentence):
	current_syl_count = 0
	first_line = ""
	second_line = ""
	third_line = ""
	for word in sentence.split():
		# print word + str(num_syllables(word))
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
		elif num_syllables(word) > 0:
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
  	# else:
  	# 	print "False: "+sentence

