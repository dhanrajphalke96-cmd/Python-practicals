list1 =[1,2,1,2,3,4,3,4,2,3,5,6]

in_list1 = set()
duplicates = set()

for i in list1:
    if i in in_list1:
        duplicates.add(i)
    else :
        in_list1.add(i)

for i in duplicates:
    print(i)            