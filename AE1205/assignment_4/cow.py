import pygame
import numpy as np
import custom_math as cst_math
import color
import math


gravvec = np.array([0, -9.81])


CD = .7
rho = 1.225



"""This is the cow object, containing a constructor, an update method that handles the physics/mechanics and a draw function that draws the cow and
other items on screen."""
class cow_sprite:
    def __init__(self, img,  init_pos, R, phi_start, phi_stop, l_elas, k_elas):
        if type(img) != int:
            self.image = img
            self.rect = self.image.get_rect()

    
        #Starting pos. The passed init_pos is taken as the origin of the catapult, then pos (which is the position of the cow itself) is calculated based on phi_start
        phi_start = math.radians(phi_start)
        self.arm_length = 10.
        self.phi = phi_start # both angles taken in as degrees, but stored as radians
        self.phi_stop = math.radians(phi_stop)
        self.arm_pos = init_pos
        self.elas_pos = init_pos + np.array([0, R])
        
        self.pos = init_pos + np.array([-R*math.cos(phi_start), R*math.sin(phi_start)])
        #Spring values
        self.l_elas = l_elas
        self.k_elas = k_elas

        #velocities and accelerations
        self.mass = 550. # in kg
        self.a = np.array([0.,0.])
        self.v = np.array([0.,0.])

        self.phi_vel = 0.
        self.phi_acc = 0.

        #Frontal area of the spherical cow
        volume = self.mass/1000.
        r_sphericalcow = math.pow((3/(4*math.pi))*volume,1./3.)	
        self.frontal_area = frontal_area = math.pi*(r_sphericalcow**2)

        #The state var determines what phase of the launch the cow is in, 0 is prelaunch, 1 is launch, 2 is free flight.
        self.state = 0
        self.trace = []

    def draw(self, target_surface, res, scale, frame_count):
        screen_pos = cst_math.screencoords(self.pos, res, scale)
        if (frame_count) % 10 == 0:
            self.trace.append(self.pos.tolist())
        if len(self.trace) > 1:
            pygame.draw.aalines(target_surface, color.black, False, cst_math.screencoords(self.trace, res, scale))
        if self.state == 0:	
            pygame.draw.aaline(target_surface, color.orange, screen_pos, cst_math.screencoords(self.elas_pos, res, scale))
            pygame.draw.aaline(target_surface, color.black, screen_pos, cst_math.screencoords(self.arm_pos, res, scale))
        
        scaled_image = pygame.transform.scale(self.image, (int(15*scale), int(10*scale)))
        self.rect = scaled_image.get_rect()
        self.rect.center = screen_pos
        
        
        target_surface.blit(scaled_image, self.rect)


    def update(self, dt):
        arm_tangent = np.array([self.pos[1]-self.arm_pos[1],-(self.pos[0]-self.arm_pos[0])])


        F_tot = np.array([0.,0.])





        if self.state == 1:
            F_elas = (self.l_elas-cst_math.mag(self.pos-self.elas_pos))*self.k_elas*cst_math.normalize(self.pos-self.elas_pos)
            F_tot = F_elas

            self.a = F_tot/self.mass + gravvec
            a_tangent = np.dot(self.a, cst_math.normalize(arm_tangent))
            self.phi_acc = a_tangent/self.arm_length
            self.phi_vel += self.phi_acc*dt
            self.phi += self.phi_vel*dt

            self.v = self.phi_vel*arm_tangent
            #self.pos = self.arm_pos + np.array([-self.arm_length*math.cos(self.phi), self.arm_length*math.sin(self.phi)]) 
            self.pos += self.v*dt
        elif self.state == 2:
            F_drag = -CD*0.5*rho*(self.v**2)*self.frontal_area
	        
            self.a = gravvec + F_drag/self.mass
            self.v += self.a*dt   
            self.pos += self.v*dt


        if self.phi >= self.phi_stop :
            self.state = 2

        if self.state == 2 and self.pos[1] <= 0. :
            self.state = 3

        return (math.degrees(self.phi), self.pos, self.v)

    def reset(self, init_pos):
        self.pos = init_pos

        self.a = np.array([0.,0.])
        self.v = np.array([0.,0.])
        self.phi = 0.
        self.phi_vel = 0
        self.phi_acc = 0


        self.arm_pos = init_pos + np.array([self.arm_length, 0])
        self.elas_pos = init_pos + np.array([self.arm_length, self.arm_length])

        self.state = 1.
        self.trace = []
