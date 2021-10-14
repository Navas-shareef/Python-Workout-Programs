from string import punctuation
class Text_anlyzer():
	def __init__(self,text):
		for symbol in punctuation:
			text=text.replace(symbol,'')
		text=text.lower()
		self.text=text.split()

	def starting_with(self,charcter):
		charcter = charcter.lower()
		count=sum(1 for i in self.text if i[:len(charcter)]==charcter)
		return count


	def number_of_words(self,letter_number):
		""" return number of words according to spacifiefied no of letters"""
		no_of_words = sum(1 for i in self.text if len(i)==letter_number)
		return no_of_words
			

text="Hi Iam Navas shareef, what I do for you, iam here for helping to you"
obj=Text_anlyzer(text)
print(text)
print("Number of words :",len(obj.text))
print("Number of words starting with 'y' :",obj.starting_with('ia'))
print("Number of words with 3 letter :",obj.number_of_words(3))