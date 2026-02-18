tul = (1,2,3,4,5,6,7,9,12)

even_tul =()
odd_tul = ()

for i in tul :

    if i % 2 == 0:

        even_tul += (i,)

    else:

        odd_tul += (i,)

print(even_tul)
print(odd_tul)