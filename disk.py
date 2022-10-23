class Disk():
    
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
    