import copy

l1 = [1, 2.5, [10, 20, 30], 'Python']

# shallow copy 
l2 = copy.copy(l1)
print(l2)
# l2 will have different memory address
print(id(l1))
print(id(l2))

l1[0] = 100
print(f'l1 = {l1}', id(l1))
print(f'l2 = {l2}', id(l2))


# deep copy
l1 = [1, 2.5, [10, 20, 30], 'Python']
l2 = copy.deepcopy(l1)
l1[0] = 5
l2[2][0] = 50
print(f'l1 = {l1}', id(l1))
print(f'l2 = {l2}', id(l2))


d1 = {'id': 1111, 'name': 'John', 'marks':{'eng': 71.5, 'maths': 91.5, 'bio':80.0} } 

# shallow copy
d2= copy.copy(d1)
d1['name']='ram'
d1['marks']['maths'] = 92.5
print(f'd1 = {d1}', id(d1))
print(f'd2 = {d2}', id(d2))

# deep copy
d2= copy.deepcopy(d1)
d1['name']='ram'
d1['marks']['maths'] = 90.5
print(f'd1 = {d1}', id(d1))
print(f'd2 = {d2}', id(d2))