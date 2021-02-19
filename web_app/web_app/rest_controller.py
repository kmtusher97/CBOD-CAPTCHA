import json
import numpy as np
from django.http import HttpResponse, JsonResponse

from .constants import COLORS


def get_all_boundary_colors(request):
    colors = np.array(COLORS)
    np.random.shuffle(colors)
    return JsonResponse(json.dumps({'colors': [color for color in colors]}), safe=False)
