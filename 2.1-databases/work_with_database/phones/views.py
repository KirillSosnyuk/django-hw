from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_catalog = Phone.objects.all()
    sorting = request.GET.get('sort', False)
    if sorting:
        phones_catalog = phones_catalog.order_by(sorting.replace('min_', '').replace('max_', '-'))
    context = {'phones': phones_catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
