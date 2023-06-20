from django.urls import path
from . import views
from . import views


urlpatterns = [
    path('<int:pk>/', views.UpdateView.as_view(), name='edit_user'),
    ]