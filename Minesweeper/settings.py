import os
import yaml
import pygame

try:
    with open(f"{os.path.dirname(os.path.realpath(__file__))}/config.yaml", 'r', encoding='utf-8') as f:
        SETTINGS = yaml.load(f, Loader=yaml.FullLoader)
except Exception as e:
    length = 20  # 格子长度
    width = 30  # 横向格子数量
    height = 30  # 纵向格子数量
    title = "军少扫雷"
else:
    length = SETTINGS["setting"]["box_length"]  # 格子长度
    width = SETTINGS["setting"]["width"]  # 横向格子数量
    height = SETTINGS["setting"]["height"]  # 纵向格子数量
    title = SETTINGS["setting"]["window_massage"]

max_width = width * length  # 屏幕宽度
max_height = height * length  # 屏幕高度

# pygame初始化
pygame.init()
screen = pygame.display.set_mode((max_width + 1, max_height + 1))
pygame.display.set_caption(title)

# 文字初始化
font = pygame.font.SysFont(pygame.font.get_fonts()[0], length - 1)

# 结束文字
o_font = pygame.font.SysFont(pygame.font.get_fonts()[0], max_width // 8)
over_font = o_font.render("GAME OVER", False, "red")

# 胜利文字
w_font = pygame.font.SysFont(pygame.font.get_fonts()[0], max_width // 8)
win_font = o_font.render("YOU WIN", False, "red")

weeper_status = {
    0: "null",
    1: "print",
    2: "ok"
}

GLOBAL_VUL = {
    "over": False,  # 游戏结束
    "win": False,  # 游戏胜利
}

weeper_lis = []
is_weeper_lis = []

ges = {}  # 格子map表
