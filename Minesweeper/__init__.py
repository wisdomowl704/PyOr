import os
import yaml
import pygame

with open(f"{os.path.dirname(os.path.realpath(__file__))}/config.yaml", 'r', encoding='utf-8') as f:
    SETTINGS = yaml.load(f, Loader=yaml.FullLoader)

length = SETTINGS["setting"]["box_length"]  # 格子长度
width = SETTINGS["setting"]["width"]  # 横向格子数量
height = SETTINGS["setting"]["height"]  # 纵向格子数量

max_width = width * length  # 屏幕宽度
max_height = height * length  # 屏幕高度

# pygame初始化
pygame.init()
screen = pygame.display.set_mode((max_width + 1, max_height + 1))
pygame.display.set_caption(SETTINGS["setting"]["window_massage"])

# 文字初始化
font = pygame.font.SysFont(pygame.font.get_fonts()[0], length - 1)

weeper_status = {
    0: "null",
    1: "print",
    2: "ok"
}

ges = {}  # 格子map表
