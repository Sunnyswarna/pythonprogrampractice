class computer:
    def __init__(self,name,make,os):
        self.name=name
        self.cpu= self.CPU(make)
        self.os= self.OS(os)
    def __str__(self):
        return 'Name:'+self.name + '\nMake: ' + self.cpu.get_make() + '\nOS Name: ' + self.os.get_name()
    class CPU:
        def __init__(self, make):
            self.make=make
        def grt_make(self):
            return self.make


    class OS:
        def __init(self, os):
            self.name = os
        def get_name(self):
            return self.name
c1= computer('pc101','intel','windows')
print(c1)