from django.urls import path
from . import views
from shortner.views import create

urlpatterns=[
	path('',views.index,name='index'),
	path('create', views.create, name='create'),
    path('<str:pk>', views.go, name='go')
]