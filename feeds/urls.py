from django.urls import path
from feeds import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:id>', views.show, name='show'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/comments/', views.create_comment, name='create_comment'),
    path('<int:id>/comments/<int:cid>/', views.delete_comment, name='delete_comment'),
    path('<int:pk>/like/', views.feed_like, name='like'),
    # FIXME: Later move to profiles urls.py
    path('<int:pk>/follow/', views.follow_manager, name='follow'),
]
