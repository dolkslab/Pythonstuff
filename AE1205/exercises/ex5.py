import numpy as np
import vector
import matplotlib.pyplot as plt
import pygame
import time

#constants 
g = 9.81
gravvec = np.array([0, -g])
k_spring = 26.0
l_spring = 1.0
mass = 1.5
damp_c = 0.4


print(color.black)







def main():
	"""set up the main game loop"""
	pygame.init()

	
	main_surface = pygame.display.set_mode((1280, 720))
	
	font_1 = pygame.font.SysFont("Courier", 16)
	
	some_color = (255, 100, 0)
	color_black = (0,0,0)
	frame_count = 0
	frame_rate = 0
	t0 = t00 = time.time()
	fps_text = dt_text = font_1.render("", True, (0,0,0))
	
	
	scale = 100
	
	#starting conditions
	pos = np.array([0.8,-0.3])
	v=np.array([0.0,0.0])
	
	while True:
		t1 = time.time()
		dt = t1-t0	
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break
			

		frame_count += 1
		if frame_count % 500 == 0:
			frame_rate = 500 / (t1-t00)
			t00 = t1
			fps_text = font_1.render(str(frame_rate), True, color_black)
			dt_text = font_1.render(str(dt), True, color_black)
		
		main_surface.fill((255, 255, 255))
		main_surface.fill(color_black, (640, 360, 10, 10))
		
		main_surface.blit(fps_text, (10,10))
		main_surface.blit(dt_text, (10,30))
		
		
		
		#sim stuff
		F_spring = (l_spring-vector.magnitude(pos))*k_spring*vector.normalize(pos)
		a = F_spring + gravvec - v*damp_c
		v += a*dt
		pos += v*dt
	

		
		main_surface.fill(some_color, (pos[0]*scale + 640, 360 - pos[1]*scale,10, 10))
		
		

		
		pygame.display.flip()
		t0 = t1
	pygame.quit()
	

main()
	
	
