
import settings
from settings import *
from meshes.sphere_mesh import Sphere_mesh

class Scene:
    def __init__(self, app):
        self.app = app

        #initialising all the objects 
        self.sphere = Sphere_mesh(self.app, settings.pcenter, settings.pradius, ((0.54, 0.27, 0.07), (0.54, 1, 0.07), (0, 0.5, 0.7)), planetsamples)
        self.sun = Sphere_mesh(self.app, scenter, settings.sradius, ((1, 0.5, 0), (1, 0, 0), (1, 1, 0)), sunsamples)
        self.stars = Sphere_mesh(self.app, settings.pcenter, independantstarrad, ((1, 1, 1), (1, 1, 1), (1, 1, 1)), dssamples)


    def update(self):
        
        #calculating the sun's velocity 
        v_t = math.sqrt(gravitationalConstant* central_mass / orbit_radius) * 2 # Tangential velocity
        omega = v_t / orbit_radius  # Angular velocity
        settings.velocity = (-v_t * math.sin(omega * settings.time),0 , v_t * math.cos(omega * settings.time)) 
        settings.time += 1

        #updating the sun's vertex information given it's new velocity
        self.sun.raw_vdata = Sphere_mesh.update_byvelocity(self.sun.raw_vdata)

        #putting into the VAO form 
        self.sun.vao = self.sun.get_vao()


    def vertexData(self):
        return self.sun.raw_vdata

    def render(self):

        #rendering all the objects
        self.sphere.render()
        self.sun.render()
        self.stars.render()