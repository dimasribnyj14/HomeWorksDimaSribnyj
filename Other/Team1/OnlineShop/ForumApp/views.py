from django.shortcuts import render
from ForumApp.models import Post
# Create your views here.


# Функция показа форум (постов)
def show_forum(request):
    # Если тип запроса POST (Если пользователь отправил запрос)
    if request.method == 'POST':
        # Заголовок, контент, Изображение (берем из запроса и записываем в переменную)
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        # Автор данного поста (берем из запроса имя пользователя и записываем в переменную)
        author = request.user.username
        # Создаем и добавляем пост в базу данных
        Post.objects.create(title = title, content = content, author = author, image = image)
    # Список постов, взятых из базы данных
    list_posts = Post.objects.all()
    return render(request, 'forum.html',context={"list_posts":list_posts})