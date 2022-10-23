from disk import Disk


class Tower():
    def __init__(self, disks_amount, is_start_tower = False):
        self.__is_start_tower = is_start_tower
        self.__disks_amount = disks_amount
        self.__disks = []

    def add_disk(self, disk):
        if(len(self.__disks) != 0):
            if(disk.size < self.__disks[len(self.__disks) - 1].size):
                self.__disks.append(disk)
                return True
        else:
            self.__disks.append(disk)
            return True
        return False
    
    def remove_disk(self):
        if(len(self.__disks) != 0):
            return self.__disks.pop()
        return None

    def check_win(self):
        if ((not(self.__is_start_tower)) and len(self.__disks) == self.__disks_amount):
            return True
        return False
    
    def fill(self):
        i = self.__disks_amount
        while i > 0:
            self.__disks.append(Disk(i)) 
            i = i - 1           

    def to_string(self):
        tower = ""
        for i in range(self.__disks_amount - len(self.__disks)):
            tower = tower + (" " * (self.__disks_amount // 2))  +"|"+ "\n"
        i = len(self.__disks) - 1
        while i > -1:
            tower = tower + (" " * (self.__disks_amount // 2)) + self.__disks[i].to_string() +"\n"
            i = i - 1
        return tower
    @property
    def disks(self):
        return self.__disks