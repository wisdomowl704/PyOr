from settings import *
from weeper import *


# 初始化
def init():
    # 添加格子
    for x in range(width):
        for y in range(height):
            ges[f"{x * length}-{y * length}"] = Ge([x * length, y * length])

    # 绘制扫雷图
    for pos, ge in ges.items():
        for c_ge_line_pos in ge.line:
            pygame.draw.line(screen, (225, 225, 225), c_ge_line_pos[0], c_ge_line_pos[1], 1)

    # 设置地雷
    set_weeper(ges)

    # 设置格子信息
    get_num(ges)


# 事件处理
def event_run(event):
    # Pygame事件处理
    if event.type == pygame.QUIT:
        pygame.quit()
        exit(0)

    elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标事件
        if GLOBAL_VUL['over']:
            pass
        elif event.button == 1:  # 鼠标左键
            x, y = event.pos
            c_pos = (x - x % length, y - y % length)
            c_k = f"{c_pos[0]}-{c_pos[1]}"
            click_weeper(c_k, ges)
        elif event.button == 3:  # 鼠标右键
            x, y = event.pos
            c_pos = (x - x % length, y - y % length)
            c_k = f"{c_pos[0]}-{c_pos[1]}"
            this_is_weeper(c_k, ges)

    elif event.type == pygame.KEYDOWN:  # 键盘事件
        if event.key == pygame.K_r:
            screen.fill((0, 0, 0))
            init()
            GLOBAL_VUL['over'] = False
            pygame.display.set_caption("军少扫雷")


# 持续检测处理
def every():
    # 游戏失败
    if GLOBAL_VUL['over']:
        font_width = over_font.get_width()
        font_height = over_font.get_height()
        screen.blit(over_font, (max_width // 2 - font_width // 2, max_height // 2 - font_height // 2))
        pygame.display.set_caption("you lost, 按R键重置")

    # 游戏胜利
    if len(weeper_lis) == 0 and len(is_weeper_lis) == len(ges) // 6:
        font_width = win_font.get_width()
        font_height = win_font.get_height()
        screen.blit(win_font, (max_width // 2 - font_width // 2, max_height // 2 - font_height // 2))
        pygame.display.set_caption("you win, 按R键重置")
