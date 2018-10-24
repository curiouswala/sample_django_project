from . import views
from django.urls import path

urlpatterns = [
    path('<slug:name>', views.hello, name="hello"),
]
