dot = "o"
line = "-"
edge = "+"
separators = ""
n = 3

for y in range (0, n,5):
    print ('-- +') * 5
    print (' o |' )  * 5
    print ('-- +') * 5
    print (  ' x |' ) * 5

for x in range(0, n, 5):
    print ('-- +') * 5
    print (' o |') * 5
    print ('-- +') * 5
    print (' x |') * 5
