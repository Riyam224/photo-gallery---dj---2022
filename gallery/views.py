from multiprocessing import context
from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Photo , Category


def photo_list(request):
    photos = Photo.objects.all()
    categories = Category.objects.all()
    context = {
        'photos': photos,
        'categories': categories
        
    }
    return render(request , 'photo_list.html', context)


def photo_view(request , id):
    photo = get_object_or_404(Photo , id=id)
    context = {
        'photo': photo
    }
    return render(request , 'photo.html', context)



def photo_by_category(request , category):
    my_category = Category.objects.get(name=category)
    photo_category = Photo.objects.filter(category=my_category)
    context = {
        'photo_category':photo_category
    }

    return render(request , 'photo_by_category.html',context)
