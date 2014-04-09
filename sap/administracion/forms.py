from django import forms
from django.contrib.auth.models import User
from administracion.models import Rol
from administracion.models import TipoAtributo, TIPO_DATO

class CrearUsuarioForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(), required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput(), required=True)
    password_uno = forms.CharField(label="Contrasenha", widget=forms.PasswordInput(render_value=False), required=True)
    password_dos = forms.CharField(label="Confirmar contrasenha", widget=forms.PasswordInput(render_value=False), required=True)
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(), required=True)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(), required=True)
    direccion = forms.CharField(label="Direccion", widget=forms.TextInput(), required=False)
    telefono = forms.CharField(label="Telefono", widget=forms.TextInput(), required=False)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            usuario = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya registrado')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya registrado')
    
    def clean_password_dos(self):
        password_uno = self.cleaned_data['password_uno']
        password_dos = self.cleaned_data['password_dos']
        if password_uno == password_dos:
            pass
        else:
            raise forms.ValidationError('Las claves no coinciden')
        
class ModificarUsuarioForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(), required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput(), required=True)
    password_uno = forms.CharField(label="Contrasenha", widget=forms.PasswordInput(render_value=False), required=True)
    password_dos = forms.CharField(label="Confirmar contrasenha", widget=forms.PasswordInput(render_value=False), required=True)
    first_name = forms.CharField(label="Nombre", widget=forms.TextInput(), required=True)
    last_name = forms.CharField(label="Apellido", widget=forms.TextInput(), required=True)
    direccion = forms.CharField(label="Direccion", widget=forms.TextInput(), required=False)
    telefono = forms.CharField(label="Telefono", widget=forms.TextInput(), required=False)
    
    def clean_password_dos(self):
        password_uno = self.cleaned_data['password_uno']
        password_dos = self.cleaned_data['password_dos']
        if password_uno == password_dos:
            pass
        else:
            raise forms.ValidationError('Las claves no coinciden')
        
class CrearRolForm(forms.Form):
    nombre = forms.CharField(label="Nombre de rol", widget=forms.TextInput(), required=True)
    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea(), required=True)
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            rol = Rol.objects.get(nombre=nombre)
        except Rol.DoesNotExist:
            return nombre
        raise forms.ValidationError('Nombre de rol ya registrado')

class ModificarRolForm(forms.Form):
    nombre = forms.CharField(label="Nombre de rol", widget=forms.TextInput(), required=True)
    descripcion = forms.CharField(label="Descripcion", widget=forms.TextInput(), required=True)
        
    def clean_nombre(self): 
        nombre = self.cleaned_data['nombre'] 
        try: 
            rol = Rol.objects.get(nombre=nombre) 
            if rol.nombre == nombre:
                return nombre 
        except Rol.DoesNotExist:
            return nombre 
        raise forms.ValidationError('Nombre de rol ya registrado')

class CrearTipoAtributoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de tipo atributo", widget=forms.TextInput(), required=True)
    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea(), required=True)
    tipo_dato = forms.ChoiceField(label="Tipo dato",choices=TIPO_DATO, required=True)
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        try:
            tipo_atributo = TipoAtributo.objects.get(nombre=nombre)
        except TipoAtributo.DoesNotExist:
            return nombre
        raise forms.ValidationError('Nombre de tipo atributo ya registrado')

    