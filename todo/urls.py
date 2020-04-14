from django.urls import path,include
from .import views
app_name='todo'

urlpatterns = [
    path('',views.overview, name='overview'),
    path('list', views.list, name='list'), 
    path('detail/<int:item-id>/', views.detail, name='detail'),
    path('create',views.create, name='create'),
    path('update/<int:item_id>/',views.update, name='update'),
    path('delete/<int:item_id>/', views.delete, name='delete')
]
