
from django.urls import path
from. import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('delete/<List_id>', views.delete, name='delete'),
    path('cross/<List_id>', views.cross, name='cross'),
    path('uncross/<List_id>', views.uncross, name='uncross'),
    
    
]
