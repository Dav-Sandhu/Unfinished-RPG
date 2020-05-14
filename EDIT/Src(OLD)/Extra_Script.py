#-----------------------------------EXTRA SCRIPT-------------------------------#

"""this script is for any cut out content for possible later use!"""


  """  prof1 = pygame.image.load('..\\images\\prof_pic\\profile1.png')
    prof1_2 = pygame.image.load('..\\images\\prof_pic\\profile1.2.png')
    prof2 = pygame.image.load('..\\images\\prof_pic\\profile2.png')
    prof2_2 = pygame.image.load('..\\images\\prof_pic\\profile2.2.png')
    prof3 = pygame.image.load('..\\images\\prof_pic\\profile3.png')
    prof3_2 = pygame.image.load('..\\images\\prof_pic\\profile3.2.png')
    edit1 = pygame.image.load('..\\images\\prof_pic\\edit_button_1.png')
    edit2 = pygame.image.load('..\\images\\prof_pic\\edit_button_2.png')
    next1 = pygame.image.load('..\\images\\prof_pic\\next_button_1.png')
    next2 = pygame.image.load('..\\images\\prof_pic\\next_button_2.png')
    exitA = pygame.image.load('..\\images\\prof_pic\\exit_button.png')"""




#info_bar(images.info_bar_powers)
#info_bar(images.info_bar_items)
#info_bar(images.info_bar_menu)
#info_bar(images.info_bar_stats)
#stats()
#info_bar(images.info_bar_interact)
#Const.gameDisplay.blit(images.info_bar, [0, 450])
#talk = 0
#profile = images.prof1
#from Main_Script import info_bar
#info_bar(images.info_bar_interact)
#message_to_screen("-"+str(player.player_attack), Const.white, [300, 400], 25)

"""def stats():
    Const.gameDisplay.fill(Const.white)
    Const.gameDisplay.blit(Const.profile, [0, 0])
    Const.gameDisplay.blit(images.edit1, [0, 59])
    message_to_screen("Level" + str(player.Level), Const.black, [0, 475], 25)
    pygame.display.update()
    Const.stat_counter = 1
    while Const.stat_counter == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            if 52 > mouse[0] > 0 and 89 > mouse[1] > 59:
                if event.type==MOUSEBUTTONDOWN:
                    Const.gameDisplay.blit(images.edit2, [0, 59])
                    pygame.display.update()
                    time.sleep(0.1)
                    Const.gameDisplay.blit(images.edit1, [0, 59])
                    pygame.display.update()
                    time.sleep(0.1)
                    edit()
                    Const.stat_counter = 0"""



"""def info_bar(state):
    Const.gameDisplay.blit(state, [0, 450])
    pygame.display.update()
    time.sleep(0.05)
    Const.gameDisplay.blit(images.info_bar, [0, 450])
    pygame.display.update()"""



"""info_bar = pygame.image.load("..\\images\\info_bar\\Info_bar.png")
info_bar_items = pygame.image.load('..\\images\\info_bar\\Info_bar-items.png')
info_bar_menu = pygame.image.load('..\\images\\info_bar\\Info_bar-menu.png')
info_bar_powers = pygame.image.load('..\\images\\info_bar\\Info_bar-powers.png')
info_bar_stats = pygame.image.load('..\\images\\info_bar\\Info_bar-stats.png')
info_bar_interact = pygame.image.load('..\\images\\info_bar\\Info_bar-interact.png')"""

"""
    attack1_1 = pygame.image.load('..\\images\\attacks\\attack.1.png')
    attack1_2 = pygame.image.load('..\\images\\attacks\\attack.2.png')
    attack1_3 = pygame.image.load('..\\images\\attacks\\attack.3.png')
    attack1_4 = pygame.image.load('..\\images\\attacks\\attack.4.png')
    attack1_5 = pygame.image.load('..\\images\\attacks\\attack.5.png')
    attack2_1 = pygame.image.load('..\\images\\attacks\\attack2.1.png')
    attack2_2 = pygame.image.load('..\\images\\attacks\\attack2.2.png')
"""


"""def edit():
    Const.edit_counter = 1
    Const.gameDisplay.fill(Const.white)
    Const.gameDisplay.blit(images.exitA, [0, 0])
    Const.gameDisplay.blit(Const.profile, [250, 250])
    prof_list = [images.prof1, images.prof1_2, images.prof2, images.prof2_2, images.prof3, images.prof3_2]
    Const.gameDisplay.blit(images.next1, [250, 309])
    pygame.display.update()
    while Const.edit_counter == 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            if 302 > mouse[0] > 250 and 339 > mouse[1] > 309:
                if event.type==MOUSEBUTTONDOWN:
                    Const.gameDisplay.blit(images.next2, [250, 309])
                    pygame.display.update()
                    time.sleep(0.1)
                    Const.gameDisplay.blit(images.next1, [250, 309])
                    pygame.display.update()
                    if Const.profNum < 5:
                        Const.profNum += 1
                    else:
                        Const.profNum = 0
                    Const.profile = prof_list[Const.profNum]
                    Const.gameDisplay.blit(Const.profile, [250, 250])
                    pygame.display.update()
            elif 84 > mouse[0] > 0 and 76 > mouse[1] > 0:
                if event.type==MOUSEBUTTONDOWN:
                    Const.edit_counter = 0
                    pygame.display.update()"""






