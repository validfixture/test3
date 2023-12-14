import pygame
import time

def test_function(display):
    img = pygame.image.load('C:/Users/DocumentEcstasy/Desktop/L-EFLI AP1-PROG17/Main/Course structure documents/PAP Project/test3/img/Battle_Screen_Background.png')
    display.blit(img, (0, 0))

def animation(display, name, frame_number, duration, position, filepath):
    for x in range(frame_number):
        x = pygame.image.load(filepath + x)
        display.blit(x, (position))
        time.sleep(duration/frame_number)

def menu(display, selection, menu_state):
    background_menu = pygame.image.load('img/to delete/background_menu.png')
    setting_1 = pygame.image.load('img/to delete/background_menu1.png')
    setting_2 = pygame.image.load('img/to delete/background_menu2.png')
    setting_3 = pygame.image.load('img/to delete/background_menu3.png')
    setting_4 = pygame.image.load('img/to delete/background_menu4.png')
    setting_5 = pygame.image.load('img/to delete/background_menu5.png')
    setting_6 = pygame.image.load('img/to delete/background_menu6.png')
    setting_7 = pygame.image.load('img/to delete/background_menu7.png')
    setting_8 = pygame.image.load('img/to delete/background_menu8.png')
    background_save = pygame.image.load('img/to delete/background_save.png')
    background_save1 = pygame.image.load('img/to delete/background_save1.png')
    background_save2 = pygame.image.load('img/to delete/background_save2.png')
    
    if menu_state == 'menu':
        display.blit(background_menu, (0,0))
        if selection == 1:
            display.blit(setting_1, (0,0))
        if selection == 2:
            display.blit(setting_2, (0,0))
        if selection == 3:
            display.blit(setting_3, (0,0))
        if selection == 4:
            display.blit(setting_4, (0,0))
        if selection == 5:
            display.blit(setting_5, (0,0))
        if selection == 6:
            display.blit(setting_6, (0,0))
        if selection == 7:
            display.blit(setting_7, (0,0))
        if selection == 8:
            display.blit(setting_8, (0,0))
    if menu_state == 'save':
        display.blit(background_save, (0,0))
        if selection == 1:
            display.blit(background_save1, (0,0))
        if selection == 2:
            display.blit(background_save2, (0,0))

def text_box(display, Ypos):
    text_box_surface = pygame.Surface((160,48))
    tile8 = pygame.image.load('img/tiles/menu/tile8.png')
    tile1 = pygame.image.load('img/tiles/menu/tile1.png')
    tile2 = pygame.image.load('img/tiles/menu/tile2.png')
    tile3 = pygame.image.load('img/tiles/menu/tile3.png')
    tile4 = pygame.image.load('img/tiles/menu/tile4.png')
    tile5 = pygame.image.load('img/tiles/menu/tile5.png')
    tile6 = pygame.image.load('img/tiles/menu/tile6.png')
    tile7 = pygame.image.load('img/tiles/menu/tile7.png')
    tile9 = pygame.image.load('img/tiles/menu/tile9.png')
    tilemap = [[8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2,],
               [7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3,],
               [7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3,],
               [7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3,],
               [7, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 3,],
               [6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4,]]
    y = 0
    for row in tilemap:
        x = 0
        for tile in row:
            if tile == 8:
                text_box_surface.blit(tile8, (x * 8, y * 8))
            if tile == 1:
                text_box_surface.blit(tile1, (x * 8, y * 8))
            if tile == 2:
                text_box_surface.blit(tile2, (x * 8, y * 8))
            if tile == 3:
                text_box_surface.blit(tile3, (x * 8, y * 8))
            if tile == 4:
                text_box_surface.blit(tile4, (x * 8, y * 8))
            if tile == 5:
                text_box_surface.blit(tile5, (x * 8, y * 8))
            if tile == 6:
                text_box_surface.blit(tile6, (x * 8, y * 8))
            if tile == 7:
                text_box_surface.blit(tile7, (x * 8, y * 8))
            if tile == 9:
                text_box_surface.blit(tile9, (x * 8, y * 8))
            x += 1
        y += 1
    display.blit(text_box_surface, (0,Ypos))

def cutscene_travel(display, filename, imgX, imgY, Xdist, Ydist, dur):
    img = pygame.image.load(filename)
    for x in range(dur):
        Xdelta_dist = Xdist / dur
        Ydelta_dist = Ydist / dur
        display.blit(img, (imgX + Xdelta_dist, imgY + Ydelta_dist))

def moving_intro(display, layer1X, layer2X, layer3X, layer4X, speed):
    layer1X = layer1X + (1*speed)
    layer2X = layer2X + (1*speed)
    layer3X = layer3X + (1*speed)
    layer4X = layer4X + (1*speed)

def clefairy_function():
    clefairy_dict = [pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy1.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png'),
                        pygame.image.load('img/intro/phase1_clefairy2.png')]
    return clefairy_dict

def vileplume_function():
    vileplume_dict = [pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume1.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png'),
                        pygame.image.load('img/intro/phase1_vileplume2.png')]
    return vileplume_dict

