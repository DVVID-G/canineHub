from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        is_boss = request.POST['is_boss']
        user = User(email=email, name=name, password=password, phone=phone, is_boss=is_boss)
        if email.is_valid():
            user.save()
            return redirect('listar_usuarios')
        else:
            return render(request, 'crear_usuario.html')
    
    return render(request, 'register.html', {'form': form})


def CrearUsuario(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        phone = request.POST['phone']
        is_boss = request.POST['is_boss']
        user = User(email=email, name=name, password=password, phone=phone, is_boss=is_boss)
        if email.is_valid():
            user.save()
            return redirect('listar_usuarios')
        else:
            return render(request, 'crear_usuario.html')