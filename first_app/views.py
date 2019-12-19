from django.http import HttpResponse
import string
import random


def generate_password(request):
    return HttpResponse(''.join(
        random.choice(string.ascii_lowercase)
        for _ in range(10)
    ), status=201)
