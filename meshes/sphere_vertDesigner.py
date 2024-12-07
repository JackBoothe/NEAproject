import scipy.spatial

from settings import *
from scipy.spatial import Delaunay


def fibonacci_sphere(radius, center, num_points):
    points = []

     #golden ratio
    phi = (1 + math.sqrt(5)) / 2 

    latitude_angle = math.pi * (1 - 1 / phi)
    longitude_angle = 2 * math.pi / phi

    for i in range(num_points):

        #range from -radius to radius
        y = radius * (1 - (i / float(num_points - 1)) * 2)  
        latitude = math.asin(y / radius)
        longitude = i * longitude_angle

        x = radius * math.cos(latitude) * math.cos(longitude)
        z = radius * math.cos(latitude) * math.sin(longitude)

        #translate the point to the desired center
        x += center[0]
        y += center[1]
        z += center[2]

        points.append((x, y, z))


    mesh = generate_triangles(points)
    return mesh, points

def generate_triangles(vertices):

    #perform convex hull algorithm to link up all the verticies 
    tri = scipy.spatial.ConvexHull(vertices)
    triangles = tri.simplices

    return triangles
