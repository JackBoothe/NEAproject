import numpy as np

class BaseMesh:
    def __init__(self):

        #openGl context
        self.ctx = None 

        #shader program
        self.program = None 
         #vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        self.attrs: tuple[str, ...] = None
        self.vao = None
        
        #retreiving the vertex information, mesh information and colour information for each vertex 
        self.raw_vdata, self.raw_mesh, self.colours = self.get_vertex_data() 
        self.raw_mesh = [item for sublist in self.raw_mesh.tolist() for item in sublist]

    #retreiving vertex data
    def get_vertex_data(self) -> np.array: ...

    def format_vdata(self) -> np.array: ...

    #retreiving Vertex Array Object
    def get_vao(self): 

        vertex_data = self.format_vdata()
        vbo = self.ctx.buffer(vertex_data)

        #specific state of vbo for rendering and including the vbo format and it's list of attributes
        vao = self.ctx.vertex_array(self.program, [(vbo, self.vbo_format, *self.attrs)]) 
        return vao

    def render(self):
        self.vao.render()



