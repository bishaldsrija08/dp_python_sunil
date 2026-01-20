# WAP to take marks of three subjects and calculate total marks and percentage.


sub1 = float(input("Enter marks of subject 1: ")) # input
sub2 = float(input("Enter marks of subject 2: ")) # input
sub3 = float(input("Enter marks of subject 3: ")) # input

total_marks = sub1 + sub2 + sub3 # calculation
percentage = (total_marks/3) # calculation

print("Total Marks: ", total_marks) # output
print(f"Percentage {percentage} %") # output
