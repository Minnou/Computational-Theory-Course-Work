from time import sleep
from tower import Tower
from ring import Ring
import keyboard

def clear_console():
    print("\033[H\033[J", end="")

def show_towers():
    clear_console()
    print(a_tower.to_string())
    print(b_tower.to_string())
    print(c_tower.to_string())

a_tower = Tower(4, is_start_tower=True)
b_tower = Tower(4)
c_tower = Tower(4)
a_tower.fill()
current_ring = None

count = 0
while(True):
    end_game = False
    while(True):
        show_towers()
        print("Ходов: " + str(count))
        print("a - взять кольцо с первой башни\nb - взять кольцо со второй башни\nс - взять кольцо с третьей башни\nesc - выход")
        key = keyboard.read_key()
        sleep(0.2)
        if (key == "a"):
            current_ring = a_tower.remove_ring()
        elif(key == "b"):
            current_ring = b_tower.remove_ring()
        elif(key == "c"):
            current_ring = c_tower.remove_ring()
        elif(key == "esc"):
            end_game = True
        if not(current_ring is None) or end_game:
            break
    if(end_game):
        break    
    while(True):
        show_towers()
        print("Ходов: " + str(count))
        print("Рамер кольца: " + str(current_ring.size))
        print("a - положить кольцо на первую башню\nb - положить кольцо на вторую башню\nс - положить кольцо на третью башню\nesc - выход")
        key = keyboard.read_key()
        sleep(0.2)
        add_succes = False
        if (key == "a"):
            add_succes = a_tower.add_ring(current_ring)
        elif(key == "b"):
            add_succes = b_tower.add_ring(current_ring)
        elif(key == "c"):
            add_succes = c_tower.add_ring(current_ring)
        elif(key == "esc"):
            end_game = True
        if add_succes or end_game:
            current_ring = None
            count = count + 1
            break
    if(end_game):
        break 
    show_towers()
    if(a_tower.check_win() or b_tower.check_win() or c_tower.check_win()):
        print("Победа!")
        break

