from django.urls import path
from .import views

urlpatterns = [
    path("retrieve-and-create/",  views.TodoAPIView.as_view(), name="create"),
    path("edit-todo/<int:pk>/",   views.EditAPIView.as_view(), name="update"),
    path("delete-todo/<int:pk>/", views.DeleteAPIView.as_view(), name="delete")
]