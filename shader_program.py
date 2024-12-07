from settings import *

class ShaderProgram:
    def __init__(self, app):

        #initialising attributes
        self.app = app
        self.ctx = app.ctx

        self.player = app.player
        self.sphere = self.get_program(shader_name="sphere")
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        #matrix projection and matrix models
        self.sphere["m_proj"].write(self.player.m_proj)
        self.sphere["m_model"].write(glm.mat4())

    def update (self):
        #updating the viewing frustum using new matrix view considering new player position 
        self.sphere["m_view"].write(self.player.m_view)

    def get_program(self, shader_name):
        #retreiving shader code 
        with open(f"shaders/{shader_name}.vert") as f:
            vertex_shader = f.read()

        with open(f"shaders/{shader_name}.frag") as f:
            fragment_shader = f.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader= fragment_shader)
        
        #returning an instance of the shader program
        return program 
