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


# I had to convert my pdf file into a text file by using an online pdf to text converted
# My file is located here /home/tangee/Downloads/Macbeth_text.txt




def filePro(filename):
    f = open(filename, 'r')
    wordcount = 0
    for lines in f:
        f1 = lines.split()
        wordcount = wordcount + len(f1)
    f.close()
    print 'word count:', str(wordcount)



