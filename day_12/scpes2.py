

# scopes in python

def outer():
    x = 30
    # print(y)
    def inner():
        y= 10
        print(x)
        def inners():
            print(y, "from inners")
            print(x, "from outer")
        inners()
    inner()

outer()  # This will print 30