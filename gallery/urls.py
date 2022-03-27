from django.urls import path 
from . import views 



urlpatterns = [
    path('' , views.photo_list , name='photo_list '),
    path('<str:id>/', views.photo_view , name='photo'),
    path('category/<str:category>/', views.photo_by_category , name='photo_by_category'),
]
