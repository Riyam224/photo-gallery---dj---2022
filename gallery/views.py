from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render

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




def add_photo(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                desc=data['description'],
                image=image,
            )

        return redirect('/')

    context = {'categories': categories}
    return render(request, 'add_photo.html', context)