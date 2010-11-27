#coding:utf-8

class C1:
    def __init__(self, name):
        self.name = name
        self.pc()

    def pc(self):
        print self.name

class C2(C1):
    def __init__(self, name):
        C1.__init__(self,name)
        self.pc()

    def pc(self):
        print 'C2'
        
p1=C1('C1')
p2=C2('c2')
