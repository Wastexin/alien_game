#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Aline
import game_functions as gf
from pygame.sprite import Group
from game_GameStats import GameStats
from button import Button
from scoreboard import  Scoreboard

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_width))
    pygame.display.set_caption("Alien Invasion")

    #创建Play按钮
    play_button = Button(ai_settings,screen,"Play")


    #创建一个用于储存游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #创造一艘飞船、一个用于储存子弹的编组和一个外星人编组
    ship = Ship(screen,ai_settings)
    aliens = Group()
    bullets = Group()

    #设置背景色
    bg_color = (230,230,230)


    #创建一个外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)


    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,
                        aliens,bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                         play_button)





run_game()





