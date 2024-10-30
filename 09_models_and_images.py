import math
import os
import sys
import numpy as np
import moderngl
import pygame
import glm
from objloader import Obj
from PIL import Image

# Set DPI awareness for high-resolution displays
os.environ['SDL_WINDOWS_DPI_AWARENESS'] = 'permonitorv2'

# Initialize pygame and OpenGL context for compatibility on M1 Macs
pygame.init()
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
pygame.display.set_mode((800, 800), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)

class ImageTexture:
    def __init__(self, path):
        self.ctx = moderngl.get_context()
        img = Image.open(path).convert('RGBA')
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        self.texture = self.ctx.texture(img.size, 4, img.tobytes())
        self.texture.use()

    def use(self):
        self.texture.use()

class ModelGeometry:
    def __init__(self, path):
        self.ctx = moderngl.get_context()
        obj = Obj.open(path)
        self.vbo = self.ctx.buffer(obj.pack('vx vy vz nx ny nz tx ty'))
    
    def vertex_array(self, program):
        return self.ctx.vertex_array(program, [(self.vbo, '3f 3f 2f', 'in_vertex', 'in_normal', 'in_uv')])

class Mesh:
    def __init__(self, program, geometry, texture=None):
        self.vao = geometry.vertex_array(program)
        self.program = program
        self.texture = texture

    def render(self, position, color, scale):
        self.program['use_texture'].value = bool(self.texture)
        self.program['position'].value = position
        self.program['color'].value = color
        self.program['scale'].value = scale

        if self.texture:
            self.texture.use()
        
        self.vao.render()

class Scene:
    def __init__(self):
        self.ctx = moderngl.get_context()
        self.program = self.ctx.program(
            vertex_shader='''
                #version 330 core
                uniform mat4 camera;
                uniform vec3 position;
                uniform float scale;
                layout (location = 0) in vec3 in_vertex;
                layout (location = 1) in vec3 in_normal;
                layout (location = 2) in vec2 in_uv;
                out vec3 v_vertex;
                out vec3 v_normal;
                out vec2 v_uv;
                void main() {
                    v_vertex = position + in_vertex * scale;
                    v_normal = in_normal;
                    v_uv = in_uv;
                    gl_Position = camera * vec4(v_vertex, 1.0);
                }
            ''',
            fragment_shader='''
                #version 330 core
                uniform sampler2D Texture;
                uniform bool use_texture;
                uniform vec3 color;
                in vec3 v_vertex;
                in vec3 v_normal;
                in vec2 v_uv;
                out vec4 out_color;
                void main() {
                    out_color = vec4(color, 1.0);
                    if (use_texture) {
                        out_color *= texture(Texture, v_uv);
                    }
                }
            ''',
        )

        # Load textures and models
        self.texture = ImageTexture('/Users/casr/casrprojects/cg-booting-up-casrhub/tec.png')
        self.car_geometry = ModelGeometry('/Users/casr/casrprojects/cg-booting-up-casrhub/lowpoly_toy_car.obj')
        self.car = Mesh(self.program, self.car_geometry)

        self.crate_geometry = ModelGeometry('/Users/casr/casrprojects/cg-booting-up-casrhub/crate.obj')
        self.crate = Mesh(self.program, self.crate_geometry, self.texture)

    def camera_matrix(self):
        now = pygame.time.get_ticks() / 1000.0
        eye = (math.cos(now), math.sin(now), 0.5)
        proj = glm.perspective(math.radians(45.0), 1.0, 0.1, 1000.0)
        look = glm.lookAt(eye, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0))
        return proj * look

    def render(self):
        camera = self.camera_matrix()

        self.ctx.clear()
        self.ctx.enable(self.ctx.DEPTH_TEST)

        self.program['camera'].write(camera)

        self.car.render((-0.4, 0.0, 0.0), (1.0, 0.0, 0.0), 0.2)
        self.crate.render((0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 0.2)
        self.car.render((0.4, 0.0, 0.0), (0.0, 0.0, 1.0), 0.2)
scene = Scene()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    scene.render()
    pygame.display.flip()
