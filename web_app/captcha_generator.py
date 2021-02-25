import os
import random
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw
from django.conf import settings
from .constants import COLORS, CENTERS
# from .noise_module import apply_random_noise


def chose_four_random_images():
    images_df = pd.read_csv(os.path.join(
        settings.BASE_DIR, 'static/captcha/data/image_data.csv'))
    images_data = np.array(images_df)
    n = 4
    images_ar = images_data[np.random.choice(
        len(images_data), n, replace=False)]

    images = [Image.open(os.path.join(
        settings.BASE_DIR, 'static/captcha/images/' + img[1])) for img in images_ar]

    return [img[2] for img in images_ar], images


def merge_four_images(images):
    image_size = images[0].size
    merged_image = Image.new(
        'RGB', (2 * image_size[0], 2 * image_size[1]), (250, 250, 250))

    coords = [(0, 0), (image_size[0], 0), (0, image_size[1]), image_size]
    for i in range(4):
        merged_image.paste(images[i], coords[i])

    return merged_image


def random_pixel(x_l, x_r, y_l, y_r):
    return (int(random.uniform(x_l, x_r)), int(random.uniform(y_l, y_r)))


def generate_random_polygon(center_p):
    x, y = center_p
    poly = []
    poly.append(random_pixel(x - 10, x + 10, y - 45, y - 70))
    poly.append(random_pixel(x + 45, x + 70, y - 10, y + 10))
    poly.append(random_pixel(x - 10, x + 10, y + 45, y + 70))
    poly.append(random_pixel(x - 45, x - 70, y - 10, y + 10))
    return poly


def draw_random_boundary(image):
    colors = COLORS
    centers = CENTERS
    polygons = []
    for center_i in centers:
        polygons.append(generate_random_polygon(center_i))

    boundary_colors = []
    image1 = ImageDraw.Draw(image)
    for poly in polygons:
        n = len(poly)
        clr = colors[int(random.uniform(0, len(colors) - 1))]
        boundary_colors.append(clr)
        for i in range(n):
            image1.line([poly[i], poly[(i + 1) % n]], fill=clr,
                        width=int(random.uniform(2, 4)))

    return boundary_colors, image


def save_captcha_image(image):
    try:
        image.save(os.path.join(settings.BASE_DIR,
                                'static/captcha/captcha.jpeg'))
    except:
        print("saving failed")


def create_new_captcha():
    categories, images = chose_four_random_images()
    merged_image = merge_four_images(images)
    boundary_colors, boundary_drawn_image = draw_random_boundary(merged_image)
    save_captcha_image(boundary_drawn_image)
    target_category = categories[int(random.uniform(0, len(categories) - 1))]
    target_colors = set()
    for i in range(len(categories)):
        if categories[i] == target_category:
            target_colors.add(boundary_colors[i])
    # apply_random_noise()

    return {'category': target_category.upper(), 'target_colors': [color for color in target_colors]}
