from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('graficador/', views.graficador, name='graficador'),
    path('grafico.png', views.grafico_png, name='grafico_png'),
    path('upload/', views.upload, name='upload'),
    path('archivos/', views.archivos, name='archivos'),
    path('ruleta-general/', views.ruleta_general, name='ruleta_general'),
    path('juego-aritmetico/', views.juego_aritmetico, name='juego_aritmetico'),
    path('juego-24/', views.juego_24, name='juego_24'),
    path('libro/', views.ir_a_drive, name='libro'),
    path('sudoku/', views.sudoku_juego, name='sudoku'),
    path('diff/', views.select_difficulty, name='select_difficulty'),
    path('formulario/', views.formulas_view, name='formulario'),
]