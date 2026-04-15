from __future__ import annotations

from djitellopy import Tello


def main() -> None:
    tello = Tello()
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    tello.takeoff()
    tello.move_up(50)

    tello.move_forward(400)
    tello.rotate_clockwise(90) #right
    tello.move_forward(130) 
    tello.rotate_counter_clockwise(90) #left
    tello.move_forward(400)

    tello.rotate_counter_clockwise(90) #left
    tello.move_forward(150) 
    tello.rotate_clockwise(90) #right
    tello.move_forward(275)

    
    tello.rotate_clockwise(90) #right
    tello.move_forward(240)



    tello.land()
    tello.end()


if __name__ == "__main__":
    main()
