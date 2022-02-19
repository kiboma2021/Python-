'''
Write a program (function!) that takes a list and returns a new list that contains all 
the elements of the first list minus all the duplicates.

'''

a=[12,35,1,2,2,2,12,54,12]
x=[]
for i in a:
    if i not in x:
        x.append(i)
print(x)

def unique_list():
    x=[]
    for i in a:
        if i not in x:
            x.append(i)
    return(x)

unique_list