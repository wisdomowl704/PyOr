from screen_func import *
import time


def main():
    init()

    while True:
        # 事件处理
        event_run(pygame.event.poll())

        # 持续检测处理
        every()

        # 屏幕刷新
        pygame.display.update()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
