'''
    Q11. Find the most frequent element in a list
'''

from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0]

lst = [1, 2, 2, 3, 3, 3, 4]
print(most_frequent(lst))
