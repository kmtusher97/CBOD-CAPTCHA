# import os
# import cv2
# import numpy as np
# from django.conf import settings


# def read_captcha_image():
#     image = cv2.imread(os.path.join(settings.BASE_DIR,
#                                     'static/captcha/captcha.jpeg'))
#     return image


# def apply_random_noise():
#     image = read_captcha_image()

#     mean = 0
#     var = 10
#     sigma = var ** 0.5
#     # np.zeros((224, 224), np.float32)
#     gaussian = np.random.normal(mean, sigma, (200, 200))

#     noisy_image = np.zeros(img.shape, np.float32)

#     if len(img.shape) == 2:
#         noisy_image = img + gaussian
#     else:
#         noisy_image[:, :, 0] = img[:, :, 0] + gaussian
#         noisy_image[:, :, 1] = img[:, :, 1] + gaussian
#         noisy_image[:, :, 2] = img[:, :, 2] + gaussian

#     cv2.normalize(noisy_image, noisy_image, 0, 255, cv2.NORM_MINMAX, dtype=-1)
#     noisy_image = noisy_image.astype(np.uint8)

#     cv2.imwrite(os.path.join(settings.BASE_DIR,
#                              'static/captcha/captcha.jpeg'), noisy_image)
