
from django.contrib import admin
from django.urls import path,include
from Agencyapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name = 'index'),
    path('innerpage/', views.inner,name='inner'),
]
