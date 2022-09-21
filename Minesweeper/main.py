from weeper import *
import time


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


def main():
    init()
    set_weeper(ges)
    get_num(ges)

    while True:
        event = pygame.event.poll()

        # Pygame事件处理
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 鼠标左键
                x, y = event.pos
                c_pos = (x - x % length, y - y % length)
                c_k = f"{c_pos[0]}-{c_pos[1]}"
                click_weeper(c_k, ges)

            elif event.button == 3:  # 鼠标右键
                x, y = event.pos
                c_pos = (x - x % length, y - y % length)
            elif event.button == 2:  # 鼠标中键
                pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                screen.fill((0, 0, 0))
                init()
                set_weeper(ges)
                get_num(ges)
            elif event.key == pygame.K_s:
                pass

        # 屏幕刷新
        pygame.display.update()

        time.sleep(0.01)


if __name__ == "__main__":
    main()
