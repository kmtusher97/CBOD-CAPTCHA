import json
import numpy as np
from django.http import HttpResponse, JsonResponse

from .constants import COLORS
from .captcha_generator import create_new_captcha


def get_all_boundary_colors(request):
    colors = np.array(COLORS)
    np.random.shuffle(colors)
    return JsonResponse(json.dumps({"colors": [color for color in colors]}), safe=False)


def generate_captcha(request):
    captcha_data = create_new_captcha()
    return JsonResponse(json.dumps(captcha_data), safe=False)
