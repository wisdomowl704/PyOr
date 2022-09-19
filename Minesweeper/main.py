from __init__ import SETTINGS
import pygame

length = SETTINGS["setting"]["box_length"]
width = SETTINGS["setting"]["width"]
height = SETTINGS["setting"]["height"]

max_width = width * length
max_height = width * length

z_line = []
z_pos = []
ges = {}


class Ge:
    def __init__(self, pos, z_pos, z_line):
        self.come = False
        self.pos = pos
        self.line = [
            [(pos[0], pos[1]), (pos[0] + length, pos[1])],
            [(pos[0], pos[1]), (pos[0], pos[1] + length)],
            [(pos[0], pos[1] + length), (pos[0] + length, pos[1] + length)],
            [(pos[0] + length, pos[1]), (pos[0] + length, pos[1] + length)]
        ]

        z_pos.append(pos)
        z_line.extend(self.line)


def main():
    for x in range(width):
        for y in range(height):
            ges[f"{x * length}-{y * length}"] = Ge([x * length, y * length], z_pos, z_line)

    pygame.init()
    screen = pygame.display.set_mode((max_width, max_height))
    pygame.display.set_caption(SETTINGS["setting"]["window_massage"])

    while True:
        event = pygame.event.poll()

        # Pygame事件处理
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 鼠标左键
                x, y = event.pos
            elif event.button == 3:  # 鼠标右键
                x, y = event.pos
            elif event.button == 2:  # 鼠标中键
                pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pass
            elif event.key == pygame.K_s:
                pass

        # 屏幕刷新
        screen.fill((0, 0, 0))

        pygame.display.update()


if __name__ == "__main__":
    main()
