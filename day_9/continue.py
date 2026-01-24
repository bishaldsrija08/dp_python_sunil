# Continue statement is used to skip the current iteration of a loop and move to the next iteration.

j = 0
while j<=10:
    j=j+1
    if j == 5:
        continue
    print(j)
    
# Example: Print all even numbers from 1 to 20 using continue statement
i = 0
while i<=20:
    i=i+1
    if i % 2!=0:
        continue
    print(i)