from django.shortcuts import render
from .models import ImportedProduct

def imported_product_list(request):
    products = ImportedProduct.objects.all()
    return render(request, 'imported_product_list.html', {'products': products})
