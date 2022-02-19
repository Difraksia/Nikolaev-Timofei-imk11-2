import pygame
from .....utils import QuitGame

# Меню проигрыша
def GameEndIterface(screen, cfg, resource_loader, is_win=True):
    background_img = resource_loader.images['others']['background']
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    font = resource_loader.fonts['end']

    gameover_img = resource_loader.images['others']['gameover']
    gameover_img = pygame.transform.scale(gameover_img, (150, 75))
    gameover_img_rect = gameover_img.get_rect()
    gameover_img_rect.midtop = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 8
    gameover_flash_time = 25
    gameover_flash_count = 0
    gameover_show_flag = True

    if is_win:
        font_render = font.render('Поздравляю, вы выиграли!', True, color_white)
    else:
        font_render = font.render('Извините, вы проиграли!', True, color_white)
    font_rect = font_render.get_rect()
    font_rect.centerx, font_rect.centery = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 3

    tank_cursor = resource_loader.images['player']['player1'][0].convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()
    restart_render_white = font.render('Заново', True, color_white)
    restart_render_red = font.render('Заново', True, color_red)
    restart_rect = restart_render_white.get_rect()
    restart_rect.left, restart_rect.top = cfg.SCREENSIZE[0] / 2.4, cfg.SCREENSIZE[1] / 2
    quit_render_white = font.render('Выйти', True, color_white)
    quit_render_red = font.render('Выйти', True, color_red)
    quit_rect = quit_render_white.get_rect()
    quit_rect.left, quit_rect.top = cfg.SCREENSIZE[0] / 2.4, cfg.SCREENSIZE[1] / 1.6
    is_quit_game = False

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return is_quit_game
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    is_quit_game = not is_quit_game
        screen.blit(background_img, (0, 0))
        gameover_flash_count += 1
        if gameover_flash_count > gameover_flash_time:
            gameover_show_flag = not gameover_show_flag
            gameover_flash_count = 0
        if gameover_show_flag:
            screen.blit(gameover_img, gameover_img_rect)
        screen.blit(font_render, font_rect)
        if not is_quit_game:
            tank_rect.right, tank_rect.top = restart_rect.left-10, restart_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(restart_render_red, restart_rect)
            screen.blit(quit_render_white, quit_rect)
        else:
            tank_rect.right, tank_rect.top = quit_rect.left-10, quit_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(restart_render_white, restart_rect)
            screen.blit(quit_render_red, quit_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)

# Меню старта
def GameStartInterface(screen, cfg, resource_loader):
    background_img = resource_loader.images['others']['background']
    color_white = (255, 255, 255)
    color_red = (255, 0, 0)
    font = resource_loader.fonts['start']
    logo_img = resource_loader.images['others']['logo']
    logo_img = pygame.transform.scale(logo_img, (446, 70))
    logo_rect = logo_img.get_rect()
    logo_rect.centerx, logo_rect.centery = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] // 4
    tank_cursor = resource_loader.images['player']['player1'][0].convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()

    player_render_white = font.render('1 Игрок', True, color_white)
    player_render_red = font.render('1 Игрок', True, color_red)
    player_rect = player_render_white.get_rect()
    player_rect.left, player_rect.top = cfg.SCREENSIZE[0] / 2.8, cfg.SCREENSIZE[1] / 2.5
    players_render_white = font.render('2 Игрока', True, color_white)
    players_render_red = font.render('2 Игрока', True, color_red)
    players_rect = players_render_white.get_rect()
    players_rect.left, players_rect.top = cfg.SCREENSIZE[0] / 2.8, cfg.SCREENSIZE[1] / 2

    game_tip = font.render('нажмите <Enter> чтобы начать', True, color_white)
    game_tip_rect = game_tip.get_rect()
    game_tip_rect.centerx, game_tip_rect.top = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 1.4
    game_tip_flash_time = 25
    game_tip_flash_count = 0
    game_tip_show_flag = True

    clock = pygame.time.Clock()
    is_dual_mode = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return is_dual_mode
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    is_dual_mode = not is_dual_mode
        screen.blit(background_img, (0, 0))
        screen.blit(logo_img, logo_rect)
        game_tip_flash_count += 1
        if game_tip_flash_count > game_tip_flash_time:
            game_tip_show_flag = not game_tip_show_flag
            game_tip_flash_count = 0
        if game_tip_show_flag:
            screen.blit(game_tip, game_tip_rect)
        if not is_dual_mode:
            tank_rect.right, tank_rect.top = player_rect.left-10, player_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(player_render_red, player_rect)
            screen.blit(players_render_white, players_rect)
        else:
            tank_rect.right, tank_rect.top = players_rect.left-10, players_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(player_render_white, player_rect)
            screen.blit(players_render_red, players_rect)
        pygame.display.update()
        clock.tick(cfg.FPS)

# Экран загрузки уровня
def SwitchLevelIterface(screen, cfg, resource_loader, level_next=1):
    background_img = resource_loader.images['others']['background']
    color_white = (255, 255, 255)
    color_gray = (192, 192, 192)
    font = resource_loader.fonts['switch']
    logo_img = resource_loader.images['others']['logo']
    logo_img = pygame.transform.scale(logo_img, (446, 70))
    logo_rect = logo_img.get_rect()
    logo_rect.centerx, logo_rect.centery = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] // 4

    font_render = font.render('Загрузка ресурсов игры, Вы войдёте на уровень-%s' % level_next, True, color_white)
    font_rect = font_render.get_rect()
    font_rect.centerx, font_rect.centery = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 2

    gamebar = resource_loader.images['others']['gamebar'].convert_alpha()
    gamebar_rect = gamebar.get_rect()
    gamebar_rect.centerx, gamebar_rect.centery = cfg.SCREENSIZE[0] / 2, cfg.SCREENSIZE[1] / 1.4
    tank_cursor = resource_loader.images['player']['player1'][0].convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()
    tank_rect.left = gamebar_rect.left
    tank_rect.centery = gamebar_rect.centery

    load_time_left = gamebar_rect.right - tank_rect.right + 8

    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                QuitGame()
        if load_time_left <= 0:
            return
        screen.blit(background_img, (0, 0))
        screen.blit(logo_img, logo_rect)
        screen.blit(font_render, font_rect)
        screen.blit(gamebar, gamebar_rect)
        screen.blit(tank_cursor, tank_rect)
        pygame.draw.rect(screen, color_gray, (gamebar_rect.left+8, gamebar_rect.top+8, tank_rect.left-gamebar_rect.left-8, tank_rect.bottom-gamebar_rect.top-16))
        tank_rect.left += 1
        load_time_left -= 1
        pygame.display.update()
        clock.tick(cfg.FPS)