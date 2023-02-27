class Car():
    def __init__(self,name,old):
        self.name = name
        self.old = old
    def print(self):
        return print(self.name+'===>'+str(self.old))
    def train(self):
        self.print()
car=Car('Tom',11)
car.print()
car.train()