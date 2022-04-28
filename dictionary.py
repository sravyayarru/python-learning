# concatenate
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)

# add key to dictionary
d = {0: 10, 1: 10}
print(d)
d.update({2: 20})
print(d)

# check whether a given key already exists in dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present(x):
    if x in d:
        print('key is present in the dictionary')
    else:
        print('key is not present in the dictonary')


is_key_present(5)
is_key_present(9)

# dictionary contains number(between 1 and n)in the form (x,x*x)
# n=int(input("input number"))
# d=dict()
# for x in range(1,n+1):
#     d[x]=x*x
# print(d)


# merge two dictionaries
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d = d1.copy()
d.update(d2)
print(d)

# combine two dictionary adding values for common keys
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)

# dictionary  keys are numbers between 1 and 15 (both included) and the values are square of keys
d = dict()
for x in range(1, 16):
    d[x] = x ** 2
print(d)

# to remove a key from a dictionary
d = {'a': 'green', 'b': 'yellow', 'c': 'pink'}
print(d)
if 'a' in d:
    del d['a']
print(d)

# to multiply all the items in a dictionary
d={'a':100,'b':200,'c':300}
result=1
for key in d:
    result=result*d[key]
print(result)