salary = int(input("Enter your salary amount : "))

tax_rate= 0

if salary < 30000 :
    tax_rate = 5

elif salary > 30000 and salary < 70000 :
    tax_rate = 15

else :
    tax_rate = 25

taxed_amount = (salary*tax_rate)/100
final_salary_after_tax = salary -taxed_amount 
print("Final salary amount afteer tax",final_salary_after_tax)
print("Taxed Amount ",taxed_amount)
print("Tax Rate ",tax_rate, "%")
