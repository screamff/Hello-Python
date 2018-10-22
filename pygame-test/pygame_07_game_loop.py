# coding: utf-8

import pygame

pygame.init()
# 创建游戏窗口 widthxhight
screen = pygame.display.set_mode((480, 700))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# blit绘制图像
screen.blit(bg, (0, 20))

# 绘制英雄战机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 300))
# 统一更新屏幕显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()
# 每次调用clock.tick()会依据上一次调用时间设置延时
i = 0
while True:
    clock.tick(60)
    i += 1
    print i
