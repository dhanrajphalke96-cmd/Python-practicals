list1 =[1,2,3,4,5]
list2 =[5,6,7,8,9]

set1 = set(list1)
set2 = set(list2)

common = set1.intersection(set2)

if len(common)== 0 :
    print("Given list has no common elements")

else :
    print("List share common elements",common)    