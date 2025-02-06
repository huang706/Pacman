from math import sqrt

class Vector2D:
    def __init__(self,x:float=0.0,y:float=0.0):
        self.x=float(x)
        self.y=float(y)

    def __add__(self,other:'Vector2D') -> 'Vector2D':
        return Vector2D(self.x+other.x,self.y+other.y)

    def __sub__(self,other:'Vector2D') -> 'Vector2D':
        return Vector2D(self.x-other.x,self.y-other.y)

    def __mul__(self,scaler:float) -> 'Vector2D':
        return Vector2D(self.x*scaler,self.y*scaler)

    def __truediv__(self,scaler:float) -> 'Vector2D':
        if scaler==0:
            raise ValueError("Cannot divide by zero!")
        return Vector2D(self.x/scaler,self.y/scaler)

    def __eq__(self, other:'Vector2D') -> bool:
        return self.x==other.x and self.y==other.y

    def normalize(self) -> 'Vector2D':
        return self/self.length()

    def dot(self,other:'Vector2D') -> float:
        return self.x*other.x+self.y*other.y

    def length(self) -> float:
        return sqrt(self.x**2+self.y**2)

    def distance(self,other:'Vector2D') -> float:
        return (self-other).length()

    def to_tuple(self):
        return (self.x,self.y)