# coding:utf-8
import random
import pygame

# 屏幕大小常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 刷新率
FRAME_PER_SECOND = 60
# 英雄发射子弹时间
HERO_FIRE_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """飞机游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类init方法
        super(GameSprite, self).__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 调用父类方法实现精灵创建
        super(Background, self).__init__("./images/background.png")
        # 判断是否为交替图像，如果是，设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类方法实现
        super(Background, self).update()
        # 2.判断是否移除屏幕，如果移除屏幕，将图像设置到屏幕上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        # 1.调用父类方法，创建敌机精灵，指定图片
        super(Enemy, self).__init__("./images/enemy1.png")
        # 2.指定敌机初始速度
        self.speed = random.randint(1, 3)
        # 3.指定敌机初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)
        # 爆炸动画参数
        self.bomb = 0
        self.counter = 0

    def update(self):

        # 1.调用父类方法
        super(Enemy, self).update()
        # 2.判断是否飞出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            print "out of screen, remove"
            # kill方法可以将精灵从所有精灵组移除，被自动销毁
            self.kill()
        # 判断是否爆炸
        bomb_gif = {2: "./images/enemy1_down1.png",
                    6: "./images/enemy1_down2.png",
                    10: "./images/enemy1_down3.png",
                    14: "./images/enemy1_down4.png"
                    }
        if self.bomb:
            self.counter += 1
            self.speed = 0
        if self.counter in bomb_gif.keys():
            self.image = pygame.image.load(bomb_gif[self.counter])

        if self.counter > 14:
            self.kill()

    def __del__(self):
        print "enemy dead, %s" % self.rect


class Hero(GameSprite):
    """英雄精灵"""

    def __init__(self):
        super(Hero, self).__init__("./images/me1.png", 0)
        # 设置英雄初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 创建子弹精灵组
        self.bullets = pygame.sprite.Group()
        # 爆炸动画检测
        self.bomb = 0
        self.counter = 0

    def update(self):
        # 英雄水平方向移动
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

        # 爆炸动画
        bomb_gif = {2: "./images/me_destroy_1.png",
                    10: "./images/me_destroy_2.png",
                    18: "./images/me_destroy_3.png",
                    26: "./images/me_destroy_4.png"
                    }

        if self.bomb:
            self.counter += 1

        if self.counter in bomb_gif.keys():
            self.image = pygame.image.load(bomb_gif[self.counter])

        if self.counter > 14:
            self.kill()




    def fire(self):
        # 发射子弹
        print "fire fire"
        for i in range(2):
            bullet = Bullet()

            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx

            self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super(Bullet, self).__init__("./images/bullet1.png", -2)

    def update(self):
        super(Bullet, self).update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print "bullet dead"
