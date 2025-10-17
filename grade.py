import random
print("welcome to the rotaluclac 6 class GPA calculator")
print("definitely getting your grades from 'jeffcopublicshools.us/infinatecampus' ")
grade1 = random.choice([0.0, 0.7, 1.4, 2.1, 2.4, 2.8, 3.3, 3.8, 4.0])
grade2 = random.choice([0.0, 0.3, 0.9, 1.5, 2.5, 3.1, 3.5, 4.0])
grade3 = random.choice([0.0, 0.6, 1.3, 1.7, 2.2, 2.9, 3.4, 3.9, 4.0])
grade4 = random.choice([0.0, 0.1, 0.8, 1.2, 1.8, 2.6, 3.2, 4.0])
grade5 = random.choice([0.0, 0.9, 1.0, 1.6, 2.3, 2.9, 3.3, 3.7, 4.0])
grade6 = random.choice([1.8, 2.5, 2.9, 3.4, 3.7, 3.9, 4.0])
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]
print("your 1st grade is", grade1)
print("your 2nd grade  is", grade2)
print("your 3rd grade is", grade3)
print("your 4th grade is", grade4)
print("your 5th grade is", grade5)
print("your 6th grade is", grade6)
grade_list = [grade1, grade2, grade3, grade4, grade5, grade6]
sum(grade_list)
len(grade_list)
count = len(grade_list)
total = sum(grade_list)
overall_gpa = total / count
print("based on the calculations your gpa should be around a", round(overall_gpa, 2))
choice = input("would you like to focus on the first half or second half of your classes(enter 1 or 2): ")
if choice == "1":
    first_classes_count = len(grade_list[:3])
    first_classes_total = sum(grade_list[:3])
    first_classes_gpa = first_classes_total / first_classes_count
    print("according to the calculations you should have", round(first_classes_gpa, 2))
    if first_classes_gpa > overall_gpa:
        print("congratulations it seems that the gpa for the first half of your classes are higher than your overall gpa")
    if first_classes_gpa < overall_gpa:
        print("it seems like your first classes gpa is lower than your overall gpa. This may mean that these classes are the ones you need to improve in the most for a higher gpa")
if choice == "2":
    second_classes_count = len(grade_list[3:])
    second_classes_total = sum(grade_list[3:])
    second_classes_gpa = second_classes_total / second_classes_count
    print("according to the calculations you should have a", round(second_classes_gpa, 2))
    if second_classes_gpa > overall_gpa:
        print("it seems like your second classes gpa is higher than your overall which means that you are doing the best in second half of your classes and that your first half could use some improvement")
    if second_classes_gpa < overall_gpa:
        print("it looks like your second half of your classes have a lower gpa than your overall gpa which means you need to improve on these classes to improve your gpa")