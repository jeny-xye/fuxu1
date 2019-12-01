class Test:
    cnt = 0
    def __init__(self):
        Test.cnt += 1 


c = Test()
c.cnt =21
# create a new instance attribute
print(Test.cnt)
print(c.cnt)