import re
import string

freq = {} #declared an empty dictionary
# I had to convert my pdf file into a text file by using an online pdf to text converted
# My file is located here /home/tangee/Downloads/Macbeth_text.txt
filename = open ('/home/tangee/Downloads/Macbeth_text.txt', 'r') #store the text file in a string
text_string = filename.read().lower() #letters will be lower case
pattern = re.findall(r'\b[a-z]{2,15}\b', text_string ) #This will set only characters a-z and no words longer than the 15 letters
for word in pattern:
     count = freq.get(word,0)
     freq[word] = count + 1

freq_list =  freq.keys()

for words in freq_list: #now you can get the number of times the word appeared and the words
    print words, freq[words]