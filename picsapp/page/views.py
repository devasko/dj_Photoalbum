from django.shortcuts import render, redirect

from .models import Category, Picture


def gallery(request):
    category = request.GET.get('category')
    if category == None:
        pictures = Picture.objects.all()
    else:
        pictures = Picture.objects.filter(category__title=category)

    categories = Category.objects.all()
    context = {'title': 'Фотогалерея', 'categories': categories, 'pictures': pictures}
    return render(request, 'page/gallery.html', context)


def viewPic(request, pk):
    picture = Picture.objects.get(id=pk)
    context = {'title': 'Просмотр изображения', 'picture': picture}
    return render(request, 'page/single.html', context)


def addPic(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(title=data['category_new'])
        else:
            category = None

        picture = Picture.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )

        return redirect('gallery')

    context = {'title': 'Добавить изображение',  'categories': categories}

    return render(request, 'page/add.html', context)
