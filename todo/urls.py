from django.urls import path
from . import views
from . import class_views
from . import new_view
from dashboard import settings
from django.conf.urls.static import static

# #Вложенность для пост/posts/
#
# urlpatterns = [
#     path('', views.home, name='home'),
#     path('create/', views.create_post, name='create_post'),
#     path('<int:post_id>/', views.show_post, name='show_post'),
#     path('<int:post_id>/edit', views.edit_post, name='edit_post'),
#     path('<int:post_id>/delete', views.post_delete, name='delete_post'),
#     ]

# #Вложенность для пост/posts/ c классами
# #Для определение маршрутов через класс обязательно должно быть вызван классовый метод.as_view()
#
# urlpatterns = [
#     path('', class_views.PostsList.as_view(), name='home'),
#     path('nn/', class_views.NotNumbersPostsList.as_view()),
#     path('create/', class_views.CreatPost.as_view(), name='create_post'),
#     path('<int:post_id>/', views.show_post, name='show_post'),
#     path('<int:post_id>/edit', class_views.EditPost.as_view(), name='edit_post'),
#     path('<int:post_id>/delete', views.post_delete, name='delete_post'),
#     ]

#Вложенность для реализации по книге
# #Для определение маршрутов через класс обязательно должно быть вызван классовый метод.as_view()
#
urlpatterns = [
    path('home/', new_view.PostsList.as_view(), name='home'),
    path('nn/', class_views.NotNumbersPostsList.as_view()),
    path('create/', new_view.CreatPost.as_view(), name='create_post'),
    path('<int:pk>/', new_view.ShowPost.as_view(), name='show_post'),
    path('<int:pk>/edit', new_view.EditPost.as_view(), name='edit_post'),
    path('<int:pk>/delete', new_view.DeletePost.as_view(), name='delete_post'),
    path('userlist/', new_view.UserList.as_view(), name='user_list'),
    path('commentslist/', new_view.StatisticComents.as_view(), name='show_comments'),
    path('<int:pk>/createcomment', new_view.CreateComent.as_view(), name='create_comment'),
    path('userlist/', new_view.UserList.as_view(), name='user_list'),
    path('<int:pk>/userinfo/', new_view.UserEdit.as_view(), name='user_info'),
    ]