def diglett_function():
    diglett_dict = [pygame.image.load('img/intro/phase1_diglett1.png'),
                        pygame.image.load('img/intro/phase1_diglett1.png'),
                        pygame.image.load('img/intro/phase1_diglett1.png'),
                        pygame.image.load('img/intro/phase1_diglett1.png'),
                        pygame.image.load('img/intro/phase1_diglett1.png'),
                        pygame.image.load('img/intro/phase1_diglett2.png'),
                        pygame.image.load('img/intro/phase1_diglett2.png'),
                        pygame.image.load('img/intro/phase1_diglett2.png'),
                        pygame.image.load('img/intro/phase1_diglett2.png'),
                        pygame.image.load('img/intro/phase1_diglett2.png'),
                        pygame.image.load('img/intro/phase1_diglett3.png'),
                        pygame.image.load('img/intro/phase1_diglett3.png'),
                        pygame.image.load('img/intro/phase1_diglett3.png'),
                        pygame.image.load('img/intro/phase1_diglett3.png'),
                        pygame.image.load('img/intro/phase1_diglett3.png'),
                        pygame.image.load('img/intro/phase1_diglett4.png'),
                        pygame.image.load('img/intro/phase1_diglett4.png'),
                        pygame.image.load('img/intro/phase1_diglett4.png'),
                        pygame.image.load('img/intro/phase1_diglett4.png'),
                        pygame.image.load('img/intro/phase1_diglett4.png'),
                        pygame.image.load('img/intro/phase1_diglett5.png'),
                        pygame.image.load('img/intro/phase1_diglett5.png'),
                        pygame.image.load('img/intro/phase1_diglett5.png'),
                        pygame.image.load('img/intro/phase1_diglett5.png'),
                        pygame.image.load('img/intro/phase1_diglett5.png'),
                        pygame.image.load('img/intro/phase1_diglett6.png'),
                        pygame.image.load('img/intro/phase1_diglett6.png'),
                        pygame.image.load('img/intro/phase1_diglett6.png'),
                        pygame.image.load('img/intro/phase1_diglett6.png'),
                        pygame.image.load('img/intro/phase1_diglett6.png')]
    return diglett_dict

def zubat_function():
    zubat_dict = [pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat1.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png'),
                        pygame.image.load('img/intro/phase1_zubat2.png')]
    return zubat_dict

def note_animation(display, noteX, noteY):
    note_frame = 0
    note_dict = [pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note1.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note2.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note3.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note4.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png'),
                        pygame.image.load('img/intro/phase1_note5.png')]
    note = note_dict[note_frame]
    note_frame += 1
    if note_frame > 43:
        note_frame = 0
    display.blit(note,(noteX,noteY))

def pikachu_function():
    pikachu_dict = [pygame.image.load('img/intro/phase1_pikachu1.png'),
                    pygame.image.load('img/intro/phase1_pikachu1.png'),
                    pygame.image.load('img/intro/phase1_pikachu1.png'),
                    pygame.image.load('img/intro/phase1_pikachu1.png'),
                    pygame.image.load('img/intro/phase1_pikachu1.png'),
                    pygame.image.load('img/intro/phase1_pikachu2.png'),
                    pygame.image.load('img/intro/phase1_pikachu2.png'),
                    pygame.image.load('img/intro/phase1_pikachu2.png'),
                    pygame.image.load('img/intro/phase1_pikachu2.png'),
                    pygame.image.load('img/intro/phase1_pikachu2.png'),
                    pygame.image.load('img/intro/phase1_pikachu3.png'),
                    pygame.image.load('img/intro/phase1_pikachu3.png'),
                    pygame.image.load('img/intro/phase1_pikachu3.png'),
                    pygame.image.load('img/intro/phase1_pikachu3.png'),
                    pygame.image.load('img/intro/phase1_pikachu3.png')]
    return pikachu_dict

def game_freak_function():
    game_freak_dict = [pygame.image.load('img/intro/game_freak/intro_game_freak5.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak5.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak5.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak6.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak6.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak6.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak7.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak7.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak7.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak8.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak8.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak8.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak9.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak9.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak9.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak10.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak10.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak10.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak11.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak11.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak11.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak12.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak12.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak12.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak13.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak13.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak13.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak14.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak14.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak14.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak15.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak15.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak15.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak16.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak16.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak16.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak17.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak17.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak17.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak18.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak18.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak18.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak19.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak19.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak19.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak20.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak20.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak20.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak21.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak21.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak21.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak22.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak22.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak22.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak23.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak23.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak23.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak24.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak24.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak24.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak25.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak25.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak25.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak26.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak26.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak26.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak27.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak27.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak27.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak28.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak28.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak28.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak29.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak29.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak29.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak30.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak30.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak30.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak31.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak31.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak31.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak32.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak32.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak32.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak33.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak33.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak33.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak34.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak34.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak34.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak35.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak35.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak35.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak36.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak36.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak36.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak37.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak37.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak37.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak38.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak38.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak38.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak39.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak39.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak39.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak40.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak40.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak40.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak41.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak41.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak41.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak42.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak42.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak42.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak43.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak43.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak43.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak44.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak44.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak44.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak45.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak45.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak45.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak46.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak46.png'),
                    pygame.image.load('img/intro/game_freak/intro_game_freak46.png'),]
    return game_freak_dict