# Global keyword

def outer():
    global x
    x = 50
outer()

print(x)  # Output: 50

def another():
    print(x, "from another") # Accessing the global variable x
    
another()  # Output: 50