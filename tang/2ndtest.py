words = "The cat in the hat. The cat jumped over the hat. A cow jumped over a chair and laughed. " \
        "A mouse ate a piece of cheese and ran away. We a laughed at the mouse."
counts = dict()
words = words.split()

for word in words:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

    lst = list()
    for key, val in counts.items():
        lst.append((val, key))

    lst.sort(reverse=True)

    for key, val in lst[:10]:
        print key, val



