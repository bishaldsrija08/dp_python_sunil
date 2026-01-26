"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# for lines we use outer loop
# for numbers in each line we use inner loop

lines = 5
for i in range(1, lines + 1, 1):  # Outer loop for lines
    for j in range(1, i + 1, 1):  # Inner loop for numbers
        print(j, end=" ")
    print()  # Move to the next line after each row

"""
i=1, j=1 to 1
i = 2, j=1 to 2
i = 3, j =1 to 3
i = 4, j =1 to 4
i = 5, j = 1 to 5
i =6, exit loop
"""

"""
*
* *
* * *
* * * *
* * * * *
"""

lines = 5
for i in range(1, lines+1, 1):
    for j in range(1, i+1, 1):
        print("*", end=" ")
    print()
    
"""
C
C H
C H I
C H I T
C H I T A
C H I T A W
C H I T A W A
C H I T A W A N
"""

word = "CHITWAN"
lines = len(word) #len helps to find the length of string
for i in range(1, lines+1,1):
    for j in range(0, i, 1):
        print(word[j], end = " ")
    print()
    
"""
* * * * *
* * * *
* * *
* *
*
"""
lines = 5
for i in range(lines, 0, -1):
    for j in range(1, i+1, 1):
        print("*", end=" ")
    print()

"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
lines =5
for i in range(lines, 0, -1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()
    

"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
lines =5
for i in range(lines, 0, -1):
    for j in range(lines, lines-i, -1):
        print(j, end=" ")
    print()
    
"""
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

lines =5
for i in range(lines, 0, -1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""



"""
* * * * *
*       *
*       *
* * * * *
"""