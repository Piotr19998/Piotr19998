import math

class Punkt2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def drukuj(self):
        print("x =", self.x, "y =", self.y)
        
    def zeruj(self):
        print("Zeruje argumenty")
        self.x = 0
        self.y = 0
        
class Punkt3D(Punkt2D):
    def __init__(self,x,y,z):
        Punkt2D.__init__(self,x,y)
        self.z=z
        
    def drukuj(self):
        print("x =", self.x,"y =", self.y,"z =", self.z)
        
    def zeruj(self):
        print("Zeruje argumenty")
        self.x=0
        self.y=0
        self.z=0
        
class Odcinek(Punkt2D):
    def __init__(self,a,b,c,d):
        self.A=Punkt2D(a,b)
        self.B=Punkt2D(c,d)
        self.odl=math.sqrt((self.B.x-self.A.x)^2+(self.B.y-self.A.y)^2)
    def drukuj(self):
        print("Wynik: ",self.odl)

def testy():
    pass

if __name__ == "__main__":
    testy()