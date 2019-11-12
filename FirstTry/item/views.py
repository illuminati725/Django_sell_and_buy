from django.shortcuts import render
from . import models

# Create your views here.

def category_page(request,category):
    cat=[]
    items=models.item.objects.all()
    # items=item.objects.all()
    for item in items:
        if item.category==category:
            cat.append(item)
    context_dict={
        'items':cat
    }
    return render(request,'item/category_page.html',context=context_dict)
