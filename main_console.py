import time 
from tower import Tower
import keyboard



def clear_console():
    print("\033[H\033[J", end="")

def show_towers():
    clear_console()
    print(a_tower.to_string())
    print(b_tower.to_string())
    print(c_tower.to_string())

clear_console()
print("Введите количество дисков")
disk_amount = int(input())

def TowerOfHanoi_recursive(n , source, destination, auxiliary):
    if n==1:
        destination.add_disk(source.remove_disk())
        return
    TowerOfHanoi_recursive(n-1, source, auxiliary, destination)
    destination.add_disk(source.remove_disk())
    TowerOfHanoi_recursive(n-1, auxiliary, destination, source)
    if (n == disk_amount):
        if(source.check_win() or destination.check_win() or auxiliary.check_win()):
            print("Задача решена успешно")

def TowerOfHanoi_iterative(n, source, auxiliary, destination):
    total_num_of_moves =int(pow(2, n) - 1)
    for i in range(1, total_num_of_moves + 1):
        if (i % 3 == 1):
            moveDisksBetweenTwoPoles(source, destination)
        elif (i % 3 == 2):
            moveDisksBetweenTwoPoles(source, auxiliary)
        elif (i % 3 == 0):
            moveDisksBetweenTwoPoles(auxiliary, destination)
    if(source.check_win() or destination.check_win() or auxiliary.check_win()):
        print("Задача решена успешно")

def moveDisksBetweenTwoPoles(src, dest):    
    pole1TopDisk = src.remove_disk()
    pole2TopDisk = dest.remove_disk()
 
    if (pole1TopDisk is None):
        src.add_disk(pole2TopDisk)
    elif (pole2TopDisk is None):
        dest.add_disk(pole1TopDisk)  
    elif (pole1TopDisk > pole2TopDisk):
        src.add_disk(pole1TopDisk)
        src.add_disk(pole2TopDisk)
    else:
        dest.add_disk(pole2TopDisk)
        dest.add_disk(pole1TopDisk)



a_tower = Tower(disk_amount, is_start_tower=True)
b_tower = Tower(disk_amount)
c_tower = Tower(disk_amount)
a_tower.fill()
print("Выберите алгоритм:\n1.Рекурсивный\n2.Итеративный\n3.Решать самостоятельно")
answer = input()
if(answer == "1"):
    n = disk_amount
    start_time = time.perf_counter() 
    TowerOfHanoi_recursive(n, a_tower, b_tower, c_tower)
    end_time= time.perf_counter()
    print("Время выполнения " + str(end_time - start_time) + " секунд")
elif(answer == "2"):
    n = disk_amount
    start_time = time.perf_counter() 
    TowerOfHanoi_iterative(n, a_tower, b_tower, c_tower)
    end_time= time.perf_counter()
    print("Время выполнения " + str(end_time - start_time) + " секунд")
else:
    current_disk = None
    count = 0
    while(True):
        end_game = False
        while(True):
            show_towers()
            print("Ходов: " + str(count))
            print("a - взять кольцо с первой башни\nb - взять кольцо со второй башни\nс - взять кольцо с третьей башни\nesc - выход")
            key = keyboard.read_key()
            time.sleep(0.2)
            if (key == "a"):
                current_disk = a_tower.remove_disk()
            elif(key == "b"):
                current_disk = b_tower.remove_disk()
            elif(key == "c"):
                current_disk = c_tower.remove_disk()
            elif(key == "esc"):
                end_game = True
            if not(current_disk is None) or end_game:
                break
        if(end_game):
            break    
        while(True):
            show_towers()
            print("Ходов: " + str(count))
            print("Рамер кольца: " + str(current_disk.size))
            print("a - положить кольцо на первую башню\nb - положить кольцо на вторую башню\nс - положить кольцо на третью башню\nesc - выход")
            key = keyboard.read_key()
            time.sleep(0.2)
            add_succes = False
            if (key == "a"):
                add_succes = a_tower.add_disk(current_disk)
            elif(key == "b"):
                add_succes = b_tower.add_disk(current_disk)
            elif(key == "c"):
                add_succes = c_tower.add_disk(current_disk)
            elif(key == "esc"):
                end_game = True
            if add_succes or end_game:
                current_disk = None
                count = count + 1
                break
        if(end_game):
            break 
        show_towers()
        if(a_tower.check_win() or b_tower.check_win() or c_tower.check_win()):
            print("Победа!")
            break
