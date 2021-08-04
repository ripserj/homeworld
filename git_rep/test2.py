from functools import reduce
#def product_of_odds(data):   # data - список целых чисел
#    return reduce(lambda x, y: x*y, filter(lambda x: x%2 ==1, data))

#print(product_of_odds([1,2,3,4,5,6])) 

#numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
#print(*list(filter(lambda x: str(x)!=str(x)[::-1], numbers)))

#numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]

#sorted_numbers = sorted(numbers, key=lambda x: sum(x)/len(x), reverse=True)

#print(sorted_numbers)
#print(div(20, 5))

words=input().split()
aa=dict(sorted(zip(list(map(lambda x: x.upper(), words)),words)))
for elem in aa:
   print(aa[elem], end=' ')

#print(*list(map(lambda x, y: x>y, n)))
#result = list(map(lambda a, b: a if a > b else b, words))
#print(lambda x: aa[x], aa)