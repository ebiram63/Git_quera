sq = []
for x in range(10):
    sq.append(x*x)

# list comprehension 
sq = [x*x for x in range(10)]
   
print(sq)


print([0 for y in range(5)])

print([str(x) + y for x in [1,2,3] for y in ['A', 'B']])

print([(x , y ) for x in[1,2,3] for y in [1,2,3] if x != y])


data = [10, -4 , 53, 122, 0]
print([x for x in data if x > 0])
print([x*x for x in data])
# wrong 
# print([x*x, x for x in data ])


matrix = [[1,2,3] , [4,5,6] , [7,8,9]]
for i in range(3):
    for j in range(3):
        print(matrix[i][j] , end=' ')
    print()
    
zeros = [[0 for c in range(3)] for r in range(2)]
print(zeros)

a = ['ebi' , 'omid', 'nickan' , 'moein']
del a[0]
print(a)
#del a[0:2]
# del a[:]

name = 'salam'
#del name 

b = [0,1,2,3,4,5,6]
print(*b)
print(b)