import pygame
from sys import exit
import json
from scripts import menu, text_box, clefairy_function, vileplume_function, diglett_function, zubat_function, note_animation, pikachu_function, game_freak_function

pygame.init()

#Set display surface size and scaling
screen_size = (640,576)
screen = pygame.display.set_mode((screen_size))
display = pygame.Surface((160,144))

#Set window title and icon
pygame.display.set_caption('Pokémon Python Version')
display_icon = pygame.image.load('img/title_screen/icon.png')
pygame.display.set_icon(display_icon)

#Set framerate
clock = pygame.time.Clock()

#Game class
class Game():
    def __init__(self):
        self.state = 'game_freak'

    def state_manager(self):
        if self.state == 'game_freak':
            self.game_freak()
        if self.state == 'intro':
            self.intro()
        if self.state == 'title_screen':
            self.title_screen()
        if self.state == 'main_menu':
            self.main_menu()
        if self.state == 'main_game':
            self.main_game()

    def game_freak(self):
        #Iniating Game Freak sprites and variables
        frametime = 0
        copyright = pygame.image.load('img/intro/game_freak/intro_copyright.png')
        game_freak_dict = game_freak_function()
        game_freak_frame = 0
        game_freak_last = pygame.image.load('img/intro/game_freak/intro_game_freak47.png')

        #Audio
        pygame.mixer_music.load('sound/bgm/bgm_game_freak.ogg')
        pygame.mixer.music.set_volume(.5)

        #Logic loop Game Freak
        while self.state == 'game_freak':
            #Handling exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #Handling input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = 'intro'
            
            #Rendering display surface scaling
            display_upscaled = pygame.transform.scale(display, screen_size)
            screen.blit(display_upscaled, (0,0))

            frametime += 1
            
            #Rendering copyright information and Game Freak logo
            if frametime == 1:
                pygame.mixer_music.play()

            if frametime >= 0 and frametime <= 120:
                display.blit(copyright, (0,0))

            if frametime > 180:
                if game_freak_frame > 125:
                    game_freak_frame = 125
                game_freak = game_freak_dict[game_freak_frame]
                game_freak_frame += 1
                display.blit(game_freak,(0,0))
            if frametime > 360:
                display.blit(game_freak_last, (0,0))

            #Move to Title Screen
            if frametime == 570:
                self.state = 'intro'

            #Debugging
            print(frametime/60)

            pygame.display.update()
            clock.tick(60)

    def intro(self):
        #Iniating intro fade sprites and variables
        pichu1 = pygame.image.load('img/intro/phase1_pichu1.png')
        pichu2 = pygame.image.load('img/intro/phase1_pichu2.png')
        pichu3 = pygame.image.load('img/intro/phase1_pichu3.png')
        pichuX = 0
        pichuX_difference = .04
        pichuY = 40
        fade = pygame.image.load('img/intro/game_freak/intro_game_freak47.png')
        fade_alpha = 255

        #Initiating intro phase 1/2 backgrounds
        phase1_display = pygame.Surface((256,256))
        phase1_layer1 = pygame.image.load('img/intro/phase1_layer1.png')
        phase1_layer2 = pygame.image.load('img/intro/phase1_layer2.png')
        phase1_layer3 = pygame.image.load('img/intro/phase1_layer3.png')
        phase1_layer4 = pygame.image.load('img/intro/phase1_layer4.png')

        #Initiating intro phase 1 sprites and variables
        layer1X_difference = .001
        layer2X_difference = .005
        layer3X_difference = .01
        layer4X_difference = .04
        clefairy_dict = clefairy_function()
        clefairy_frame = 0
        clefairyX = -13
        clefairyX_difference = .01
        vileplume_dict = vileplume_function()
        vileplume_frame = 0
        vileplumeX = -35
        vileplumeX_difference = .01
        diglett_dict = diglett_function()
        diglett_frame = 0
        diglettX = -30
        diglettX_difference = .01
        zubat_dict = zubat_function()
        zubat_frame = 0
        zubatX = 50
        shedinja = pygame.image.load('img/intro/phase1_shedinja.png')
        shedinjaX = 50
        shedinjaY = 112
        snorlax = pygame.image.load('img/intro/phase1_snorlax.png')
        snorlaxX = -60
        minunplusle = pygame.image.load('img/intro/phase1_minunplusle1.png')
        minunplusleX = -83
        minunplusleY = 112
        pikachu_dict = pikachu_function()
        pikachu_frame = 0
        pikachuX = 60
        unown = pygame.image.load('img/intro/phase1_unown.png')
        unownX = -160

        #Iniating intro phase 3 backgrounds
        background = pygame.image.load('img/intro/background.png')
        floor = pygame.image.load('img/intro/floor.png')
        groudon = pygame.image.load('img/intro/groudon.png')
        intro_static = pygame.image.load('img/intro/intro_static.png')
        intro_static2 = pygame.image.load('img/intro/intro_static2.png')
        intro_animate = pygame.image.load('img/intro/intro_animate.png')

        #Initiating intro phase 3 cuts
        phase3_cut1 = pygame.Surface((160,144))
        phase3_cut2 = pygame.Surface((160,144))
        phase3_cut3 = pygame.Surface((160,144))

        #Initiating intro animation variables
        frametime = 0

        is_moving = False
        phase1X = -0
        phase1Y = -112
        layer1X = -160
        layer1Y = 0
        layer2X = -160
        layer2Y = 0
        layer3X = -320
        layer3Y = 0
        layer4X = -1024
        layer4Y = 0

        backgroundY = -1
        floorY = -1
        groudonY = -2
        groudon_transparency = 0
        transparency_difference = 5
        animation_count = 0

        #Audio
        pygame.mixer_music.load('sound/bgm/bgm_opening.ogg')
        pygame.mixer.music.set_volume(.5)
        sfx_intro_appear = pygame.mixer.Sound('sound/sfx/sfx_intro_appear.ogg')
        sfx_intro_appear.set_volume(.3)
        sfx_intro_blink = pygame.mixer.Sound('sound/sfx/sfx_intro_blink.ogg')
        sfx_intro_blink.set_volume(.3)

        #Logic loop intro
        while self.state == 'intro':
            #Handling exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #Handling input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state = 'title_screen'

            #Rendering display surface scaling
            display_upscaled = pygame.transform.scale(display, screen_size)
            screen.blit(display_upscaled, (0,0))

            frametime += 1

            #Rendering first phase animation
            display.blit(phase1_display,(phase1X,phase1Y))  #Rendering phase 1 backgrounds as base in phase 1 surface
            phase1_display.blit(phase1_layer1,(layer1X,layer1Y))
            phase1_display.blit(phase1_layer2,(layer2X,layer2Y))
            phase1_display.blit(phase1_layer3,(layer3X,layer3Y))            

            if frametime >= 0 and frametime <= 16:   #Rendering Pichu reveal and sound
                display.blit(pichu1, (pichuX,pichuY))
                pichuY -= 2.5
            if frametime == 1:
                sfx_intro_appear.play()

            if frametime > 15 and frametime <= 170:    #Rendering Pichu pause
                display.blit(pichu1, (pichuX,pichuY))

            if frametime == 80 or frametime == 81 or frametime == 82 or frametime == 83 or frametime == 84 or frametime == 85 or frametime == 100 or frametime == 101 or frametime == 102 or frametime == 103 or frametime == 104 or frametime == 105:  #Rendering Pichu blinks and sound
                display.blit(pichu2, (0,0))
            if frametime == 80 or frametime == 100:
                sfx_intro_blink.play()

            if frametime > 170 and pichuX < 160:    #Rendering Pichu animation
                display.blit(pichu3, (pichuX,0))

            if frametime == 170:    #Playing BGM once Pichu animation starts
                pygame.mixer_music.play()

            if frametime >= 170 and frametime <= 260:   #Pan left to reveal Pokemon
                pichuX += 1
                layer1X += .025
                layer2X += .125
                layer3X += .25
                clefairyX += .25
                vileplumeX += .25

            if frametime >= 170 and frametime <= 700:   #Render Clefairy, Vileplume and Shedinja
                if clefairy_frame > 63:
                    clefairy_frame = 0
                clefairy = clefairy_dict[clefairy_frame]
                clefairy_frame += 1
                phase1_display.blit(clefairy,(clefairyX,112))
                if vileplume_frame > 63:
                    vileplume_frame = 0
                vileplume = vileplume_dict[vileplume_frame]
                vileplume_frame += 1
                phase1_display.blit(vileplume, (vileplumeX,112))
                phase1_display.blit(shedinja, (shedinjaX, shedinjaY))
                shedinjaY -= 1
                shedinjaX -= 1

            if frametime < 200:  #Fade out for 30 frames (500ms) after initial Pichu reveal
                phase1_display.blit(fade,(0,112))
            if frametime > 170:
                fade.set_alpha(fade_alpha)
                fade_alpha -= 8.5

            if frametime >= 350 and frametime <= 700: #Render Diglett at t=3.0
                if diglett_frame > 29:
                    diglett_frame = 29
                diglett = diglett_dict[diglett_frame]
                diglett_frame += 1
                phase1_display.blit(diglett, (diglettX,109))

            if frametime > 440 and frametime <= 500: #Render Zubat flying at t=3.75 before the music transition
                if zubat_frame > 14:
                    zubat_frame = 0
                zubat = zubat_dict[zubat_frame]
                zubat_frame += 2
                phase1_display.blit(zubat,(zubatX,112))
                zubatX -= 8

            if frametime == 485:  #Make background move at t=5.75, a second before the music transition
                is_moving = True
            
            if is_moving == True: #Make backgrounds move
                layer1X_difference += .001
                layer2X_difference += .005
                layer3X_difference += .01
                clefairyX_difference += .01
                vileplumeX_difference += .01
                diglettX_difference += .01
                layer4X_difference += .04
                pichuX_difference += .04
                layer1X += layer1X_difference
                layer2X += layer2X_difference
                layer3X += layer3X_difference
                clefairyX += clefairyX_difference
                vileplumeX += vileplumeX_difference
                diglettX += diglettX_difference
                pichuX += pichuX_difference
                if phase1Y == -112:
                    layer4X += layer4X_difference
                else:
                    layer4X = 256
                if layer1X_difference > .1:
                    layer1X_difference = .1
                if layer2X_difference > .5:
                    layer2X_difference = .5
                if layer3X_difference > 1:
                    layer3X_difference = 1
                if clefairyX_difference > 1:
                    clefairyX_difference = 1
                if vileplumeX_difference > 1:
                    vileplumeX_difference = 1
                if diglettX_difference > 1:
                    diglettX_difference = 1
                if layer4X_difference > 4:
                    layer4X_difference = 4
                if pichuX_difference > 4:
                    pichuX_difference = 4              
              
            if layer1X > 0:
                layer1X = -160
            if layer2X > 0:
                layer2X = -160
            if layer3X > 0:
                layer3X = -320
            if layer4X > 256:
                layer4X = -1024

            if frametime >= 615 and frametime <= 1310:   #Render Snorlax
                phase1_display.blit(snorlax, (snorlaxX, 112))
                snorlaxX += 1

            # if frametime >= 830 and frametime <= 6500:    #Render Unown or other Pokemon in the background
            #     phase1_display.blit(unown, (unownX,112))
            #     unownX += .25
            
            if frametime == 830:    #Set the ZubatX position to 0 to initiate Zubat sequence
                zubatX = -160
            if frametime >= 830 and frametime <= 1380 and zubatX < -80:    #Render Zubat from the left edge of the screen and have him follow until the mid-point
                if zubat_frame > 14:
                    zubat_frame = 0
                zubat = zubat_dict[zubat_frame]
                zubat_frame += 1
                phase1_display.blit(zubat,(zubatX,112))
                zubatX += .5
            elif zubatX == -80:
                if zubat_frame > 14:
                    zubat_frame = 0
                zubat = zubat_dict[zubat_frame]
                zubat_frame += 1
                phase1_display.blit(zubat,(zubatX,112))

            if frametime >= 830 and frametime <= 1380 and zubatX < -80:    #Render Pikachu from the left edge of the screen and have him follow until the mid-point
                if pikachu_frame > 13:
                    pikachu_frame = 0
                pikachu = pikachu_dict[pikachu_frame]
                pikachu_frame += 1
                phase1_display.blit(pikachu,(pikachuX,112))
                pikachuX -= .5
            elif zubatX == -80:
                if pikachu_frame > 13:
                    pikachu_frame = 0
                pikachu = pikachu_dict[pikachu_frame]
                pikachu_frame += 1
                phase1_display.blit(pikachu,(pikachuX,112))

            # if frametime >= 1100 and frametime <= 1310 and minunplusleX < 80 - 39:    #Render Plusle and Minun skipping from left
            #     phase1_display.blit(minunplusle, (minunplusleX,minunplusleY))
            #     minunplusleX += .5
            #     note_animation(phase1_display, minunplusleX, 112+56)
            # elif minunplusleX == 80 - 39:
            #     phase1_display.blit(minunplusle, (minunplusleX,minunplusleY))
            #     note_animation(phase1_display, minunplusleX, 112+56)

            #Rendering phase 1 foreground
            phase1_display.blit(phase1_layer4,(layer4X,layer4Y))

            #Rendering second phase animation
            if frametime > 1320 + 170 and phase1Y < 0:
                phase1Y += 1
                layer2Y += .1
                layer3Y += .1


            #Rendering third phase animation
            if frametime >= 2007 + 170 and frametime < 2367 + 170:  #background pan down
                display.blit(background, (0, backgroundY))
                display.blit(floor, (0, floorY))
                display.blit(groudon, (0, groudonY))
                backgroundY -= 0.4
                floorY -= 0.8
                groudonY -= 1.2

            if frametime >= 2007 + 170 and frametime <= 2007 + 170 + 30:    #Cut 1
                phase3_cut1.fill((255,0,0))
                display.blit(phase3_cut1, (0,0))

            if frametime >= 2127 + 170 and frametime <= 2127 + 170 + 30:    #Cut 2
                phase3_cut2.fill((0,255,0))
                display.blit(phase3_cut2, (0,0))

            if frametime >= 2247 + 170 and frametime <= 2247 + 170 + 30:    #Cut 3
                phase3_cut3.fill((0,0,255))
                display.blit(phase3_cut3, (0,0))

            if frametime >= 2367 + 170: #Static background fix
                display.blit(intro_static, (0,0))

            if frametime >= 2467 + 170: #Static2 background fix
                display.blit(intro_static2, (0,0))

            if frametime >= 2407 + 170 and animation_count <= 1 or frametime > 2490 + 170 and groudon_transparency < 255:   #Groudon first and second animation cycle                
                display.blit(intro_static, (0,0))
                if groudon_transparency == 255:
                    transparency_difference = -15
                if groudon_transparency == 0:
                    transparency_difference = 15
                    animation_count += 1
                groudon_transparency += transparency_difference
                intro_static2.set_alpha(groudon_transparency)
                display.blit(intro_static2, (0,0))
            elif frametime >= 2407 + 170 and frametime <= 2490 + 170 and animation_count == 2:
                display.blit(intro_static, (0,0))
                
            if frametime >= 2520 + 170 and frametime <= 2610 + 170 and groudon_transparency == 255:    #Groudon cry
                display.blit(intro_animate, (0,0))           
            elif frametime > 2610 + 170:
                display.blit(intro_static2, (0,0))

            #Move to Title Screen
            if frametime == 2670 + 170:
                self.state = 'title_screen'

            #Debugging
            print(frametime/60)

            pygame.display.update()
            clock.tick(60)

    def title_screen(self):
        #Initiating Title Screen images
        background = pygame.image.load('img/title_screen/background.png')
        floor = pygame.image.load('img/title_screen/floor.png')
        groudon_base2 = pygame.image.load('img/title_screen/groudon_Base2.png')
        groudon_base = pygame.image.load('img/title_screen/groudon_Base.png')
        groudon_animate = pygame.image.load('img/title_screen/groudon_animate.png')
        logo = pygame.image.load('img/title_screen/logo.png')
        logo_left = pygame.image.load('img/title_screen/logo_left.png')
        logo_right = pygame.image.load('img/title_screen/logo_right.png')
        made_by = pygame.image.load('img/title_screen/made_by.png')

        #Initiating particles
        #add code here lel

        #Initiating Groudon animation and UI variables
        transparency = 255
        transparency_difference = 0
        framerate = 0
        leftX = -160
        rightX = 160
        
        #Audio
        pygame.mixer_music.load('sound/bgm/bgm_main_theme.ogg')
        pygame.mixer.music.set_volume(.5)
        intro_whoosh = pygame.mixer.Sound('sound/sfx/sfx_intro.ogg')
        intro_whoosh.set_volume(.3)
        intro_cry = pygame.mixer.Sound('sound/sfx/sfx_intro_cry.ogg')
        intro_cry.set_volume(.5)
        delay = 81

        #Logic loop main menu
        while self.state == 'title_screen':
            #Handling exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #Handling input: On keypress, play audio and set up Main Menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and delay > 80:
                        pygame.mixer_music.stop()
                        delay = 0
            
            #Rendering display surface scaling
            display_upscaled = pygame.transform.scale(display, screen_size)
            screen.blit(display_upscaled, (0,0))

            #Rendering backgrounds
            display.blit(background,(0,0))
            display.blit(floor,(0,0))
            display.blit(groudon_base2,(0,0))

            #Rendering Groudon animation transparency
            if transparency == 255 and framerate > 60:
                transparency_difference = -5

            if transparency == 0 and framerate > 60:
                transparency_difference = 5
            
            transparency += transparency_difference
            groudon_base.set_alpha(transparency)
            display.blit(groudon_base,(0,0))
            framerate += 1

            #Rendering logo
            if framerate < 40:
                display.blit(logo_left,(leftX,0))
                display.blit(logo_right,(rightX,0))
                leftX += 4
                rightX -= 4

            if framerate > 40:
                display.blit(logo,(0,0))
                display.blit(made_by,(0,0))

            #Playing BGM on start, animation and setting up Main Menu transition on keypress
            if framerate == 1:
                intro_whoosh.play()
            if framerate == 60 and delay > 80:
                pygame.mixer_music.play()

            if delay == 0:
                intro_cry.play()
            if delay >= 0 and delay <= 80:
                display.blit(groudon_animate, (0,0))
            if delay == 80:
                self.state = 'main_menu'
            delay += 1

            #Debugging
            print(transparency, transparency_difference, framerate, leftX, rightX)

            #Update display and set framerate
            pygame.display.update()
            clock.tick(60)

    def main_menu(self):
        #Initiating Main Menu images
        background_false = pygame.image.load('img/to delete/background_main_menu_false.png')
        background_true = pygame.image.load('img/to delete/background_main_menu_true.png')
        setting_1 = pygame.image.load('img/to delete/main_menu_1.png')
        setting_2 = pygame.image.load('img/to delete/main_menu_2.png')
        setting_3 = pygame.image.load('img/to delete/main_menu_3.png')

        #Initiating Main Menu variables
        selection = 1
        saved_data = False

        #Checking for save file
        try:
            with open('save_file.txt') as save_file:
                saved_data = True
        except:
            saved_data = False

        while self.state == 'main_menu':
        #Logic loop main menu
            for event in pygame.event.get():
                #Handling exit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #Handling input: On keypresses, adjust selection variable and perform actions accordingly
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selection -= 1
                    if event.key == pygame.K_DOWN:
                        selection += 1
                    if event.key == pygame.K_c:
                        if saved_data == False and selection == 1:
                            self.state = 'main_game'
                        if saved_data == False and selection == 2:
                            pass
                        if saved_data == True and selection == 1:
                            pass
                        if saved_data == True and selection == 2:
                            self.state = 'main_game'
                        if saved_data == True and selection == 3:
                            pass

            #Rendering display surface scaling
            display_upscaled = pygame.transform.scale(display, screen_size)
            screen.blit(display_upscaled, (0,0))

            #Resetting selection variable
            if saved_data == False:
                if selection > 2:
                    selection = 2
                if selection < 1:
                    selection = 1
            if saved_data == True:
                if selection > 3:
                    selection = 3
                if selection < 1:
                    selection = 1

            #Rendering backgrounds
            if saved_data == False:
                display.blit(background_false,(0,0))
                if selection == 1:
                    display.blit(setting_1, (0,0))
                else:
                    display.blit(setting_2, (0,0))
            if saved_data == True:
                display.blit(background_true, (0,0))
                if selection == 1:
                    display.blit(setting_1, (0,0))
                if selection == 2:
                    display.blit(setting_2, (0,0))
                if selection == 3:
                    display.blit(setting_3, (0,0))

            #Debugging
            print(selection, saved_data)

            #Update display and set framerate
            pygame.display.update()
            clock.tick(60)

    def main_game(self):
        #Initiating tilemap (40x36 tilemap, 8px tiles)
        map_surface = pygame.Surface((320, 288))
        game_map = [[107, 107, 107, 107, 107, 107, 459, 460, 107, 107, 107, 107, 107, 107, 459, 460, 105, 105, 105, 105, 459, 460, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 459, 460, 107, 107,],
                    [107, 107, 107, 107, 107, 107, 495, 496, 107, 107, 107, 107, 107, 107, 495, 496, 105, 105, 105, 105, 495, 496, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 495, 496, 107, 107,],
                    [459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 105, 105, 105, 105, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460,],
                    [495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 105, 105, 105, 105, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 444, 445, 446, 446, 446, 446, 449, 450, 465, 465, 465, 465, 465, 465, 465, 465, 444, 445, 446, 446, 446, 446, 449, 450, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 480, 481, 482, 482, 482, 482, 485, 486, 465, 465, 465, 465, 465, 465, 465, 465, 480, 481, 482, 482, 482, 482, 485, 486, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 416, 417, 418, 419, 418, 418, 521, 522, 465, 465, 465, 465, 465, 465, 465, 465, 416, 417, 418, 419, 418, 418, 521, 522, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 552, 553, 553, 553, 553, 553, 553, 558, 465, 465, 465, 465, 465, 465, 465, 465, 552, 553, 553, 553, 553, 553, 553, 558, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 531, 532, 588, 589, 590, 591, 418, 418, 589, 594, 465, 465, 465, 465, 465, 465, 531, 532, 588, 589, 590, 591, 418, 418, 589, 594, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 567, 568, 624, 625, 626, 627, 625, 625, 625, 630, 465, 465, 465, 465, 465, 465, 567, 568, 624, 625, 626, 627, 625, 625, 625, 630, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 451, 452, 452, 452, 452, 452, 452, 452, 452, 452, 452, 458, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 487, 488, 488, 488, 488, 488, 488, 488, 488, 488, 488, 494, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 461, 461, 461, 461, 461, 461, 531, 532, 465, 465, 465, 465, 487, 488, 488, 488, 488, 488, 488, 488, 488, 488, 488, 494, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 497, 497, 497, 497, 497, 497, 567, 568, 465, 465, 465, 465, 523, 524, 524, 524, 524, 524, 524, 524, 524, 524, 524, 530, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 107, 107, 107, 107, 107, 107, 107, 107, 465, 465, 465, 465, 559, 560, 560, 560, 560, 596, 596, 560, 560, 560, 560, 566, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 107, 616, 107, 616, 107, 616, 107, 616, 465, 465, 465, 465, 559, 596, 596, 596, 596, 596, 596, 596, 596, 596, 596, 566, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 616, 107, 616, 107, 616, 107, 616, 107, 465, 465, 465, 465, 559, 596, 596, 596, 590, 591, 560, 560, 596, 596, 596, 566, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 107, 107, 107, 107, 107, 107, 107, 107, 465, 465, 465, 465, 631, 632, 632, 632, 626, 627, 632, 632, 632, 632, 632, 638, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 461, 461, 461, 461, 461, 461, 531, 532, 461, 461, 461, 461, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 497, 497, 497, 497, 497, 497, 567, 568, 497, 497, 497, 497, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 107, 107, 107, 107, 641, 641, 641, 641, 641, 641, 641, 644, 465, 465, 465, 465, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 465, 465, 465, 465, 107, 616, 107, 616, 107, 616, 107, 616, 107, 107, 107, 107, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 465, 465, 465, 465, 616, 107, 616, 107, 616, 107, 616, 107, 107, 107, 107, 107, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 465, 465, 465, 465, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 107, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 107, 107, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 459, 460,],
                    [495, 496, 107, 107, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 465, 107, 107, 495, 496,],
                    [459, 460, 459, 460, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460, 459, 460,],
                    [495, 496, 495, 496, 107, 107, 107, 107, 641, 642, 642, 642, 642, 642, 642, 644, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496, 495, 496]]

        tile107 = pygame.image.load('img/tiles/pallet_town/107.png')
        tile495 = pygame.image.load('img/tiles/pallet_town/495.png')
        tile496 = pygame.image.load('img/tiles/pallet_town/496.png')
        tile460 = pygame.image.load('img/tiles/pallet_town/460.png')
        tile459 = pygame.image.load('img/tiles/pallet_town/459.png')
        tile465 = pygame.image.load('img/tiles/pallet_town/465.png')
        tile105 = pygame.image.load('img/tiles/pallet_town/105.png')
        tile616 = pygame.image.load('img/tiles/pallet_town/616.png')
        tile497 = pygame.image.load('img/tiles/pallet_town/497.png')
        tile461 = pygame.image.load('img/tiles/pallet_town/461.png')
        tile531 = pygame.image.load('img/tiles/pallet_town/531.png')
        tile532 = pygame.image.load('img/tiles/pallet_town/532.png')
        tile567 = pygame.image.load('img/tiles/pallet_town/567.png')
        tile568 = pygame.image.load('img/tiles/pallet_town/568.png')
        tile641 = pygame.image.load('img/tiles/pallet_town/641.png')
        tile644 = pygame.image.load('img/tiles/pallet_town/644.png')
        tile642 = pygame.image.load('img/tiles/pallet_town/642.png')
        tile444 = pygame.image.load('img/tiles/pallet_town/444.png')
        tile445 = pygame.image.load('img/tiles/pallet_town/445.png')
        tile480 = pygame.image.load('img/tiles/pallet_town/480.png')
        tile481 = pygame.image.load('img/tiles/pallet_town/481.png')
        tile446 = pygame.image.load('img/tiles/pallet_town/446.png')
        tile482 = pygame.image.load('img/tiles/pallet_town/482.png')
        tile416 = pygame.image.load('img/tiles/pallet_town/416.png')
        tile417 = pygame.image.load('img/tiles/pallet_town/417.png')
        tile418 = pygame.image.load('img/tiles/pallet_town/418.png')
        tile419 = pygame.image.load('img/tiles/pallet_town/419.png')
        tile449 = pygame.image.load('img/tiles/pallet_town/449.png')
        tile450 = pygame.image.load('img/tiles/pallet_town/450.png')
        tile485 = pygame.image.load('img/tiles/pallet_town/485.png')
        tile486 = pygame.image.load('img/tiles/pallet_town/486.png')
        tile521 = pygame.image.load('img/tiles/pallet_town/521.png')
        tile522 = pygame.image.load('img/tiles/pallet_town/522.png')
        tile552 = pygame.image.load('img/tiles/pallet_town/552.png')
        tile553 = pygame.image.load('img/tiles/pallet_town/553.png')
        tile558 = pygame.image.load('img/tiles/pallet_town/558.png')
        tile588 = pygame.image.load('img/tiles/pallet_town/588.png')
        tile589 = pygame.image.load('img/tiles/pallet_town/589.png')
        tile590 = pygame.image.load('img/tiles/pallet_town/590.png')
        tile591 = pygame.image.load('img/tiles/pallet_town/591.png')
        tile594 = pygame.image.load('img/tiles/pallet_town/594.png')
        tile624 = pygame.image.load('img/tiles/pallet_town/624.png')
        tile625 = pygame.image.load('img/tiles/pallet_town/625.png')
        tile626 = pygame.image.load('img/tiles/pallet_town/626.png')
        tile627 = pygame.image.load('img/tiles/pallet_town/627.png')
        tile630 = pygame.image.load('img/tiles/pallet_town/630.png')
        tile451 = pygame.image.load('img/tiles/pallet_town/451.png')
        tile452 = pygame.image.load('img/tiles/pallet_town/452.png')
        tile458 = pygame.image.load('img/tiles/pallet_town/458.png')
        tile487 = pygame.image.load('img/tiles/pallet_town/487.png')
        tile488 = pygame.image.load('img/tiles/pallet_town/488.png')
        tile494 = pygame.image.load('img/tiles/pallet_town/494.png')
        tile523 = pygame.image.load('img/tiles/pallet_town/523.png')
        tile524 = pygame.image.load('img/tiles/pallet_town/524.png')
        tile530 = pygame.image.load('img/tiles/pallet_town/530.png')
        tile559 = pygame.image.load('img/tiles/pallet_town/559.png')
        tile560 = pygame.image.load('img/tiles/pallet_town/560.png')
        tile566 = pygame.image.load('img/tiles/pallet_town/566.png')
        tile631 = pygame.image.load('img/tiles/pallet_town/631.png')
        tile632 = pygame.image.load('img/tiles/pallet_town/632.png')
        tile638 = pygame.image.load('img/tiles/pallet_town/638.png')
        tile596 = pygame.image.load('img/tiles/pallet_town/596.png')
        tile_size = 8

        #Iniating map position and movement variables
        mapX = -80
        mapY = -16
        mapX_add = 0
        mapY_add = 0

        is_moving_left = False
        is_moving_right = False
        is_moving_down = False
        is_moving_up = False

        Xpos = 0
        Ypos = 0

        direction = "up"

        #Initiating Menu variables
        menu_open = False
        menu_state = ''
        selection = 1
        
        #Initating character sprite
        char_up = pygame.image.load('C:/Users/DocumentEcstasy/Desktop/L-EFLI AP1-PROG17/Main/Course structure documents/PAP Project/test3/img/character/2.png')
        char_down = pygame.image.load('C:/Users/DocumentEcstasy/Desktop/L-EFLI AP1-PROG17/Main/Course structure documents/PAP Project/test3/img/character/1.png')
        char_left = pygame.image.load('C:/Users/DocumentEcstasy/Desktop/L-EFLI AP1-PROG17/Main/Course structure documents/PAP Project/test3/img/character/3.png')
        char_right = pygame.image.load('C:/Users/DocumentEcstasy/Desktop/L-EFLI AP1-PROG17/Main/Course structure documents/PAP Project/test3/img/character/4.png')

        #Logic loop main game
        while self.state == 'main_game':
            #Handling exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()                
                #Handling input: On keypress, open and close menu according to variable
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if menu_open == False:
                            menu_open = True
                            menu_state = 'menu'
                        elif menu_open == True and menu_state == 'menu':
                            menu_open = False
                            menu_state = 'game'
                    #Handling input: On keypress, accept set selections according to variable
                    if event.key == pygame.K_c:
                        if menu_open == True and selection == 6:
                            menu_state = 'save'
                            selection = 1
                    #Handling input: On keypress, return from set selections according to variable
                    if event.key == pygame.K_x:
                        if menu_open == True and menu_state == 'save':
                            menu_state = 'menu'
                            selection = 6
                    if event.key == pygame.K_c:
                        if menu_open == True and menu_state == 'save' and selection == 2:
                            menu_state = 'menu'
                            selection = 6
                    if event.key == pygame.K_v: #Save the game
                        if menu_open == True and menu_state == 'save' and selection == 1:
                            with open('save_file.txt', 'w') as save_file:
                                json.dump((Xpos, Ypos), save_file)
                            menu_state = 'menu'
                            selection = 6
                    #Handling input: On keypress, cycle selection variable according to menu variable
                    if event.key == pygame.K_UP:
                        if menu_open == True and (menu_state == 'menu' or menu_state == 'save'):
                            selection -= 1
                    if event.key == pygame.K_DOWN and (menu_state == 'menu' or menu_state == 'save'):
                        if menu_open == True:
                            selection += 1
            
            #Resetting menu variables if they reach a certain amount
            if menu_state == 'menu':
                if selection > 8:
                    selection = 1
                if selection < 1:
                    selection = 8
            if menu_state == 'save':
                if selection > 2:
                    selection = 2
                if selection < 1:
                    selection = 1

            #Handling input: If menu is closed, set movement values accordingly on keypresses
            key = pygame.key.get_pressed()
            if menu_open == False:
                if key[pygame.K_LEFT] and mapX_add == 0 and mapY_add == 0 and is_moving_left == False:
                    mapX_add = 16
                    is_moving_left = True
                    direction = "left"
                if key[pygame.K_RIGHT] and mapX_add == 0 and mapY_add == 0 and is_moving_right == False:
                    mapX_add = -16
                    is_moving_right = True
                    direction = "right"
                if key[pygame.K_UP] and mapY_add == 0 and mapY_add == 0 and is_moving_up == False:
                    mapY_add = 16
                    is_moving_up = True
                    direction = "up"
                    Ypos += 1
                if key[pygame.K_DOWN] and mapY_add == 0 and mapY_add == 0 and is_moving_down == False:
                    mapY_add = -16
                    is_moving_down = True
                    direction = "down"
                    Ypos -= 1

            #Resetting movements values if movement reaches 0
            if mapX_add == 0:
                is_moving_left = False
                is_moving_right = False
            if mapY_add == 0:
                is_moving_down = False
                is_moving_up = False

            #Move map position and universal position in accordance with the movement values        
            if mapX_add > 0 and is_moving_left == True:
                mapX += 1
                mapX_add -= 1
            if mapX_add < 0 and is_moving_right == True:
                mapX -= 1
                mapX_add += 1
            if mapY_add > 0 and is_moving_up == True:
                mapY += 1
                mapY_add -= 1
            if mapY_add < 0 and is_moving_down == True:
                mapY -= 1
                mapY_add += 1
            Xpos = mapX / 16
            Ypos = mapY / 16

            #Rendering display surface scaling
            display_upscaled = pygame.transform.scale(display, screen_size)
            screen.blit(display_upscaled, (0,0))

            #Rendering map surface (40x36 tiles, from 8px to 32px)
            display.fill((56,56,56))
            display.blit(map_surface, (mapX,mapY))

            #Rendering tilemap onto map surface
            y = 0
            for row in game_map:
                x = 0
                for tile in row:
                    if tile == 107:
                        map_surface.blit(tile107, (x * tile_size, y * tile_size))
                    if tile == 495:
                        map_surface.blit(tile495, (x * tile_size, y * tile_size))
                    if tile == 496:
                        map_surface.blit(tile496, (x * tile_size, y * tile_size))
                    if tile == 460:
                        map_surface.blit(tile460, (x * tile_size, y * tile_size))
                    if tile == 459:
                        map_surface.blit(tile459, (x * tile_size, y * tile_size))
                    if tile == 465:
                        map_surface.blit(tile465, (x * tile_size, y * tile_size))
                    if tile == 105:
                        map_surface.blit(tile105, (x * tile_size, y * tile_size))
                    if tile == 616:
                        map_surface.blit(tile616, (x * tile_size, y * tile_size))
                    if tile == 497:
                        map_surface.blit(tile497, (x * tile_size, y * tile_size))
                    if tile == 461:
                        map_surface.blit(tile461, (x * tile_size, y * tile_size))
                    if tile == 531:
                        map_surface.blit(tile531, (x * tile_size, y * tile_size))
                    if tile == 532:
                        map_surface.blit(tile532, (x * tile_size, y * tile_size))
                    if tile == 567:
                        map_surface.blit(tile567, (x * tile_size, y * tile_size))
                    if tile == 568:
                        map_surface.blit(tile568, (x * tile_size, y * tile_size))				
                    if tile == 641:
                        map_surface.blit(tile641, (x * tile_size, y * tile_size))
                    if tile == 644:
                        map_surface.blit(tile644, (x * tile_size, y * tile_size))
                    if tile == 642:
                        map_surface.blit(tile642, (x * tile_size, y * tile_size))
                    if tile == 444:
                        map_surface.blit(tile444, (x * tile_size, y * tile_size))
                    if tile == 445:
                        map_surface.blit(tile445, (x * tile_size, y * tile_size))
                    if tile == 480:
                        map_surface.blit(tile480, (x * tile_size, y * tile_size))
                    if tile == 481:
                        map_surface.blit(tile481, (x * tile_size, y * tile_size))
                    if tile == 446:
                        map_surface.blit(tile446, (x * tile_size, y * tile_size))
                    if tile == 482:
                        map_surface.blit(tile482, (x * tile_size, y * tile_size))
                    if tile == 416:
                        map_surface.blit(tile416, (x * tile_size, y * tile_size))
                    if tile == 417:
                        map_surface.blit(tile417, (x * tile_size, y * tile_size))
                    if tile == 418:
                        map_surface.blit(tile418, (x * tile_size, y * tile_size))
                    if tile == 419:
                        map_surface.blit(tile419, (x * tile_size, y * tile_size))
                    if tile == 449:
                        map_surface.blit(tile449, (x * tile_size, y * tile_size))
                    if tile == 450:
                        map_surface.blit(tile450, (x * tile_size, y * tile_size))
                    if tile == 485:
                        map_surface.blit(tile485, (x * tile_size, y * tile_size))
                    if tile == 486:
                        map_surface.blit(tile486, (x * tile_size, y * tile_size))
                    if tile == 521:
                        map_surface.blit(tile521, (x * tile_size, y * tile_size))
                    if tile == 522:
                        map_surface.blit(tile522, (x * tile_size, y * tile_size))
                    if tile == 552:
                        map_surface.blit(tile552, (x * tile_size, y * tile_size))
                    if tile == 553:
                        map_surface.blit(tile553, (x * tile_size, y * tile_size))
                    if tile == 558:
                        map_surface.blit(tile558, (x * tile_size, y * tile_size))
                    if tile == 588:
                        map_surface.blit(tile588, (x * tile_size, y * tile_size))
                    if tile == 589:
                        map_surface.blit(tile589, (x * tile_size, y * tile_size))
                    if tile == 590:
                        map_surface.blit(tile590, (x * tile_size, y * tile_size))
                    if tile == 591:
                        map_surface.blit(tile591, (x * tile_size, y * tile_size))
                    if tile == 594:
                        map_surface.blit(tile594, (x * tile_size, y * tile_size))
                    if tile == 624:
                        map_surface.blit(tile624, (x * tile_size, y * tile_size))
                    if tile == 625:
                        map_surface.blit(tile625, (x * tile_size, y * tile_size))
                    if tile == 626:
                        map_surface.blit(tile626, (x * tile_size, y * tile_size))
                    if tile == 627:
                        map_surface.blit(tile627, (x * tile_size, y * tile_size))
                    if tile == 630:
                        map_surface.blit(tile630, (x * tile_size, y * tile_size))
                    if tile == 451:
                        map_surface.blit(tile451, (x * tile_size, y * tile_size))
                    if tile == 452:
                        map_surface.blit(tile452, (x * tile_size, y * tile_size))
                    if tile == 458:
                        map_surface.blit(tile458, (x * tile_size, y * tile_size))
                    if tile == 487:
                        map_surface.blit(tile487, (x * tile_size, y * tile_size))
                    if tile == 488:
                        map_surface.blit(tile488, (x * tile_size, y * tile_size))
                    if tile == 494:
                        map_surface.blit(tile494, (x * tile_size, y * tile_size))
                    if tile == 523:
                        map_surface.blit(tile523, (x * tile_size, y * tile_size))
                    if tile == 524:
                        map_surface.blit(tile524, (x * tile_size, y * tile_size))
                    if tile == 530:
                        map_surface.blit(tile530, (x * tile_size, y * tile_size))
                    if tile == 559:
                        map_surface.blit(tile559, (x * tile_size, y * tile_size))
                    if tile == 560:
                        map_surface.blit(tile560, (x * tile_size, y * tile_size))
                    if tile == 566:
                        map_surface.blit(tile566, (x * tile_size, y * tile_size))
                    if tile == 631:
                        map_surface.blit(tile631, (x * tile_size, y * tile_size))
                    if tile == 632:
                        map_surface.blit(tile632, (x * tile_size, y * tile_size))
                    if tile == 638:
                        map_surface.blit(tile638, (x * tile_size, y * tile_size))
                    if tile == 596:
                        map_surface.blit(tile596, (x * tile_size, y * tile_size))
                    x += 1
                y += 1
            
            #Rendering character sprite
            if direction == 'up':
                display.blit(char_up, (64,60))
            if direction == 'down':
                display.blit(char_down, (64,60))
            if direction == 'left':
                display.blit(char_left, (64,60))
            if direction == 'right':
                display.blit(char_right, (64,60))

            #Rendering in-game menu
            if menu_open == True:
                menu(display, selection, menu_state)

            #Debugging
            print(f"{Xpos, Ypos}, {mapX, mapY}, {direction}, {mapX_add, mapY_add}, {menu_open}, {selection}, {menu_state}")

            #Update display and set framerate
            pygame.display.update()
            clock.tick(60)

#Running the game class    
game_state = Game()  
game_state.state_manager()