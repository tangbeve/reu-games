import re
from collections import Counter


document_text = open('/home/tangee/Downloads/Macbeth_text.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[^\W\d_]+\b', text_string)

frequency = {}
for word in match_pattern:

    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print words, frequency[words]
