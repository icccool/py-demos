import random

spam = {'name':'Zophie','color':'red','age':32}
print(spam['name'])

print('-----------------')
for v in spam.values():
    print(v)

print('-----------------')
for k in spam.keys():
    print(k)
    
print('-----------------')
for k in spam.items():
    print(k)