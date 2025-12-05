import time

from lekiwi import LeKiwiConfig
from lekiwi.lekiwi import LeKiwi
from lekiwi.utils import busy_wait

from lekiwi.key_board_teleop import KeyboardTeleop

FPS = 30

def main():
    cfg = LeKiwiConfig(port="/dev/tty.usbmodem5A7C1231451")
    robot = LeKiwi(cfg)
    robot.connect()

    teleop = KeyboardTeleop()
    print("WASD: 移动 | QE: 旋转 | []: 调速 | ESC: 退出")

    try:
        while True:
            t0 = time.perf_counter()

            action = teleop.get_action()
            _action_sent = robot.send_action(action)

            # 控制循环频率
            busy_wait(max(1.0 / FPS - (time.perf_counter() - t0), 0.0))
    except KeyboardInterrupt:
        pass
    finally:
        teleop.stop()
        robot.disconnect()

if __name__ == '__main__':
    main()
