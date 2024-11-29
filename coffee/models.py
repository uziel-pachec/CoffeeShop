from django.db import models
from django.db import models
from django.contrib.auth.models import User

#clase para los objetos coffe
class Coffee(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)
    
#clase para la imagen de fondo
class Fondo(models.Model):
    image = models.CharField(max_length=2083)

#clase para un icono rn la plantilla html de inicio
class Modelo(models.Model):
    image = models.CharField(max_length=2083)


#Modelo para los pedidos y detalle de la compra
class pedido_ventaDertalle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #producto rela

    cantidad = models.IntegerField(blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now=True)
    precioUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    productoAsociado = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    
    targeta_credito = models.IntegerField(blank=True)
    



#clase para el registro de los comentarios
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

#clase para el registro de los post que se lancen por el administrador
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




    