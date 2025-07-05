from lidar_bot.drivebase import DriveBase
from lidar_bot.teleop import get_key
import time

def main():
    robot = DriveBase()

    print("WASD to drive, Q to quit, E to square")

    try:
        while True:
            key = get_key().lower()
            if key == 'w':
                robot.forward()
            elif key == 's':
                robot.backward()
            elif key == 'a':
                robot.left()
            elif key == 'd':
                robot.right()
            elif key == 'e':
                robot.drive_square()
            elif key == 'q':
                break
            else:
                robot.stop()
            time.sleep(0.1)
    finally:
        robot.stop()

if __name__ == "__main__":
    main()