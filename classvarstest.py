class Test1(object):
    name: str = "bob"
    _gee = "willma"
    
    def __init__(self, name: str = None) -> None:
        if name:
            self.name = name


t1 = Test1()
t2 = Test1("Nicholas")
t3 = Test1(5)
t1._gee = "wow"

print(t1.name)
print(t2.name)
print(t3.name)
print(t1._gee)
print(t2._gee)
print(t3._geetgyzs)