from django.urls import path

from . import views

app_name = 'demo_app1'

urlpatterns = [
    path('<int:pk>/query/', views.QueryView.as_view(), name='query'),
]