i = 1
while(i<100):
    j = 1
    while(j <=(i/j)):
        if not (i%j): break
        j = j * 3
    if (j > i/j): print i, "is odd"
    i = i + 3

    print "good bye"

i=0
while i<m:
    j=0
    while j<n:
        j=j+1
    i=i+1
print i