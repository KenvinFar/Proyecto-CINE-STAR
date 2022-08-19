from django.shortcuts import render,redirect

from .models import reservation, usuario, movie
from django.contrib import messages

# Create your views here.
def index(request):
    return render (request, 'index.html')
def thor (request):
    return render (request, 'THOR.html')
def ama (request):
    return render (request, 'MINIONS.html')
def dino (request):
    return render (request, 'JURASSIC.html')
def telf (request):
    return render (request, 'TELEF.html')
def top (request):
    return render (request, 'TOP.html')
def light (request):
    return render (request, 'LIGHT.html')
def contactos (request):
    return render (request, 'CONTACTOS.html')
def peliculas (request):
    return render (request, 'peliculas.html')

def reserva (request):
    ticket=reservation.objects.all()
    return render (request, 'reserva.html',{'reservation': ticket})

#redirecion al usuario
def new_user (request):
    task= usuario()

#redirecion al create
def create_Tickets(request):
    #print(request.POST)
    task=reservation( 
                     Nombre= request.POST['Nombre'],
                     language_movie = request.POST['language_movie'], 
                     duration = request.POST['duration'], 
                     seating= request.POST['seating'], 
                     location = request.POST['location'])  
    task.save()
    return redirect('/CINE-STAR/reserva/')

def login (request):
    return render (request,'login.html')

def registros (request):
    return render (request, 'registros.html')

def create_regis (request):
     reg=usuario(name=request.POST['name'],
                 email=request.POST['email'],
                 phone=request.POST['phone'],
                 address=request.POST['address'],
                 user=request.POST['user'],
                 password=request.POST['password'])
     reg.save()
     return redirect ('/CINE-STAR/login/')

def login(request):
    if request.method == 'POST':
        try:
            cine = usuario.objects.get(user=request.POST['user1'], password=request.POST['password1'])
            print("Usuario", cine)
            request.session['user'] = cine.user
            return render(request, 'index.html')
        except usuario.DoesNotExist as e:
            print('Usuario o contraseña no registrados')
    return render(request, 'login.html')

def delete_Tickets(request,reser_id):
    ticket=reservation.objects.get(id=reser_id)
    ticket.delete();
    return redirect('/CINE-STAR/reserva/')


  