from django.shortcuts import redirect, render
from .models import Categories_Tags
import random

# Create your views here.

categories = ['Interior', 'Exterior']
interior_tags = [
    ['Kitchen', 'Dining', 'Bedroom'],
    ['BathRoom', 'Hallway', 'GYM'],
    ['Front Door', 'Media Room', 'Laundry Room'],
    ['Basement', 'Office', 'Closet'],
    ['Archit.Drawing', 'Sunroom', 'Community'],
    ['Garage', 'FamilyRoom', 'Stairs']
]
exterior_tags = [
    ['House', 'TownHouse'],
    ['Mobile / Manufactured', 'Condo / Appartment'],
    ['PentHouse', 'None']
]

photo_list = []
database = Categories_Tags.objects.all()
for i in database:
    photo_list.append(i.image)
a_number = []

def home(request):
    random_number = random.randint(0,20)
    if len(a_number) == 0:
        a_number.append(random_number)
    else:
        a_number.clear()
        a_number.append(random_number)

    return render(request, "home.html", {'categories' : categories, 'database_image' : photo_list[random_number]})


def interior(request):
    for i in database:
        if i.image == photo_list[a_number[0]]:
            print(photo_list[a_number[0]])
            i.category = 'Interior'
            i.save()
    return render(request, 'interior.html', {'interior_tags' : interior_tags, 'database_image' : photo_list[a_number[0]]})


def exterior(request):
    for i in database:
        if i.image == photo_list[a_number[0]]:
            print(photo_list[a_number[0]])
            i.category = 'Exterior'
            i.save()
    return render(request, 'exterior.html', {'exterior_tags' : exterior_tags, 'database_image' : photo_list[a_number[0]]})


def tables(request):
    arr = request.POST.getlist('arr')
    print(arr)
    for i in database:
        if i.image == photo_list[a_number[0]]:
            print(photo_list[a_number[0]])
            if len(arr) == 0:
                i.tag = 'None'
            else:
                i.tag = arr
            i.save()
    return render(request, 'tables.html', {'database' : database})