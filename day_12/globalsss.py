# Global scope

x=50

def outer():
    print(x, "from outer")
    def inner():
        print(x, "from inner")
        def inners():
            print(x, "from inners")
        inners()
    inner()

outer()  # This will print 50 from all functions