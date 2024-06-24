from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request):

    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели ПАРУС",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page" : "Текст о том, почему наш магазин такой класный, и какой у нас хороший товар"
    }

    return render(request, "main/about.html", context)
