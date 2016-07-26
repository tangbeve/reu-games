
import re
import string

frequency = {}
text = open('/home/tangee/Downloads/Macbeth_text.txt', 'r')
text_string = text.read().lower()
copy = [ ]

for word in text_string:
   frequency[word] = frequency.get(word, 0)+ 1
   frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]


import re
import string

frequency = {}
document_text = open('/home/tangee/Downloads/Macbeth_text.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
copy = [ ]
for word in match_pattern:
    copy.append ((word))
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]