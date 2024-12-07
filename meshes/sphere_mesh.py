import settings
from settings import *
from meshes.base_mesh import BaseMesh
from meshes.sphere_vertDesigner import fibonacci_sphere
import re

#inheriting the super class "BaseMesh"
class Sphere_mesh(BaseMesh): 
    def __init__(self, app, pcenter, pradius, pcolours, psamples):

        #initialising attributes 
        self.radius = pradius
        self.center = pcenter
        self.colour = pcolours
        self.samples = psamples
        self.Graphics = self.profile_retreiver()
        
        #inheriting the objects and methods from "baseMesh"
        super().__init__()

        self.app = app
        self.program = app.shader_program.sphere
        self.ctx = app.ctx
        
        #three floats for position (e.g., x, y, z) and three floats for color (e.g., red, green, blue).
        self.vbo_format ="3f 3f" 
        self.attrs = ("in_position", "in_color")
        self.vao = self.get_vao()
        

    #retreives the specific graphics profile from "savedSettings.txt"
    def profile_retreiver(self):
        with open ("textures/DAT/savedSettings.txt", "r") as f: 
            filedata = f.read()

        #parsing the file
        graphicsProfile = filedata[11:filedata.find("Mo")].strip()

        if graphicsProfile == "Low":    return settings.LOW_GRAPHICSPROFILE
        elif graphicsProfile == "Medium":    return settings.MEDIUM_GRAPHICSPROFILE
        elif graphicsProfile == "High":    return settings.HIGH_GRAPHICSPROFILE

    def generate_star_coords(self):
        coordinates = []
        for _ in range(self.Graphics[1]):

            #generate random spherical coordinates
            theta = random.uniform(0, 2 * math.pi)
            phi = random.uniform(0, math.pi)
            r = random.uniform(dsradius/2, dsradius)

            #convert spherical coordinates to Cartesian coordinates
            x = self.center[0] + r * math.sin(phi) * math.cos(theta)
            y = self.center[1] + r * math.sin(phi) * math.sin(theta)
            z = self.center[2] + r * math.cos(phi)

            coordinates.append((x, y, z))

        return coordinates
    

    def get_vertex_data(self):  
        
        if self.radius == 1: 
        
            meshes, verticess = [], []
            coords = self.generate_star_coords()
            
            for i in range(self.Graphics[1]):
                mesh, vertices = fibonacci_sphere(self.radius, coords[i], self.samples)
                previousmesh = len(mesh) -1
                
                if i != 0: 
                    mesh += previousmesh * i
            
                meshes.append(mesh), verticess.append(vertices)

            mesh = np.concatenate(meshes)   
            vertices = [item for sublist in verticess for item in sublist]
            
        #as the get_vertex_data class handles both the vertex information for the planet and that of the sun, I needed to differentiate between the two
        #check the coordinates of self.center against the coordinates of the planet to decide which one is being generated.

        elif self.center == pcenter: 
            
            self.samples = self.Graphics[0]
           
            mesh, vertices = self.retreieving_info()
            vertices = self.addingSomeNoise(vertices) 

        else:   
            if self.center ==scenter:
                self.samples = self.Graphics[2]
            
            mesh, vertices = fibonacci_sphere(self.radius, self.center, self.samples)

        #using the colour information to generate a set of colours for each set of 3 verticies 

        colours = [item for sublist in [[self.colour[0], self.colour[1], self.colour[2]] for i in range(len(mesh))] for item in sublist]   
        return vertices, mesh, colours
                
    def retreieving_info(self):
        #opening "savedVertexData" with read permissions
        with open ("textures/DAT/savedVertexData", "r") as f: 

            #saving it's contents to a variable    
            previousSamples = f.read()      

        
        #checking if the number of samples matches the current number of samples by parsing the string
        if int(previousSamples[previousSamples.find(':') + 1:previousSamples.find('[')].strip()) == self.samples: 

            #extracting vertex information from between the first "[" of the file (where vertex information begins) and just before "Mesh"
            extractedvertices = previousSamples[previousSamples.find('['): previousSamples.find("Mesh:")-1].strip() 

            #extracting mesh information from after "Mesh:" until the end of the file. 
            extractedmesh = previousSamples[(previousSamples.find("Mesh:")+4):].strip()

            #parsing mesh information 
            nested_lists = [s.strip(" []") for s in re.findall(r'\[.*?\]', extractedmesh)]
            nested_lists = [list(map(int, sublist.split(", "))) for sublist in nested_lists]
            mesh = np.array(nested_lists)

            #extract and parse vertices information
            tuple_strings = extractedvertices[1:-1].split("),")
            vertices = []
            for tpl in tuple_strings:
                tpl_parts = tpl.strip().lstrip("(").rstrip(")").split(", ")
                tpl_floats = tuple(float(part) if "." in part or "e" in part else int(part) for part in tpl_parts)
                    
                vertices.append(tpl_floats)
                
        else: #when the number of samples recorded in the text file does not match the current number of samples.

            #generating mesh and vertex information 
           
            mesh, vertices = fibonacci_sphere(self.radius, self.center, self.samples)

            #then writing this information to the "savedVertexData" text file with read+ permissions
            with open("textures/DAT/savedVertexData", "w+") as f: 
                f.write(f"Number of samples:\t{self.samples} \n {str(vertices)}")
                f.write(f"\n\nMesh: \n {mesh.tolist()}")

        return mesh, vertices
    
    
    def addingSomeNoise(self, verts):
        noise_values = []
        for i in range(len(verts)):
            x, y, z = verts[i]

            #retreiving relevant noise constants from module 
            noise_values.append(noise([x * noise_scale, y * noise_scale, z * noise_scale]))

        #applying each noise constant to the x, y, z compnents of each vertex of the planet. Also being able to dampen the height scale using the constant "height_factor"
        noise_vertices = [(x + height_factor * noise_values[i], y + height_factor * noise_values[i], z + height_factor * noise_values[i]) for i, (x, y, z) in enumerate(verts)]
       
        return noise_vertices


    def format_vdata(self):
        triangle_vertices = []

        #changing the type of the rawmesh information  
        for i in self.raw_mesh:
            triangle_vertices.append(self.raw_vdata[i])

        #stacking the triangle primitives with their associated RGB values 
        vertex_data = np.hstack([triangle_vertices, self.colours], dtype="float32")
        
        return vertex_data

    def update_byvelocity(raw_v):

        #changes the position of the sun verticies by applying a velocity to each vertex 
        for j, y in enumerate(raw_v): raw_v[j] = (y[0] +(settings.velocity[0]), y[1] +(settings.velocity[1]), y[2] +(settings.velocity[2]))
        return raw_v










