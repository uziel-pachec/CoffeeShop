from django import forms
from .models import pedido_ventaDertalle
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class pedido_ventaDertalleForm(forms.ModelForm):    #clase el formulario para realizar pedido
    class Meta:
        model = pedido_ventaDertalle
        fields = ['cantidad', 'targeta_credito']


class CommentForm(forms.ModelForm):                  #Clase para el formulario de la pagina de comentarios
    class Meta:
        model = Comment
        fields = ['text']


#ddddddddddddddddddddddddddddddddddddd


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Introduzca una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




