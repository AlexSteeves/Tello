from easytello import tello
import keyboard
t = tello.Tello()
print(t.get_battery())



t.takeoff()

t.forward(1)
t.back(1)
t.land()




