# coding:utf-8
import pygame

# 无需pygame.init()也可直接使用
hero_rect = pygame.Rect(100, 500, 120, 125)

print "英雄的原点 %d %d" % (hero_rect.x, hero_rect.y)
print "英雄的尺寸 %d %d" % (hero_rect.width, hero_rect.height)
print "size:%d %d" % hero_rect.size  # 元组
