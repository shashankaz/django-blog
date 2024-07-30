from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('store/', views.chai_store, name='chai_store'),
]
