from settings import *

import random

fj = [
    (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0),
]


class Ge:
    def __init__(self, pos):
        self.come = False
        self.pos = pos
        self.line = [
            [(pos[0], pos[1]), (pos[0] + length, pos[1])],
            [(pos[0], pos[1]), (pos[0], pos[1] + length)],
            [(pos[0], pos[1] + length), (pos[0] + length, pos[1] + length)],
            [(pos[0] + length, pos[1]), (pos[0] + length, pos[1] + length)]
        ]

        self.fj_pos = []

        self.num = "0"
        self.print = self.num
        self.status = 0
        self.weeper = False

        self.get_fj_pos()

    def get_fj_pos(self):
        for _fj in fj:
            c_x = self.pos[0] + _fj[0] * length
            c_y = self.pos[1] + _fj[1] * length

            if not (c_x < 0 or c_y < 0 or c_x >= max_width or c_y >= max_height):
                self.fj_pos.append(f"{c_x}-{c_y}")

    def for_screen(self):
        # 绘制矩形
        rect = (self.pos[0] + 1, self.pos[1] + 1, length - 1, length - 1)
        pygame.draw.rect(screen, "#98F5FF", rect, width=0)

        # 绘制附近地雷数量
        if self.num in "12345678" or True:
            surface = font.render(self.print, False, "#8B0000")
            screen.blit(surface, (self.pos[0] + length // 4, self.pos[1]))

    def del_for_screen(self):
        # 绘制矩形
        rect = (self.pos[0] + 1, self.pos[1] + 1, length - 1, length - 1)
        pygame.draw.rect(screen, "black", rect, width=0)


# 设置地雷
def set_weeper(ge_lis: dict):
    pos_lis = list(ge_lis.keys())

    for _ in range(len(pos_lis) // 6):
        new_wp_index = random.randint(0, len(pos_lis) - 1)
        new_wp_pos = pos_lis.pop(new_wp_index)
        ge_lis[new_wp_pos].weeper = True
        ge_lis[new_wp_pos].num = "!"
        ge_lis[new_wp_pos].print = "!"
        weeper_lis.append(new_wp_pos)


# 设置所有格子周围地雷数
def get_num(ge_lis: dict):
    for pos, ge in ge_lis.items():
        if ge.weeper:
            continue

        num = 0
        for c_pos in ge.fj_pos:
            c_ge = ge_lis.get(c_pos)
            if c_ge and c_ge.weeper:
                num += 1

        ge.num = str(num)
        ge.print = str(num)


# 翻雷
def click_weeper(pos: str, ge_lis: dict):
    cur_ge = ge_lis.get(pos)

    if cur_ge.status != 0:
        return

    if cur_ge.num == "0":
        cur_ge.status = 1

        for _ge_pos in cur_ge.fj_pos:
            click_weeper(_ge_pos, ge_lis)

    elif cur_ge.num in "12345678":
        cur_ge.status = 1

    elif cur_ge.num == "!":
        GLOBAL_VUL["over"] = True

    cur_ge.for_screen()


# 插旗
def this_is_weeper(pos: str, ge_lis: dict):
    cur_ge = ge_lis.get(pos)

    if cur_ge.status == 0:
        cur_ge.status = 2
        cur_ge.print = "*"

        if pos in weeper_lis and cur_ge.weeper:
            weeper_lis.remove(pos)

        is_weeper_lis.append(pos)
        cur_ge.for_screen()
    elif cur_ge.status == 1:
        return
    elif cur_ge.status == 2:
        cur_ge.status = 0
        cur_ge.print = cur_ge.num

        if pos not in weeper_lis:
            weeper_lis.append(pos)

        is_weeper_lis.remove(pos)
        cur_ge.del_for_screen()
