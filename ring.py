import re
from pygame import Rect
class Ring():
    
    def __init__(self, size):
        self.__size = size
    
    @property
    def size(self):
        return self.__size

    def __eq__(self,other):
        return self.size == other.size
    
    def __lt__(self, other):
        return self.size < other.size
    
    def __le__(self, other):
        return self.size <= other.size
    
    def to_string(self):
        return "#" * self.size
    
    def get_rect(self, x_pos, y_pos):
        r = Rect(0,0,self.size * 23, 20)
        r.midtop = (x_pos, y_pos)
        return r