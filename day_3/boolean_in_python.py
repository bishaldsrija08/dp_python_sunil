print(10>9)
print(10>=10)
print(10<9)
print(10<=9)
print(10==10) # equal to
print(10 !=9) # not (!) equal to
print(10!=10)
# a+b> a and b are operands, a+b is an expression, + is an operator


# And operator => both conditions must be true
print(10>9 and 5>3, "Both conditions are true")
print(10>9 and 5<3, "One condition is false")
print(10<9 and 5<3, "Both conditions are false")

# Or operator => at least one condition must be true
print(10>9 or 5>3, "Both conditions are true")
print(10>9 or 5<3, "One condition is true")
print(10<9 or 5<3, "Both conditions are false")
print(10>9 or 5>3, "Both conditions are true")

# Not operator => reverses the result
print(not True)
print(not False)
print(not(10>9))
print(not(10<9))