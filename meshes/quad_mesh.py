from settings import *
from meshes.base_mesh import BaseMesh

class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__() #inheriting parent class constructor

        self.app = app
        self.ctx = app.ctx
        self.program = app.shader_program.quad

        self.vbo_format ="3f 3f" #three floats for position (e.g., x, y, z) and three floats for color (e.g., red, green, blue).
        self.attrs = ("in_position", "in_color")
        self.vao = self.get_vao()

    def get_vertex_data(self):
        vertices = [
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0), (0.5, -0.5, 0),
            (0.5, 0.5, -0.5), (-0.5, 0.5, -0.5), (-0.5, 0.5, 0),
            (0.5, 0.5, -0.5), (-0.5, 0.5, 0), (0.5, 0.5, 0)
            ]
        colors = [
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1, 0), (1, 1, 0), (1, 1, 1),
            (0, 1, 0), (1, 1, 0), (1, 1, 1),
            (0, 1, 0), (1, 0, 0), (1, 1, 0)

        ] #normalised colour values

        vertex_data = np.hstack([vertices, colors], dtype="float32")

        return vertex_data
    