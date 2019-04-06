from django.conf.urls import include
from django.urls import path
from feeds import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>', views.show, name='show'),
    path('<int:id>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
]
