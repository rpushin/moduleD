from django.urls import path
from .views import PostList, PostFull

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostFull.as_view())
]