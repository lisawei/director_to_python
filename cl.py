class Customer(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def setage(self,age):
        self.age=age
if __name__==('__main__'):
    c1=Customer('lisa',23,'female')
    c2=Customer('liuzheng',22,'male')
    c1.setage(22)
    c2.name='liu.zheng'
    customers = [c1,c2]
    for i in customers:
        print i.name,i.age,i.sex