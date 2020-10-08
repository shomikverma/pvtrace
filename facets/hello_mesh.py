import time
import sys
import functools
import numpy as np
import trimesh
from pvtrace import *
import logging
logging.getLogger('trimesh').setLevel(logging.CRITICAL)

world = Node(
    name="world (air)",
    geometry=Sphere(
        radius=50.0,
        material=Material(refractive_index=1.0),
    )
)

box = Node(
    name="box (glass)",
    geometry = Mesh(
        trimesh = trimesh.load('colortest4.gltf').dump().sum(),
        material = Material(
            refractive_index = 1.5,
            components = [
                Absorber(coefficient = 0.525),
                ]
        ),
    ),
    parent=world
)

light = Node(
    name="Light (555nm)",
    light=Light(direction=functools.partial(cone, np.pi/8)),
    parent=world
)
# light.rotate(np.radians(60), (1.0, 0.0, 0.0))

if(False):
    renderer = MeshcatRenderer(wireframe=True, open_browser=True)
    scene = Scene(world)
    renderer.render(scene)
    start_t = time.time()
    for ray in scene.emit(100):
        steps = photon_tracer.follow(scene, ray)
        path, events = zip(*steps)
        renderer.add_ray_path(path)

    print(f"Took {time.time() - start_t}s to trace 100 rays.")
