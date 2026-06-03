def before(func):
    def execute():
        print("calling before test")
        func()
    return execute

def after(func):
    def execute():
        func()
        print("calling after test")
    return execute

@before
@after
def test():
    print("calling function test")
test()


#--------------------------Example--------------------------

