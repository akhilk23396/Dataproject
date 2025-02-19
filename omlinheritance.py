class parent:
    money= True
    def parent(self):
        print("This is parent class")

class child(parent):
    def child(self):
        print("This is child class")

class child_child(child):
    def child_child(self):
        print("This is child_child class")

c=child_child()
d=child()
print(c.money)
c.parent()
c.child()
c.child_child()