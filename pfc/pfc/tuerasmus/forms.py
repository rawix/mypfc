#encoding:utf-8

##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 07/10/13.                                                      #
# @Description : Forms to be used.                                       #
##########################################################################

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils import timezone 
from tuerasmus.models import City, Cities, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistic, Others, Place, Resis, Score, Subjs, Subjects, Universities, University, UserProfile, Users, UsersUniversity

#import datetime

#----------------------------------------------------------------------------
#            Class RegisterForm: to register the user  
#----------------------------------------------------------------------------     
class RegisterForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(), error_messages={'required': 'Debes introducir un nombre de usuario'})
    email = forms.EmailField(label="Correo electrónico (gmail)", widget=forms.TextInput(), error_messages={'required': 'Debes introducir un correo electrónico', 'invalid':u'Introduce un correo válido'})
    password_one = forms.CharField(label="Contraseña (6 caracteres)", widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Debes introducir una contraseña'})
    password_two = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Debes volver a introducir la contraseña'})
    #day = forms.DateField(label="Fecha de registro", widget=forms.TextInput(), initial=datetime.date.today)

    # Data validation
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario registrado')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            e = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return email
        raise forms.ValidationError('Correo electrónico registrado')

    def clean_password_two(self):  
        password_one = self.cleaned_data.get('password_one', '')
        password_two = self.cleaned_data.get('password_two', '')
        if (not password_one):
            error_msg = u'Debes introducir una contraseña'
            self._errors['password_one'] = self.error_class([error_msg]) 
        elif (not password_two):
            error_msg = u'Debes introducir una contraseña'
            self._errors['password_two'] = self.error_class([error_msg])
        elif password_one and password_two and (password_one == password_two):
            pass
        else:
            raise forms.ValidationError('Contraseñas no coinciden')

#----------------------------------------------------------------------------
#            Class ProfileForm: to change the user profile 
#----------------------------------------------------------------------------
class ProfileForm(forms.Form):
    name = forms.CharField(label="Nombre", widget=forms.TextInput(), error_messages={'required': 'Debes introducir tu nombre'})
    lastname = forms.CharField(label="Apellidos", widget=forms.TextInput(), error_messages={'required': 'Debes introducir tus apellidos'})
    description = forms.CharField(label="Cómo te definirías en pocas palabras", required=False)
    image = forms.ImageField(label="Imagen de perfil", required=False)

#----------------------------------------------------------------------------
#            Class PasswordForm: to change the password 
#----------------------------------------------------------------------------
class PasswordForm(forms.Form):
    password_one = forms.CharField(label="Contraseña (6 caracteres)", widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Debes introducir una contraseña'})
    password_two = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(render_value=False), error_messages={'required': 'Debes volver a introducir la contraseña'})

    def clean_password_two(self):  
        password_one = self.cleaned_data.get('password_one', '')
        password_two = self.cleaned_data.get('password_two', '')
        if (not password_one):
            error_msg = u'Debes introducir una contraseña'
            self._errors['password_one'] = self.error_class([error_msg]) 
        elif (not password_two):
            error_msg = u'Debes introducir una contraseña'
            self._errors['password_two'] = self.error_class([error_msg])
        elif password_one and password_two and (password_one == password_two):
            pass
        else:
            raise forms.ValidationError('Contraseñas no coinciden')

#----------------------------------------------------------------------------
#            Class ImageForm: to change the university image  
#----------------------------------------------------------------------------
class ImageForm(forms.Form):
    image_profile = forms.ImageField(label="Imagen de universidad", required=False)

#----------------------------------------------------------------------------
#            Class BasicForm: to change the university profile   
#----------------------------------------------------------------------------
class BasicForm(forms.Form):
  
#class BasicForm(forms.ModelForm):
    #class Meta:
    #    model = InfoBasic
    #    fields = ('address', 'city', 'country', 'latitud', 'longitud', 'link', 'image', 'description')
        
    address = forms.CharField(label="Dirección", widget=forms.TextInput(), error_messages={'required': 'Debes introducir la dirección'})
    postalcode = forms.IntegerField(label="Código postal", widget=forms.TextInput(), required=False)
    phone = forms.IntegerField(label="Teléfono de contacto", widget=forms.TextInput(), error_messages={'required': 'Debes introducir un teléfono de contacto', 'invalid':u'Introduce el teléfono sin el prefijo'})
    prefix = forms.IntegerField(label="Prefijo telefónico", widget=forms.TextInput(), error_messages={'required': 'Debes introducir un teléfono de contacto', 'invalid':u'Introduce el prefijo telefónico'})
    city = forms.CharField(label="Ciudad", widget=forms.TextInput(), error_messages={'required': 'Debes introducir la ciudad'})
    country = forms.CharField(label="País", widget=forms.TextInput(), error_messages={'required': 'Debes introducir el país'})
    latitud = forms.DecimalField(label='Coordenadas de latitud', widget=forms.TextInput(), error_messages={'required': 'Debes introducir la coordenada de latitud'})
    longitud = forms.DecimalField(label='Coordenadas de longitud', widget=forms.TextInput(), error_messages={'required': 'Debes introducir la coordenada de longitud'})
    link = forms.URLField(label='Web oficial de la universidad', widget=forms.TextInput(), error_messages={'required': 'Debes introducir la web oficial de la universidad', 'invalid':u'Introduce una URL válida'})
    image = forms.ImageField(label="Imagen de universidad", error_messages={'required': 'Debes seleccionar una imagen'})
    description = forms.CharField(label="Descripción breve sobre la universidad", widget=forms.Textarea(), error_messages={'required': 'Debes introducir una breve descripción'})

#----------------------------------------------------------------------------
#            Class AreaForm: to change the university profile   
#----------------------------------------------------------------------------
class AreaForm(forms.Form):
    qualification = forms.CharField(label="Titulación impartida", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    specialty = forms.CharField(label="Especialidades", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    teachingequipment = forms.CharField(label="Equipamiento docente", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    # SubMenu
    library = forms.CharField(label="Bibliotecas", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    lab = forms.CharField(label="Laboratorios", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    computerequipment = forms.CharField(label="Equipos informáticos", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'}) 

    others = forms.CharField(label="Otras observaciones", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    # SubMenu
    dinningroom = forms.CharField(label="Comedores universitarios", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    cafeteria = forms.CharField(label="Cafeterías", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    sportactivities = forms.CharField(label="Actividades deportivas", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    asociation = forms.CharField(label="Asociaciones universitarias", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    languagecourse = forms.CharField(label="Cursos de idiomas", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
  
    schoolyear = forms.CharField(label="Periodo lectivo", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    vacations = forms.CharField(label="Vacaciones/Fiestas", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    compteleco = forms.CharField(label="Dificultades en los estudios", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    # SubMenu
    teachers = forms.CharField(label="Calidad/Dedicación/Atención de profesorado", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    teaching = forms.CharField(label="Calidad global de la enseñanza", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    studies = forms.CharField(label="Nivel de exigencia de los estudios", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
  
#----------------------------------------------------------------------------
#            Class CostumerServiceForm: to change the university profile   
#----------------------------------------------------------------------------
class CostumeServiceForm(forms.Form):
    costume = forms.CharField(label="Atención a los estudiantes Erasmus", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    # SubMenu
    meetings = forms.CharField(label="Reuniones para Erasmus", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    offices = forms.CharField(label="Oficinas de Asuntos Extranjeros", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})

#----------------------------------------------------------------------------
#            Class DocumentationForm: to change the university profile   
#----------------------------------------------------------------------------
class DocumentationForm(forms.Form):
    unidoc = forms.CharField(label="Documentación necesaria", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    residencelicence = forms.CharField(label="Seguro médico", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    getresidence = forms.CharField(label="Alojamiento", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    economicaid = forms.CharField(label="Ayudas económicas", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    bankaccount = forms.CharField(label="Servicios bancarios", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})

#----------------------------------------------------------------------------
#            Class ResidenceForm: to change the university profile   
#----------------------------------------------------------------------------
class ResidenceForm(forms.Form):
    flatshare = forms.CharField(label="Pisos compartidos", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    linktoshare = forms.CharField(label="Páginas web para pisos compartidos", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})

#----------------------------------------------------------------------------
#            Class PlaceForm: to change the university profile   
#----------------------------------------------------------------------------
class PlaceForm(forms.Form):
    name = forms.CharField(label="Nombre del sitio", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    address = forms.CharField(label="Dirección", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    postalcode = forms.IntegerField(label="Código postal", widget=forms.TextInput(), required=False)
    city = forms.CharField(label="Ciudad", widget=forms.TextInput(), error_messages={'required':'Debes rellenar este campo'})
    latitud = forms.DecimalField(label="Coordenadas de latitud", widget=forms.TextInput(), error_messages={'required': 'Debes introducir la coordenada de latitud'})
    longitud = forms.DecimalField(label="Coordenadas de longitud", widget=forms.TextInput(), error_messages={'required': 'Debes introducir la coordenada de longitud'})
    image = forms.URLField(label="Imagen (copia la URL de internet)", widget=forms.TextInput(), error_messages={'required': 'Debes introducir la URL de una imagen', 'invalid':u'Introduce una URL válida'}, )

#----------------------------------------------------------------------------
#            Class SubjectsForm: to change the university profile   
#----------------------------------------------------------------------------
class SubjectsForm(forms.Form):
    subname = forms.CharField(label="Asignatura en la URJC", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    credits = forms.DecimalField(label="Créditos de la asignatura", widget=forms.TextInput(), error_messages={'required': 'Debes rellenar este campo', 'invalid':u'Debes introducir un número'})
    subnameout = forms.CharField(label="Asignatura cursada fuera", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    subnameout2 = forms.CharField(label="Otra asignatura cursada fuera", widget=forms.Textarea(), required=False)
    subnameout3 = forms.CharField(label="Otra más cursada fuera", widget=forms.Textarea(), required=False)
    works = forms.CharField(label="Trabajos a entregar", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    practices = forms.CharField(label="Prácticas a realizar", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
    difficult = forms.CharField(label="Dificultad de la asignatura fuera", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar este campo'})
      
#----------------------------------------------------------------------------
#            Class WorkForm: to change the university profile   
#----------------------------------------------------------------------------
class WorkForm(forms.Form):
    scholarships = forms.CharField(label="Becas", widget=forms.Textarea(), required=False)
    practices = forms.CharField(label="Trabajo", widget=forms.Textarea(), required=False)
    contact = forms.CharField(label="Contacto con empresas", widget=forms.Textarea(), required=False)

#----------------------------------------------------------------------------
#            Class CityForm: to change the university profile   
#----------------------------------------------------------------------------
class CityForm(forms.Form):
    cityname = forms.CharField(label="Nombre de la ciudad", widget=forms.TextInput(), error_messages={'required':'Debes rellenar este campo'})
    prices = forms.CharField(label="Precios", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    uniarea = forms.CharField(label="La universidad", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    studentlife = forms.CharField(label="Vida estudiantil", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    turism = forms.CharField(label="Turismo", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    party = forms.CharField(label="Salir", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    culture = forms.CharField(label="Cultura", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    crime = forms.CharField(label="Delincuencia", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    shopping = forms.CharField(label="De compras", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    erasmuslife = forms.CharField(label="Ambiente erasmus", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    more = forms.CharField(label="Más cosas", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})

#----------------------------------------------------------------------------
#            Class OthersForm: to change the university profile   
#----------------------------------------------------------------------------
class OthersForm(forms.Form):
    tema = forms.CharField(label="Tema de información(documentación, residencias, asignaturas, la ciudad)", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    title = forms.CharField(label="Título de tu comentario", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    body_text = forms.CharField(label="El contenido de tu comentario", widget=forms.Textarea(), error_messages={'required':'Debes rellenar este campo'})
    
#----------------------------------------------------------------------------
#            Class ContactForm: to contact any user  
#----------------------------------------------------------------------------    
class ContactForm(forms.Form):
    username = forms.CharField(label="Usuario",widget=forms.TextInput())
    subject = forms.CharField(label="Asunto",max_length=100, widget=forms.TextInput())
    message = forms.CharField(label="Mensaje",widget=forms.Textarea())
    #sender = forms.EmailField(label="EL desarrollador (rawankho@gmail.com)",widget=forms.TextInput(), error_messages={'required':'Debes rellenar este campo', 'invalid':u'Introduce un correo válido'})
    #cc_myself = forms.BooleanField(label="Ponerme en CC", required=False)
    
#----------------------------------------------------------------------------
#            Class CommentForm: to comment anything
#----------------------------------------------------------------------------
class CommentForm(forms.Form):
    title = forms.CharField(label="Título del comentario", widget=forms.TextInput(), error_messages={'required': 'Pon un título para el comentario'})
    text = forms.CharField(label="Escribe tu comentario", widget=forms.Textarea(), error_messages={'required': 'Debes rellenar el campo'})


