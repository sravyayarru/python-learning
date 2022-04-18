x=1
y=245689
z=-25896
print(x,y,z)
print(type(x))

import random
print(random.random())
print(random.randint(1,50))
print(random.choice([15,25,38,78,36,85]))
print(random.sample([22,32,42,96,75,85],4))
print(max(12,36,45,93,25))
print(min(1,3,4,65,78))

# strings
s="welcome to python"
print(s.isalnum())
print(s.isalpha())
print("2012".isdigit())
print("first number".isidentifier())
print("WELCOME".isupper())
print(s.islower())
print(" ".isspace())
print(s.capitalize())
print(s.startswith("wel"))

# list
l=[1,2,5,6,8,23]
print(l)
l.append(19)
print(l)
l2=[15,16]
l.extend(l2)
print(l)
print(l.index(23))
print(l.insert(1,22))
print(l)
print(l.pop(2))
print(l)
l.remove(15)
print(l)
l.reverse()
print(l)
l.sort()
print(l)

#dictionaries
d={'john':'23','bob':'25'}
print(d)
d['joy']='45'
print(d)
d.popitem()
print(d)
print(d.keys())
print(d.values())
print(d.get('bob'))
print(d.pop('john'))
print(d.clear())

#tuple
t=()
t1=(1,2,3)
t2=([10,20,30,40,50])
t4=tuple("abc")

print(t)
print(t1)
print(t2)
print(t4)

print(len(t2))
print(max(t2))
print(min(t2))
#iterating tuple
t=(1,2,3,4,5)
for i in t:
    print(i,end=" ")
#slice
print(t[0:3])
print(t[:4])

