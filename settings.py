from numba import njit
import numpy as np
import glm, math, random
from scipy.spatial import Delaunay
from perlin_noise import PerlinNoise
import pygame as pg

#resolution
#vec2 provides a scalar value for each component.
WIN_RES = glm.vec2(1600, 900) 

#orbit constances
orbit_radius = 400
central_mass = 500000000
gravitationalConstant = 6.674 * (10 ** -11)
time = 0

#sun constants
sradius = 125
scenter = (200, 0, 0)
velocity = (0, 0, 0)
sunsamples = 100

#planet constants
pradius = 50
pcenter = (-300, 0, 0)
planetsamples = 1000

#distance star constants
dsradius = 1000
independantstarrad = 1
dssamples = 5
numstars = 100

#camera constants
ASPECT_RATIO = WIN_RES.x / WIN_RES.y
FOV_DEG = 50

#degress to rad
V_FOV = FOV_DEG * (math.pi / 180) 
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO)
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = 89 * (math.pi / 180)

#player constants 
PLAYER_SPEED = 0.001
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(-300, 51.5, 0)
MOUSE_SENSITIVITY = 0.002
JOYSTICK_SENSITIVITY = 0.003

#Screen constants
BG_COLOUR = glm.vec3(0.0, 0.0, 0.0)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')

#star constants
STAR_SIZE = 50
STAR_SPACING = 100
STAR_COLOR = (255, 255, 0)  
LIT_STAR_COLOR = (255, 0, 0)  


#perlin noise constants 
noise_scale = 2.0
octaves = 1
persistence = 0.5
lacunarity = 2.0
seed = random.randint(1, 1000)
noise = PerlinNoise(octaves=octaves, seed=seed)
height_factor = 1

#settings profiles
HIGH_GRAPHICSPROFILE = (1000000, 10000, 500)
MEDIUM_GRAPHICSPROFILE = (100000, 3000, 250)
LOW_GRAPHICSPROFILE = (50000, 1500, 150)

HIGH_MGAMESENSE = 0.005
MEDIUM_MGAMESENSE = 0.0025
LOW_MGAMESENSE = 0.0015

HIGH_CGAMESENSE = 0.006
MEDIUM_CGAMESENSE = 0.004
LOW_CGAMESENSE = 0.002

HIGH_TIMEPROFILE = (450000, 2700000)
MEDIUM_TIMEPROFILE =  (300000, 1800000)
LOW_TIMEPROFILE =  (100, 9)

