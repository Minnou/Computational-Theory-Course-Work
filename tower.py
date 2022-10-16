from ring import Ring


class Tower():
    def __init__(self, rings_amount, is_start_tower = False):
        self.__is_start_tower = is_start_tower
        self.__rings_amount = rings_amount
        self.__rings = []

    def add_ring(self, ring):
        if(len(self.__rings) != 0):
            if(ring.size < self.__rings[len(self.__rings) - 1].size):
                self.__rings.append(ring)
                return True
        else:
            self.__rings.append(ring)
            return True
        return False
    
    def remove_ring(self):
        if(len(self.__rings) != 0):
            return self.__rings.pop()
        return None

    def check_win(self):
        if ((not(self.__is_start_tower)) and len(self.__rings) == self.__rings_amount):
            return True
        return False
    
    def fill(self):
        i = self.__rings_amount
        while i > 0:
            self.__rings.append(Ring(i)) 
            i = i - 1           

    def to_string(self):
        tower = ""
        for i in range(self.__rings_amount - len(self.__rings)):
            tower = tower + (" " * (self.__rings_amount // 2))  +"|"+ "\n"
        i = len(self.__rings) - 1
        while i > -1:
            tower = tower + (" " * (self.__rings_amount // 2)) + self.__rings[i].to_string() +"\n"
            i = i - 1
        return tower
    def print(self):
        print(self.__rings)