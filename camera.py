from scene import Scene
from settings import *


class Camera:
    def __init__(self, position, yaw, pitch):

        #initialising camera attributes 
        self.position = glm.vec3(position)
        self.yaw = glm.radians(yaw)
        self.pitch = glm.radians(pitch)

        #defining movement vectors 
        self.up = glm.vec3(0, 1 ,0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        self.m_proj = glm.perspective(V_FOV, ASPECT_RATIO, NEAR, FAR)
        self.m_view = glm.mat4()

    #updates all algorthms which must occur each frame 
    def update(self):
        self.update_vectors()
        self.update_view_matrix()
        self.position = self.update_player_position(self.position, self.faux_gravity())

        #when collision -> resolve 
        collision_detected = self.sphere_sphere_collision()
        if collision_detected:  self.position = self.resolve_collision()
        
    #gravity function 
    def faux_gravity(self):

        #calculating unit vector of the collision normal 
        gravity_direction = glm.normalize(pcenter - self.position)
        gravity_force = 1 / glm.distance(self.position, pcenter)

        #calculating strength and direction of gravity vector 
        gravity_vector = gravity_force * gravity_direction
        return gravity_vector

    def update_player_position(self, player_position, gravity_vector):

        updated_position = player_position + gravity_vector
        return updated_position
    
    def sphere_sphere_collision(self):
       
        #check if camera and planet meshes collide 
        distance_squared = glm.distance2(self.position, pcenter)
        radii_sum_squared = (0.2 + pradius) ** 2

        return distance_squared < radii_sum_squared
    
    def resolve_collision(self):
        #calculating collision normal 
        collision_normal = glm.normalize(self.position - pcenter)
        penetration_depth = 0.2 + pradius - glm.distance(self.position, pcenter)

        #move the player outside the colliding object
        new_player_position = self.position + penetration_depth * collision_normal

        return new_player_position

    def update_view_matrix(self):

        #updating view frustum using new player position 
        self.m_view = glm.lookAt(self.position, self.position + self.forward, self.up)

    def update_vectors(self):

        #calculating movement vectors 
        self.forward.x = glm.cos(self.yaw) * glm.cos(self.pitch)
        self.forward.y = glm.sin(self.pitch)
        self.forward.z = glm.sin(self.yaw * glm.cos(self.pitch))

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    #functions below are used to move the player 
    def rotate_pitch(self, delta_y):
        self.pitch -= delta_y
        self.pitch = glm.clamp(self.pitch, -PITCH_MAX, PITCH_MAX)

    def rotate_yaw(self, delta_x):
        self.yaw += delta_x

    def move_left(self, velocity):
        self.position -= self.right * velocity

    def move_right(self, velocity):
        self.position += self.right * velocity

    def move_up(self, velocity):
        self.position += self.up * velocity

    def move_down(self, velocity):
        self.position -= self.up * velocity

    def move_forwards(self, velocity):
        self.position += self.forward * velocity

    def move_back(self, velocity):
        self.position -= self.forward * velocity

