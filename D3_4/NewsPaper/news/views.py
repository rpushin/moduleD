from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

# Create your views here.
class PostList(ListView):
    model = Post
    template_name = 'newslist.html' 
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-timestamp')
    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. в возвращаемом словаре context будут храниться все переменные. ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон


# Create your views here.

class PostFull(DetailView):
    model = Post # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'news.html' # название шаблона будет product.html
    context_object_name = 'post' # название объекта. в нём будет
