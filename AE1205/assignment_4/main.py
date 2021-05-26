import numpy as np #same
import custom_math as cst_math # this might not be needed
import pygame
import time
import color
import cow

def main():
    """set up the main game loop"""
    pygame.init()

    reso = (800, 400)
    scale = 5. # pixels per meter
    main_surface = pygame.display.set_mode(reso)


    font_1 = pygame.font.SysFont("Courier", 16)


    frame_count = 0
    fps = 0
    t0 = t00 = t0_fps = time.time()
    fps_text = dt_text = font_1.render("", True, color.black)
    calc_per_frame = 10

    #cow sprite
    cow_1 = cow.cow_sprite(pygame.image.load("cow.png"), np.array([30.,60.]),10.,00.,60.,0.5,10500.)

    #background image
    background_img = pygame.image.load("background.jpg")
    background_img = pygame.transform.scale(background_img, reso)
    background_img = pygame.transform.flip(background_img, True, False)
    background_rect = background_img.get_rect()


    #key_actions = {
    #	pygame.K_ESCAPE: 
    #}

    game_state = 0

    running = True
    while running:
        t1 = time.time()
        dt = t1-t0	
        t_since_start = t1-t00


        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    game_state = 1
                    cow_1.state = 1         
                    




        frame_count += 1
        if frame_count % (500 / calc_per_frame) == 0:
            fps= 500 / ((t1-t0_fps) * calc_per_frame)
            t0_fps = t1
            fps_text = font_1.render(str(fps), True, color.black)
            dt_text = font_1.render(str(dt), True, color.black)

        main_surface.blit(background_img, background_rect)

        main_surface.blit(fps_text, (10,10))
        main_surface.blit(dt_text, (10,30))


        if cow_1.state == 2 and scale >= 2:
            scale -= dt
        if game_state == 1:

            for i in range(calc_per_frame):
                cow_info = cow_1.update(dt/calc_per_frame)

            cow_text = font_1.render('phi: {}, pos: {}'.format(cow_info[0], cow_info[1]), True, color.black)
            main_surface.blit(cow_text, (10,60))

        
        cow_1.draw(main_surface, reso, scale, frame_count)

        

        pygame.display.flip()


        t0 = t1
    pygame.quit()


main()
	
