import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import numpy as np 
import cv2

im_width = 640
im_height = 480

def process_img(image, image_count):
    i = np.array(image.raw_data)
    i2 = i.reshape((im_height, im_width, 4))
    i3 = i2[:, :, :3]

    # Save image to disk
    cv2.imwrite(f"image_{image_count}.png", i3)

try:
    client = carla.Client('localhost', 2000)
    client.set_timeout(10.0)

    world = client.get_world()

    blueprint_library = world.get_blueprint_library()

    bp = blueprint_library.filter('model3')[0]
    print(bp)

    spawn_point = random.choice(world.get_map().get_spawn_points())

    vehicle = world.spawn_actor(bp, spawn_point)
    vehicle.apply_control(carla.VehicleControl(throttle=1.0, steer=0.0))

    cam_bp = blueprint_library.find('sensor.camera.rgb')
    cam_bp.set_attribute('image_size_x', f'{im_width}')
    cam_bp.set_attribute('image_size_y', f'{im_height}')
    cam_bp.set_attribute('fov', '110')

    spawn_point = carla.Transform(carla.Location(x=2.5, z=0.7))

    try:
        image_count = 0
        sensor = world.spawn_actor(cam_bp, spawn_point, attach_to=vehicle)
        sensor.listen(lambda data: process_img(data, image_count))
        image_count += 1

        # Wait indefinitely
        input("Press Enter to exit...")

    finally:
        print('destroying actors')
        if sensor is not None:
            sensor.destroy()
        print('done.')

finally:
    print('destroying actors')
    if vehicle is not None:
        vehicle.destroy()
    print('done.')
