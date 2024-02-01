from django.urls import path
from .import views

app_name = "todo"

urlpatterns = [
    path("",views.home, name="home"),
    path('update', views.updateTodo, name="update"),
	path('create', views.createTodo, name='create'),
	path('delete', views.deleteTodo, name='delete')
]