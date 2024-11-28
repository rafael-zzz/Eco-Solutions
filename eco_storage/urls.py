from django.urls import path
from usuarios import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),
    path('mapa/',views.mapa,name='mapa'),
    path('ong/<int:id>/', views.OngDetailView.as_view(), name='ong_detail'),
    path('ong/<int:ong_id>/update/', views.update_ong, name='update_ong'),
    path('ong/<int:ong_id>/avaliar/', views.avaliar_ong, name='avaliar_ong'),
    path('adicionar_residuo/<int:ong_id>/', views.adicionar_residuo, name='adicionar_residuo'),
    path('remover_residuo/<int:residuo_id>/', views.remover_residuo, name='remover_residuo'),
]
