user = input("Enter a string :")

unique = ''
for i in user :
    if i not in unique:
        unique +=i
print(unique)
print(len(unique))        