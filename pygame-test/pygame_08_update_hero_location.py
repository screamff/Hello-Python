# coding: utf-8

import pygame

pygame.init()
# 创建游戏窗口 widthxhight
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# blit绘制图像
screen.blit(bg, (0, 0))

# 绘制英雄战机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
# 统一更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 1. 定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)
# 每次调用clock.tick()会依据上一次调用时间设置延时
i = 0
while True:
    clock.tick(60)
    # 2. 修改飞机的位置
    hero_rect.y -= 1
    # 3. 调用blit方法绘制图像，首先覆盖原图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4. 调用update更新显示
    pygame.display.update()
