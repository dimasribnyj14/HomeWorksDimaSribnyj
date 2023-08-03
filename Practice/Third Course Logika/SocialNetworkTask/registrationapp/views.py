from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
# Create your views here.
def show_reg_form(request):
    context={}
    # якщо тип запиту є POST (тобто користувач надіслав форму)
    if request.method == "POST":
        # записуємо данні з форми в змінні
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        # записуємо данні зі змінних в контекст щоб потім у разі помилки видати користовачу не 
        # пусту форму, а форму з раніше заповненими данними
        context = {
            'password':password,
            'password_confirm':password_confirm,
            'username':username,
        }
        # якщо повторення паролю співпадає з паролем
        if password == password_confirm:
            # Пробуємо зберегти користувача у БД
            try:
                # створюємо користувача в БД
                User.objects.create_user(username = username, password = password)
                # перенаправляє на сторінку "Реєстрація успішна"
                return redirect("reg_success")
            # якщо користувач вже існує у БДA            
            except IntegrityError:
                # передає в контекст текст помилки
                context['error_text']= 'Такий користувач вже існує!'
        else:
            # передає в контекст текст помилки
            context['error_text']= 'Паролі не співпадають!'

    return render(request,'registrationapp/reg_form.html', context)
    
def show_reg_success(request):
    return render(request,'registrationapp/reg_success.html')
# Створюєм функцію для показу та обробки форми логіну
def show_login_form(request):
    # Пустий контекс-словник
    context = {}
    # Якщо метод запиту "POST" (тобто користувач надіслав форму)
    if request.method == "POST":
        # Отримання username та password з форми
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Знаходження користувача за ім'ям та паролем  у БД
        user = authenticate(request, username = username, password = password)
        # Якщо в змінна user непорожня, тобто дані користувачем введені правильно
        if user != None:
            # Здійснюємо вхід
            login(request,user)
            # Переадресація на сторінку після входу
            return redirect('welcome')
        else:
            # Якщо помилка в якомусь з полів, то показуємо помилку на сторінці входу
            context['error_text'] = 'Ім`я або пароль не співпадають'
    # Повертаємо сторінку за шаблоном
    return render(request,'registrationapp/login_form.html',context)
    
            
# Функція успішності входу
def welcome(request):
    # Якщо користувач авторизирован
    if request.user.is_authenticated:
        # Рендерить сторінку успішності входу
        return render(request,"registrationapp/welcome.html")
    else:
        # Переходить до форми логіну        
        return redirect('login_form')

# Функція вихід з аккаунту
def user_logout(request):
    # Виходить з аккаунту (видаляє sessionid з кукі файлів)
    logout(request)
    # Переходить до форми логіну      
    return redirect('log_reg')

# Функція вибору логіну та реєстрації
def log_or_reg(request):
    # Якщо користувач авторизирован
    if request.user.is_authenticated:
        # Переходить до успішності входу
        return redirect('welcome')
    else:
        # Якщо користувач НЕ авторизован, то переходить до вибору.
        return render(request,'registrationapp/choice_form.html')