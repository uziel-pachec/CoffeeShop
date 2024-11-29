from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .form import pedido_ventaDertalleForm, CommentForm, CustomUserCreationForm
from .models import Coffee, Fondo, pedido_ventaDertalle, Modelo
from django.db.models import Q
from .models import Comment, Post
from django.contrib.auth.decorators import login_required


def home(request):#
    fondo = Fondo.objects.first()
    posts = Post.objects.all()
    buscar=request.GET.get("Buscar")
    coffee = Coffee.objects.all()
    no_result=False

    if buscar:                               #condiciona si se realizo una busqueda
        coffee = Coffee.objects.filter(      #Filtra los objetos en el modelo datos en relacion a la busqueda
            Q(name__icontains=buscar)               
        ).distinct()
        if not coffee.exists():
            no_result=True
        
    return render(request, 'home.html', {'coffee': coffee, 'fondo': fondo, 'no_results': no_result, 'posts': posts})  


#funcion de la pagina front.html
def front(request):
    posts = Post.objects.all()
    fondo = Fondo.objects.first()
    modelo = Modelo.objects.first()

    return render(request, 'front.html', {'fondo': fondo, 'posts': posts, 'modelo':modelo})  

@login_required
def order_coffee(request, coffee_id):
    fondo = Fondo.objects.first()                           #se almacena el objeto, imagen que se usara de fondo
    coffee = get_object_or_404(Coffee, id=coffee_id)        #instancia los registros del objeto coffee

    if request.method == 'POST':                            #si se llama a la accion post dentro del formulario
        form = pedido_ventaDertalleForm(request.POST)
        if form.is_valid():
            order_detail = form.save(commit=False)
            order_detail.total = coffee.price * order_detail.cantidad           #registra cantidad total a pagar
            order_detail.precioUnitario = coffee.price                          #registra el precio unitario
            order_detail.productoAsociado = coffee                              #registra el rpoducto seleccionado
            order_detail.user = request.user # Asigna el usuario autenticado al pedido
            order_detail.save()
            return redirect('order_success')               #redirecciona a la pagina de confirmacion de compra
    else:
        form = pedido_ventaDertalleForm()
    return render(request, 'order_coffee.html', {'coffee': coffee, 'form': form, 'fondo':fondo})


#funcion de  vista para la pagina de confirmacion una vex echo la compra
def order_success(request):
    fondo = Fondo.objects.first()
    return render(request, 'order_success.html', {'fondo':fondo})


#Funcion vista para hacer las consultas de las compras y pedidos que se hicieron
@login_required
def shoppingcars(request):
    user = request.user 
    pedido_ventaDetalle = pedido_ventaDertalle.objects.filter(user=user)
    
    fondo = Fondo.objects.first()
  
    return render(request, 'ShoppingCars.html',  {'fondo':fondo, 'pedido_ventaDetalle': pedido_ventaDetalle} )


#funcion vista para la muestra de los comentarios
def post_detail(request, pk):
    fondo = Fondo.objects.first()
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form, 'fondo': fondo})



#fffffffffffffffffffffffffffffffffffffffffffffff

def signup(request):
    fondo = Fondo.objects.first()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form, 'fondo': fondo})



from django.contrib.auth.views import LoginView

class LoginView(LoginView):
    template_name = 'login.html'
    



