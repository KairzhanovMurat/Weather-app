from . import views
from django.urls import path

app_name = 'weather_app'
urlpatterns = [
    path('',views.index,name='home'),
    path('/history',views.History.as_view(),name='history'),
    path('/delete:<int:id>',views.delete,name='delete')
]
