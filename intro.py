#
#str = "1 4 3 5 7"
#a = str.split()

#l = len(a)

#for i in range(0, l, 1):
#    if (int(a[i]) > 3):
#        print(a[i])

#print ('\n')

l = []
l2 = [1, 10]
l.append(l2)
l2 = [10, 100]
l.append(l2)
l2 = [20, 200]
l.append(l2)

rows = 3
cols = 2

for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        print (l[i][j])
        print (" ")
    print('\n')
    
