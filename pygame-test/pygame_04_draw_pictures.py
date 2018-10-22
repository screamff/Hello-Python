# coding: utf-8

import pygame

pygame.init()
# 创建游戏窗口640x480
screen = pygame.display.set_mode((640, 640))
# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# blit绘制图像
screen.blit(bg, (0, 20))
# update 更新屏幕显示
pygame.display.update()
