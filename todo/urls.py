from django.urls import path
from . import views
from . import class_views

# #Вложенность для пост/posts/
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('create/', views.create_post, name='create_post'),
#     path('<int:post_id>/', views.show_post, name='show_post'),
#     path('<int:post_id>/edit', views.edit_post, name='edit_post'),
#     path('<int:post_id>/delete', views.post_delete, name='delete_post'),
#     ]

#Вложенность для пост/posts/ c классами
#Для определение маршрутов через класс обязательно должно быть вызван классовый метод.as_view()

urlpatterns = [
    path('', class_views.PostsList.as_view(), name='home'),
    path('nn/', class_views.NotNumbersPostsList.as_view()),
    path('create/', class_views.CreatPost.as_view(), name='create_post'),
    path('<int:post_id>/', views.show_post, name='show_post'),
    path('<int:post_id>/edit', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete', views.post_delete, name='delete_post'),
    ]