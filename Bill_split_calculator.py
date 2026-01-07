print("Bill Split Calculator")

bill_amount = float(input("Enter the bill amount: "))

tip_percentage = float(input("Enter the tip percentage: "))

tip_amount = (tip_percentage/ 100) * bill_amount

total_amount = bill_amount + tip_amount

print(f"Total (including tip): ${total_amount}")

no_of_people = int(input("Enter the no of people:  "))

amount_per_person = total_amount/no_of_people

print(f"Each person pays: ${amount_per_person}")
