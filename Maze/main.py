import copy
import random
import pygame
import yaml
import time
import os

f = open(f"{os.path.dirname(os.path.realpath(__file__))}/config.yaml", 'r', encoding='utf-8')
settings = yaml.load(f, Loader=yaml.FullLoader)

length = settings["setting"]["box_length"]
width = settings["setting"]["width"]
height = settings["setting"]["height"]
PrintMode = settings["setting"]["print_mode"]

max_width = width * length
max_height = width * length

font_type = "microsoft Yahei"
z_line = []
old_list = []
z_pos = []
select = {}
ges = {}
Status = [True, True, True]


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


class Url:
    def __init__(self, cur_pos, url):
        self.end = cur_pos
        self.to_pos = url


def SelectUrl(cur_pos, url):
    global select, Status

    Status[1] = False
    cur_ge = ges[f"{cur_pos[0]}-{cur_pos[1]}"]
    pos = cur_ge.pos

    if not [(pos[0], pos[1]), (pos[0] + length, pos[1])] in z_line:
        next_pos = [pos[0], pos[1] - length]
        if f"{next_pos[0]}-{next_pos[1]}" in ges.keys() and not f"{next_pos[0]}-{next_pos[1]}" in select.keys():
            zs_url = url[:]
            zs_url.append(next_pos)
            select[f"{next_pos[0]}-{next_pos[1]}"] = Url(next_pos, zs_url)
            SelectUrl(next_pos, zs_url)

    if not [(pos[0], pos[1]), (pos[0], pos[1] + length)] in z_line:
        next_pos = [pos[0] - length, pos[1]]
        if f"{next_pos[0]}-{next_pos[1]}" in ges.keys() and not f"{next_pos[0]}-{next_pos[1]}" in select.keys():
            zs_url = url[:]
            zs_url.append(next_pos)
            select[f"{next_pos[0]}-{next_pos[1]}"] = Url(next_pos, zs_url)
            SelectUrl(next_pos, zs_url)

    if not [(pos[0], pos[1] + length), (pos[0] + length, pos[1] + length)] in z_line:
        next_pos = [pos[0], pos[1] + length]
        if f"{next_pos[0]}-{next_pos[1]}" in ges.keys() and not f"{next_pos[0]}-{next_pos[1]}" in select.keys():
            zs_url = url[:]
            zs_url.append(next_pos)
            select[f"{next_pos[0]}-{next_pos[1]}"] = Url(next_pos, zs_url)
            SelectUrl(next_pos, zs_url)

    if not [(pos[0] + length, pos[1]), (pos[0] + length, pos[1] + length)] in z_line:
        next_pos = [pos[0] + length, pos[1]]
        if f"{next_pos[0]}-{next_pos[1]}" in ges.keys() and not f"{next_pos[0]}-{next_pos[1]}" in select.keys():
            zs_url = url[:]
            zs_url.append(next_pos)
            select[f"{next_pos[0]}-{next_pos[1]}"] = Url(next_pos, zs_url)
            SelectUrl(next_pos, zs_url)


def Za(cur_pos, s_ge):
    global ges, z_pos

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
        if f"{pos[0]}-{pos[1]}" in ges.keys() and ges[f"{pos[0]}-{pos[1]}"].come == False:
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

        return True, cur_pos, s_ge

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
            return False, cur_pos, s_ge

        return True, cur_pos, s_ge


def main():
    global Status, select

    cur_pos = [0, 0]
    s_ge = {}
    start = ()
    end = ()

    for x in range(width):
        for y in range(height):
            ges[f"{x * length}-{y * length}"] = Ge([x * length, y * length], z_pos, z_line)

    pygame.init()
    screen = pygame.display.set_mode((max_width, max_height))
    pygame.display.set_caption(settings["setting"]["window_massage"])

    while True:
        event = pygame.event.poll()

        # Pygame事件处理
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                start = (x - x % length, y - y % length)
            elif event.button == 3:
                x, y = event.pos
                end = (x - x % length, y - y % length)
            elif event.button == 2:
                start = ()
                end = ()
                select = {}
                Status = [True, True, True]

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                Status[2] = not Status[2]
            elif event.key == pygame.K_s:
                pass
                # 保存

        # 逻辑事件
        if Status[0]:
            # 迷宫生成
            Status[0], cur_pos, s_ge = Za(cur_pos, s_ge)

        elif len(start) == 2 and Status[1]:
            # 全图深度显示
            select[f"{start[0]}-{start[1]}"] = Url(start, [])
            SelectUrl(start, [])

        else:
            time.sleep(0.1)

        # 屏幕刷新
        screen.fill((0, 0, 0))

        if Status[0]:
            pygame.draw.rect(screen, (225, 255, 255), (cur_pos[0], cur_pos[1], length, length), 0)

        if len(start) >= 2:
            pygame.draw.rect(screen, (225, 0, 0), (start[0], start[1], length, length), 0)
            for k, v in select.items():
                if PrintMode == 1:
                    font = pygame.font.SysFont(font_type, length // 2)
                    surface = font.render(str(len(v.to_pos)), False, (225, 0, 0))
                    screen.blit(surface, (v.end[0], v.end[1]))

                elif PrintMode == 2:
                    shen = len(v.to_pos) * 1
                    if shen // 225 >= 3:
                        color = (225, 225, 225)
                    elif shen // 225 == 2:
                        color = (225, 225, shen % 225)
                    elif shen // 225 == 1:
                        color = (225, shen % 225, 0)
                    else:
                        color = (shen, 0, 0)
                    pygame.draw.rect(screen, color, (v.end[0], v.end[1], length, length), 0)

        if len(end) >= 2:
            pygame.draw.rect(screen, (0, 0, 225), (end[0], end[1], length, length), 0)
            if f"{end[0]}-{end[1]}" in select.keys():
                for url_pos in select[f"{end[0]}-{end[1]}"].to_pos[1:-1]:
                    pygame.draw.rect(screen, (0, 0, 0), (url_pos[0], url_pos[1], length, length), 0)

        if len(select) > 0:
            pass


        if Status[2]:
            for pos in z_line:
                pygame.draw.line(screen, (225, 225, 225), pos[0], pos[1], 1)

        pygame.display.update()


if __name__ == "__main__":
    main()
