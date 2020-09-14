from easytello import tello
import keyboard
t = tello.Tello();

t.takeoff();
t.streamon();

while(True):
    try:
        if keyboard.is_pressed('w'):
            t.forward(50)
        if keyboard.is_pressed('s'):
            t.back(50)
        if keyboard.is_pressed('d'):
            t.right(50)
        if keyboard.is_pressed('a'):
            t.left(50)
        if keyboard.is_pressed('q'):
            break
    except:
        pass
t.streamoff();
t.land();

##22

