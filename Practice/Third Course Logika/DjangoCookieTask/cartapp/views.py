from django.shortcuts import render
from django.http import JsonResponse
from cartapp.models import *
# Create your views here.
def show_products(request):
    response = render(request,"products.html",context={"products": Product.objects.all()}) #Создаем ответ рендером, чтобы при создание куки не перешло на другую страницу
    if request.method == "POST": # Если метод запроса является POST
        if "product_pk" not in request.COOKIES: # Если продукт_айди нету в куки
            new_product = request.POST.get('product_pk') # берем айди из запроса ПОСТ
            response.set_cookie('product_pk',new_product) # создаем куки
            return response # возращаем ответ
        else: # Если все таки продукт_айди есть в куки
            new_product = request.COOKIES['product_pk'] + " " + request.POST.get('product_pk') # просто берем существующий куки и добавляем еще
            response.set_cookie('product_pk',new_product) # создаем новый куки 
            return response # возращаем ответ
        # Я считаю, что лучше писать ТУТ return response, чем в условиях про присутствие или отсутствие продукт_айди в куки, поскольку мы всеравно будем возращать ответ в любом случае.
    return response # Возращаем ответ

def show_cart(request): 
    if "product_pk" in request.COOKIES: # Если продукт_айди присутствует в куки
        products_pk = request.COOKIES['product_pk'] #Берем существующий куки
        products_pk = products_pk.split(' ') #разделяет продукты_айди на список подстрок по разделителю

        list_products = list() # Создаем список продуктов
        for product_pk in products_pk: # Перечисляем продуктов_айди
            list_products.append(Product.objects.get(pk=product_pk)) # добавляем продуктов_айди в список
        response = render(request,"cart.html",context={"products": list_products}) # добавляем список и все остальное в рендер,а рендер в ответ
    else: # Если продукт_айди отсутствует в куки
        response = render(request,"cart.html",context={"products":list()}) # создаем список и все остальное в рендер,а рендер в ответ
    if request.method == "POST": # если метод запроса является POST
        response.delete_cookie('product_pk') # Я могу конечно удалить весь куки, но как удалить тот, который я выбрал не знаю (просто все таки стоит использовать, то что написано на презентации)
        
    return response # возращаем ответ
