from django.shortcuts import render
from django.http import HttpResponse
from techshopapp.models import Item

# Create your views here.
def index(request):
    context = {
        'title': 'The coolest Tech Shop in the world',
        'description': 'You can buy here anything you want',
    }
    return render(request, "techshopapp/index.html", context=context)


def items_create(request):
    for i in range(20):
        item = Item.objects.create(name=f"Item_num{i}",
                                        price=12543+i,
                                        description=f"This is the coolest phone in the world num {i}",
                                        image=f"Here will be image number {i}")
        item.save()
    return HttpResponse('Create items')


def catalog(request):
    items = Item.objects.all()
    return render(request, "techshopapp/catalog.html", context={'items': items})
