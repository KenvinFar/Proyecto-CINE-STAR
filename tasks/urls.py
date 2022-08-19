from asyncio import tasks
from django.urls import path
from .views import index, thor, ama, dino, telf, top, light, contactos, peliculas, create_Tickets,login, registros, create_regis,reserva,delete_Tickets

urlpatterns = [
    path('', login),
    path('index/', index),
    path('THOR/', thor),
    path('MINIONS/', ama),
    path('JURASSIC/', dino),
    path('TELF/', telf),
    path('TOP/', top),
    path('LIGHT/', light),
    path('CONTACTOS', contactos),
    path('peliculas/', peliculas, name='peliculas'),
    path('create_Tickets/',create_Tickets,name='create_Tickets'),
    path('login/',login, name='login'),
    path('registros/', registros, name='registros'),
    path('new_inicio/',create_regis, name='create_regis'),
    path('reserva/', reserva, name='reserva'),
    path('delete_Tickets/<int:reser_id>/',delete_Tickets,name='delete_Tickets'),


    
    

]
