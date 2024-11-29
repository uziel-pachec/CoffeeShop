from django.contrib import admin
from .models import Coffee, Fondo ,  pedido_ventaDertalle, Post,  Comment, Modelo


class CoffeeAdmin(admin.ModelAdmin):     #clase para especificar los datos de agregacion en el administrador django
    list_display = ('name', 'price', 'quantity')

#registra los modelos creados en el adinistrador django para su manipulacion
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Fondo)
admin.site.register(Modelo)
admin.site.register(pedido_ventaDertalle)
admin.site.register(Post)
admin.site.register(Comment)


