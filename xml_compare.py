import collections
name = 'parasnathbakchodanand'
capital_name = name.upper()
print(capital_name)
print(name[::-1])
for ele in name:
    
name_split = list(capital_name)
i  = 0
for char in name_split:
    if char == 'A':
        i = i + 1
print(i)

with open('file.txt',mode= 'w') as f:
    f.write('SaulGoodman')




#print(component)
#value = component[0:2:-1]
#print(value)