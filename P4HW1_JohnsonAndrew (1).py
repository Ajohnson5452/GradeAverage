# CTI-110
# P4HW1 - List
# Andrew Johnson
# 3/30/23
# Grades
module_grades = [ ] 
#Number of Grades
num_grades = int(input("How many grades? ")) 
#Set to 1
number = 1

while number <= num_grades:
    module_grades.append(float(input(f'Enter Grade {number}: ')))
    number += 1







print("------------Results-------------")
#Lowest Grade
print(f"Lowest Grade: {min(module_grades)}")
#Highest Grade
print(f"Hghest Grade: {max(module_grades)}")
#Sum of Grades
print(f"Sum: {sum(module_grades)}")
#Formulas to get the Average
module_sum = sum(module_grades)
number_of_tests = len(module_grades)
#Grades Average
average = (module_sum / number_of_tests)
print("-----------------------------------------")
print(f"Average: {average}")

if average <= 59.9:
   print(f"Your Grade Is A: F")
elif average <= 69.9:
    print(f"Your Grade Is A: D")
elif average <= 79.9:
    print(f"Your Grade Is A: C")
elif average <= 89.9:
    print(f"Your Grade Is A: B")
elif average <= 100.0:
    print(f"Your Grade Is A: A")
else:
    print("Entry Not Valid")
         



         

