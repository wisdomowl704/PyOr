import random

import pygame
import yaml
import time

f = open("config.yaml", 'r', encoding='utf-8')
settings = yaml.load(f, Loader=yaml.FullLoader)

length = settings["setting"]["box_length"]
width = settings["setting"]["width"]
height = settings["setting"]["height"]

z_line = []
old_list = []
z_pos = []
ges = {}


class Ge:
    def __init__(self, pos):
        self.come = False
        self.pos = pos
        self.line = [
            [(pos[0], pos[1]), (pos[0] + length, pos[1])],
            [(pos[0], pos[1]), (pos[0], pos[1] + length)],
            [(pos[0], pos[1] + length),
             (pos[0] + length, pos[1] + length)],
            [(pos[0] + length, pos[1]),
             (pos[0] + length, pos[1] + length)]
        ]

        global z_pos, z_line
        z_pos.append(pos)
        z_line.extend(self.line)


def main():
    global ges

    global ges, z_pos

    za = True
    cur_pos = [0, 0]
    s_ge = {}

    max_width = width * length
    max_height = width * length

    for x in range(width):
        for y in range(height):
            ges[f"{x * length}-{y * length}"] = Ge(
                [x * length, y * length])

    pygame.init()
    screen = pygame.display.set_mode((max_width, max_height))
    pygame.display.set_caption(settings["setting"]["window_massage"])

    while True:

        if not za:
            time.sleep(0.1)

        event = pygame.event.poll()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        screen.fill((0, 0, 0))

        for pos in z_line:
            pygame.draw.line(screen, (225, 225, 225), pos[0], pos[1], 1)

        if za:
            old_pos = cur_pos
            ges[f"{cur_pos[0]}-{cur_pos[1]}"].come = True

            all_pos = [
                [cur_pos[0] + length, cur_pos[1]],
                [cur_pos[0], cur_pos[1] + length],
                [cur_pos[0] - length, cur_pos[1]],
                [cur_pos[0], cur_pos[1] - length]
            ]

            to_pos = []

            for pos in all_pos:
                if f"{pos[0]}-{pos[1]}" in ges.keys():
                    if ges[f"{pos[0]}-{pos[1]}"].come == False:
                        to_pos.append(pos)

            if len(to_pos) > 0:
                cur_pos = to_pos[random.randint(0, len(to_pos) - 1)]
                if old_pos[0] - cur_pos[0] == length:
                    for i in range(z_line.count(
                            [(old_pos[0], old_pos[1]), (old_pos[0], old_pos[1] + length)])):
                        z_line.remove(
                            [(old_pos[0], old_pos[1]), (old_pos[0], old_pos[1] + length)])

                elif old_pos[0] - cur_pos[0] == -length:
                    for i in range(z_line.count([(old_pos[0] + length, old_pos[1]),
                                                 (old_pos[0] + length,
                                                  old_pos[1] + length)])):
                        z_line.remove([(old_pos[0] + length, old_pos[1]),
                                       (old_pos[0] + length,
                                        old_pos[1] + length)])

                elif old_pos[1] - cur_pos[1] == length:
                    for i in range(z_line.count(
                            [(old_pos[0], old_pos[1]), (old_pos[0] + length, old_pos[1])])):
                        z_line.remove(
                            [(old_pos[0], old_pos[1]), (old_pos[0] + length, old_pos[1])])

                elif old_pos[1] - cur_pos[1] == -length:
                    for i in range(z_line.count([(old_pos[0], old_pos[1] + length),
                                                 (old_pos[0] + length,
                                                  old_pos[1] + length)])):
                        z_line.remove([(old_pos[0], old_pos[1] + length),
                                       (old_pos[0] + length,
                                        old_pos[1] + length)])
            else:
                br = False
                for k, v in ges.items():
                    if v.come and not f"{v.pos[0]}-{v.pos[1]}" in s_ge.keys():
                        all_pos = [
                            [v.pos[0] + length, v.pos[1]],
                            [v.pos[0], v.pos[1] + length],
                            [v.pos[0] - length, v.pos[1]],
                            [v.pos[0], v.pos[1] - length]
                        ]

                        for pos in all_pos:
                            if f"{pos[0]}-{pos[1]}" in ges.keys() and ges[f"{pos[0]}-{pos[1]}"].come == False:
                                cur_pos = ges[k].pos
                                br = True
                                break
                        else:
                            s_ge[f"{pos[0]}-{pos[1]}"] = False

                        if br:
                            break
                else:
                    za = False

        pygame.display.update()


if __name__ == "__main__":
    main()
