
list1 = [34, 567, 975, 127]

list1_for = []
for num in list1:
    list1_for.append(num/10)
print(list1_for)

list_origin = [num/10 for num in list1]
print(list_origin)

list_if = [num/10 for num in list1 if num > 50]
print(list_if)

def foo(lst):
    return [l for l in lst if isinstance(l, int)]

result = foo([99, 'data', 95, 94, "nodata"])
print(result)

# if else has to put in front of for statement 
list_ifel = [i/10 if i > 50 else i+50 for i in list1]
print(list_ifel)

def foo(lst):
    return sum([float(i) for i in lst])

print(foo(['1.2', '3.3']))