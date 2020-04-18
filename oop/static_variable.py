class Test:
    # static variable
    instance_count = 0
    def __init__(self):
        # static variable should be accessed this way
        Test.instance_count += 1;
    @staticmethod
    def hello( str):
        print( "Hello " + str);

a = Test()
b = Test()

print(Test.instance_count);
print(a.instance_count);
print(b.instance_count);
c = Test()
print(a.instance_count)
print(b.instance_count)
print(c.instance_count)
Test.hello("World")