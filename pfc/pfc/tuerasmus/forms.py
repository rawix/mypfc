#encoding:utf-8

##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 07/10/13.                                                      #
# @Description : Forms to be used.                                       #
##########################################################################

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from tuerasmus.models import City, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistics, Residence, Subjects, Universities, University, UserProfile, Users, UsersUniversity

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
    description = forms.CharField(label="Biografía")
    university = forms.CharField(label="Universidad", widget=forms.TextInput())
    uni_reg = forms.BooleanField(required=False)
    photo = forms.ImageField(label="Imagen de perfil", required=False)

#----------------------------------------------------------------------------
#            Class BasicForm: to change the university profile   
#----------------------------------------------------------------------------
class BasicForm(forms.Form):
    acronym = forms.CharField(label="Siglas de la universidad", widget=forms.TextInput(), required=False)
    address = forms.CharField(label="Dirección", widget=forms.TextInput(), required=False)
    city = forms.CharField(label="Ciudad de la universidad", widget=forms.TextInput(), required=False)
    country = forms.CharField(label="País de la universidad", widget=forms.TextInput(), required=False)

    #Revisar como se ponen los link en un formulario!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    latitud = forms.DecimalField(label='Coordenadas de latitud', required=False)
    longitud = forms.DecimalField(label='Coordenadas de longitud', required=False)
    link = forms.URLField(label='Web oficial de la universidad', required=False)
    image = forms.URLField(label='Alguna imagen de la universidad', required=False)

    description = forms.CharField(label="Descripción breve sobre la universidad", widget=forms.TextInput(), required=False)
    qualification = forms.CharField(label="Titulación impartida", widget=forms.TextInput(), required=False)

    specialty = forms.CharField(label="Especialidades", widget=forms.TextInput(), required=False)
    
    teachingequipment = forms.CharField(label="Equipamiento docente", widget=forms.TextInput(), required=False)
    # SubMenu
    librariy = forms.CharField(label="Bibliotecas", widget=forms.TextInput(), required=False)
    lab = forms.CharField(label="Laboratorios", widget=forms.TextInput(), required=False)
    computerequipment = forms.CharField(label="Equipos informáticos", widget=forms.TextInput(), required=False) 

    others = forms.CharField(label="Especialidades", widget=forms.TextInput(), required=False)
    # SubMenu
    dinningroom = forms.CharField(label="Comedores universitarios", widget=forms.TextInput(), required=False)
    cafeteria = forms.CharField(label="Cafeterías", widget=forms.TextInput(), required=False)
    sportactivities = forms.CharField(label="Actividades deportivas", widget=forms.TextInput(), required=False)
    asociation = forms.CharField(label="Asociaciones universitarias", widget=forms.TextInput(), required=False)
    languagecourse = forms.CharField(label="Cursos de idiomas", widget=forms.TextInput(), required=False)
  
    schoolyear = forms.CharField(label="Periodo lectivo", widget=forms.TextInput(), required=False)
    vacations = forms.CharField(label="Vacaciones/Fiestas", widget=forms.TextInput(), required=False)
    compteleco = forms.CharField(label="En comparación con teleco", widget=forms.TextInput(), required=False)
    # SubMenu
    teachers = forms.CharField(label="Calidad/Dedicación/Atención de profesorado", widget=forms.TextInput(), required=False)
    teaching = forms.CharField(label="Calidad global de la enseñanza", widget=forms.TextInput(), required=False)
    studies = forms.CharField(label="Nivel de exigencia de los estudios", widget=forms.TextInput(), required=False)
  
#----------------------------------------------------------------------------
#            Class CostumerServiceForm: to change the university profile   
#----------------------------------------------------------------------------
class CostumeServiceForm(forms.Form):
    costume = forms.CharField(label="Atención a los estudiantes Erasmus", widget=forms.TextInput(), required=False)
    # SubMenu
    meetings = forms.CharField(label="Reuniones para Erasmus", widget=forms.TextInput(), required=False)
    offices = forms.CharField(label="Oficinas de Asuntos Extranjeros", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class DocumentationForm: to change the university profile   
#----------------------------------------------------------------------------
class DocumentationForm(forms.Form):
    unidoc = forms.CharField(label="Documentación necesaria en la universidad", widget=forms.TextInput(), required=False)
    residencelicence = forms.CharField(label="Obtener permiso de residencia", widget=forms.TextInput(), required=False)
    getresidence = forms.CharField(label="Obtener alojamiento", widget=forms.TextInput(), required=False)
    economicaid = forms.CharField(label="Obtener ayudas económicas", widget=forms.TextInput(), required=False)
    bankaccount = forms.CharField(label="Abrir cuenta bancaria", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class AccommodationForm: to change the university profile   
#----------------------------------------------------------------------------
class AccommodationForm(forms.Form):
    residencehall = forms.CharField(label="Residencias de estudiantes", widget=forms.TextInput(), required=False)
    flatshare = forms.CharField(label="Pisos compartidos", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class SubjectsForm: to change the university profile   
#----------------------------------------------------------------------------
class SubjectsForm(forms.Form):
    subjects = forms.CharField(label="Asignaturas", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class WorkForm: to change the university profile   
#----------------------------------------------------------------------------
class WorkForm(forms.Form):
    scholarships = forms.CharField(label="Becas", widget=forms.TextInput(), required=False)
    practices = forms.CharField(label="Trabajo", widget=forms.TextInput(), required=False)
    contact = forms.CharField(label="Contacto con empresas", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class CityForm: to change the university profile   
#----------------------------------------------------------------------------
class CityForm(forms.Form):
    general = forms.CharField(label="En general", widget=forms.TextInput(), required=False)
    prices = forms.CharField(label="Precios", widget=forms.TextInput(), required=False)
    theuniversity = forms.CharField(label="La universidad", widget=forms.TextInput(), required=False)
    studentlife = forms.CharField(label="Vida estudiantil", widget=forms.TextInput(), required=False)
    turism = forms.CharField(label="Turismo", widget=forms.TextInput(), required=False)
    goingout = forms.CharField(label="Salir", widget=forms.TextInput(), required=False)
    culture = forms.CharField(label="Cultura", widget=forms.TextInput(), required=False)
    crime = forms.CharField(label="Delincuencia", widget=forms.TextInput(), required=False)
    shopping = forms.CharField(label="De compras", widget=forms.TextInput(), required=False)
    erasmuslife = forms.CharField(label="Ambiente erasmus", widget=forms.TextInput(), required=False)
    more = forms.CharField(label="Más cosas", widget=forms.TextInput(), required=False)

#----------------------------------------------------------------------------
#            Class OthersForm: to change the university profile   
#----------------------------------------------------------------------------
class OthersForm(forms.Form):
    others = forms.CharField(label="Varios", widget=forms.TextInput(), required=False)

