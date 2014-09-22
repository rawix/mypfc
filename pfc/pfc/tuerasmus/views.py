#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Views that handle the urls selected.                    #
##########################################################################

# Libraries.
import sys

# Forms
from django.forms import ModelForm
from django import forms

# Auth
from django.contrib import auth
from django.contrib.auth.models import User

# HTTP mssages.
from django.http import HttpResponse
from django.http import Http404  
from django.http import HttpResponseRedirect

#CSRF
from django.core.context_processors import csrf

# Cross Site Request Forgery protection
from django.views.decorators.csrf import csrf_exempt

# HTML short way for rendering.
from django.shortcuts import render_to_response, get_object_or_404

# HTML rendering libraries.
from django.template import RequestContext, loader

# Sending HTML
from django.core.mail import EmailMessage, EmailMultiAlternatives 

# Date
from datetime import datetime, date

# Database tables.  
from tuerasmus.models import City, Cities, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistic, Others, Place, Resis, Score, Subjs, Subjects, Universities, University, UserProfile, Users, UsersUniversity

# Forms
from tuerasmus.forms import ProfileForm, BasicForm, AreaForm, CommentForm, CostumeServiceForm, DocumentationForm, ImageForm, ResidenceForm, PasswordForm, PlaceForm, SubjectsForm, WorkForm, CityForm, OthersForm



# =======================================================================
#                       TuErasmus methods
# =======================================================================

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------


#Desactivation of CSRF
@csrf_exempt

# Name : HOME USER
def home(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):
            print "HOME USER: User authenticated: " + user

            # User is professor or student
            # User has a profile image
            type_user=""
            path_image=""
            description=""
            genero=""
            t = User.objects.get(username=user)
            tt = t.username
            tu = Users.objects.all()
            tp = UserProfile.objects.all()
            for i in tu:
                if (tt == str(i.username)):
                    type_user = str(i.type_user)
                    genero = str(i.genero)
                    
            # Get the path of the image and the user description  
            for j in tp:              
                if (tt == str(j.username)):
                    # No photo and no description
                    if ((str(j.name_image)=="") or (str(j.name_image)=="None")) and ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Estudiante de la ETSIT"
                        
                    # No photo but yes description
                    elif ((str(j.name_image)=="") or (str(j.name_image)=="None")) and not ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = (j.description)
                        
                    # No description but yes photo
                    elif ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Estudiante de la ETSIT"
                    
                     # Yes photo and description
                    elif not ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = (j.description)
                        

            # Return the template
            ctx = {'username': user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/home.html', ctx, context_instance=RequestContext(request))
            
        else:
            # User authenticated and user requested are differents
            print "HOMEUSER: User authenticated and user requested are differents"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
              
    else:
        # User no authenticated
        print "HOME USER: User no authenticated"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : MYPROFILE
def myprofile(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):
            
            print "MYPROFILE: user authenticated " + request.user.username
            print "MYPROFILE: user requested " + user
            
            # Concatenate URL + username
            ur = "/tuerasmus/" + user + "/profile"
            print "MYPROFILE: " + ur
            # Redirect url
            return HttpResponseRedirect(ur)
        else:
            # User authenticated and user requested are differents
            print "MYPROFILE: User authenticated and user requested are differents"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User no authenticated
        print "MYPROFILE: User no authenticated"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : PROFILE
def profile(request, user):

    if request.user.is_authenticated():
       
        print "PROFILE: user authenticated " + request.user.username
        print "PROFILE: user requested " + user
                   
        # User is professor or student
        # User has a profile image
        type_user=""
        path_image=""
        description=""
        try:
            t = User.objects.get(username=user)
        except User.DoesNotExist:
            return HttpResponseRedirect("/tuerasmus")
            
        tt = t.username
        tu = Users.objects.all()
        tp = UserProfile.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)
                genero = str(i.genero) 
                user_email = str(i.email)  
                print tt  
                print type_user
                print genero
                print user_email
                
        # Get the path of the image and the user description
        for j in tp:
        
            if (tt == str(j.username)):
                # No photo and no description
                if ((str(j.name_image)=="") or (str(j.name_image)=="None")) and ((j.description)==""):
                    if genero=="male":
                        path_image ="tuerasmus/male.jpg"
                    elif genero=="female":
                        path_image="tuerasmus/female.jpg"
                    description = "Estudiante de la ETSIT"
                    print "111111111111111111111111111111111111111111111!"
                # No photo but yes description
                elif ((str(j.name_image)=="") or (str(j.name_image)=="None")) and not ((j.description)==""):
                    if genero=="male":
                        path_image ="tuerasmus/male.jpg"
                    elif genero=="female":
                        path_image="tuerasmus/female.jpg"               
                    description = (j.description)
                    print "22222222222222222222222222222222222222222222222"
                # No description but yes photo
                elif ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                    path_image = "profiles/" + str(j.name_image)
                    description = "Estudiante de la ETSIT"
                    print "33333333333333333333333333333333333333333333333333333333333"
                # Yes photo and description
                elif not ((j.description)=="") and (not (str(j.name_image)=="None") or not (str(j.name_image)=="")):
                    path_image = "profiles/" + str(j.name_image)
                    description = (j.description)
                    print "44444444444444444444444444444444444444444444444444444444444444444"
                    
                if (j.uni1=="") or (j.uni1==None):
                    showuni1 = False
                elif not (j.uni1=="") and not (j.uni1==None):
                    showuni1 = True
                    
                if (j.uni2=="") or (j.uni2==None):
                    showuni2 = False
                elif not (j.uni2=="") and not (j.uni2==None):
                    showuni2 = True

                ctx = {'up_obj':j, 'showuni1':showuni1, 'showuni2':showuni2, 'see_profile':True, 'username': user, 'user_email':user_email, 'type_user': type_user, 'genero':genero, 'path_image':path_image, 'description':description}

        # Return the template
        return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))

    else:
        # User no authenticated
        print "PROFILE: User no authenticated"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')
        
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : EDIT_PROFILE
def edit_profile(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):

            print "EDIT_PROFILE: user authenticated " + request.user.username
            print "EDIT_PROFILE: user requested: " + user
                
            # Concatenate the URL with username
            ur = '/tuerasmus/' + user + '/edit_profile/'
            print "EDIT_PROFILE: " + ur
            
            # User is professor or student
            # User has a profile image
            type_user=""
            path_image=""
            description=""
            t = User.objects.get(username=user)
            tt = t.username
            tu = Users.objects.all()
            tp = UserProfile.objects.all()
            for i in tu:
                if (tt == str(i.username)):
                    type_user = str(i.type_user)
                    genero = str(i.genero)
                    
            # Get the path of the image and the user description
            for j in tp:
                
                if (tt == str(j.username)):
                    # No photo and no description
                    if ((str(j.name_image)=="") or (str(j.name_image)=="None")) and ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Estudiante de la ETSIT"
                        print "!1111111111"
                    # No photo but yes description
                    elif ((str(j.name_image)=="") or (str(j.name_image)=="None")) and not ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = (j.description)
                        print "2222222222222222222222222"
                        
                    # No description but yes photo
                    elif ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Estudiante de la ETSIT"
                        print "3333333333333333333333333333"
                    # Yes photo and description
                    elif not ((j.description)=="") and (not (str(j.name_image)=="None") or not (str(j.name_image)=="")):
                        path_image = "profiles/" + str(j.name_image)
                        description = (j.description)
                        print "44444444444444444444444444444"
                        
            if request.method=="POST":
                form = ProfileForm(request.POST, request.FILES) 
                if form.is_valid():
                    # Valid form
                    name = form.cleaned_data['name']
                    lastname = form.cleaned_data['lastname']
                    form_description = form.cleaned_data['description']
                    image = form.cleaned_data['image']
                    
                    print "name " + name
                    print "lastname " + lastname
                    print "description " + form_description
                    
                    print "la siguiente linea es el nombre de la imagen que se ha introducido en el formulario"
                    print "image " + str(image)
                    
                    for u in tp:
                        if (str(u.username) == tt):
                            if not (name==""):
                                u.name = name
                            if not (lastname==""):
                                u.lastname = lastname
                            if not (form_description==""):
                                u.description = form_description
                            if not (str(image)=="None"):
                                print "es name_image no vacioooooooooooooooooooooooooooooooooooooooooo"
                                print u.name_image
                                
                                if (u.name_image=="") or (u.name_image==None):
                                    
                                    print "name_image es vacio en el usuario "
                                    # Saving the name of the file image.xxx
                                    u.name_image = str(image)
                                    u.image = image
                                else:
                                    im = "/tuerasmus/media/profiles/" + str(u.image)
                                    print "borramos esta imagen para guardar la nueva: " + im
                                    if not (im=="/tuerasmus/media/profiles/"):
                                        u.image.delete(im)
                                    print "esta es la nueva imagen: " + str(image)
                                    u.name_image = str(image)
                                    u.image = image
                                    print "ya tenemos guardada la imagen nueva"
                                    path_image = "profiles/" + u.name_image
                            else:
                                print "8888888888888888888888888888888888888888888888888888888888"
                                
                                path_image = "tuerasmus/" + genero + ".jpg"
                           
                                                                
                            print "recogi la info del form"
                            
                            u.save()
                            print "se han guardado los datos del perfil de usuario"
                            
                            us_image = UserProfile.objects.get(username=u.username)
                            path_image = "profiles/" + str(us_image.name_image)
                            description = us_image.description
                            form = ProfileForm()
                            
                            ctx = {'alertdone':True,  'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                            
                            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
                        else:
                            print "No existe el usuario"
                            ctx = {'alerterror':True, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                else:
                    # Invalid form
                    print "Formulario invalido!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!99999999"
                    form = ProfileForm()
                    ctx = {'alerterror':True, 'see_profile':False, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                    return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
                    
            else:
                # Method not POST
                form = ProfileForm()
                
                   
            # Return the template
            ctx = {'form':form, 'username': user, 'type_user': type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
                
        else:
            # User authenticated and user requested are differents
            print "EDIT_PROFILE: User authenticated and user requested are differents"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User no authenticated
        print "EDIT_PROFILE: usuario no logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

       
# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIREGISTER
# Register new university
def uniregister(request):

    if request.user.is_authenticated():
        

        user = request.user.username
        print "UNIREGISTER: el usuario esta logueado: " + user

        # User is professor or student
        # User has a profile image
        type_user=""
        path_image=""
        description=""
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()
        tp = UserProfile.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)
                

        # Variable 'unis' has all the universities
        unis = Universities.objects.all()
        unis = unis.extra(order_by=['country'])
        # Variable 'countries' has all the unis countries        
        countries = Countries.objects.all()
        countries = countries.extra(order_by=['country'])
        

        if request.method=="POST": 
            form = BasicForm(request.POST)       
            uni=""
            coun=""
            
            print "METODO POST"

            ### We get uni and scholarship
            unimenu = request.POST['uni_selected'] 
            unitext = request.POST['uni_written']

            print "UNI_SELECTED: " + unimenu
            print "UNI_WRITTEN: " + unitext

            
            menu = unimenu.split(" - ")
            if unitext=="":
                
                print menu[0]
                print menu[1]
                
                uni=menu[1]
            else:
                uni=unitext

            
            countext = request.POST['coun_written']
            
            print "Imprimo en la siguiente line el country del menu"
            
            print "COUN_WRITTEN: " + countext
            
            if countext=="":
                coun=menu[0]
            else:
                coun=countext
                
            scholarship = request.POST['scholarship']
                                   
            print "LA OPCION DE SCHOLARSHIP HA SIDO LA SIGUIENTE: " + scholarship
            es=""
            ms=""
            if scholarship=="erasmus":
                es=True
            if scholarship=="mundus":
                ms=True

            # Variables para guardar la universidad en la base de datos
            done=""
            # Variable para saber si ya está registrada o no la universidad
            warning=""

            ### No se ha seleccionado ninguna universidad
            if uni=="":
                print "uni es vacio, no se ha seleccionado ninguna universidad"
                error_msg="Debes introducir o seleccionar una universidad"
                ctx = {'alerterror':True, 'msg':True, 'error_msg': error_msg, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request))

            # Se ha seleccionado una universidad
            else:
                print "la universidad seleccionada es: " + uni

                try:
                    print "ESTOY EN EL TRY"
                    # Ya está la universidad registrada en la base de datos
                    u_saved = University.objects.get(uni=uni)
                    warning = True
                except University.DoesNotExist:
                    # No está la universidad registrada en la base de datos
                    u_saved = None
                    warning = False
                    #raise Http404
            
            ### User's university/s
            nu = UserProfile.objects.all()
            for i in nu:
                if (tt == str(i.username)):
                    print "N_UNIVERSITY: " + str(i.n_university)
                    n_university = i.n_university
                    print "4444444444444444444444444444444444444444444444444444444444444444444"

                    
                    # Aún no ha registrado
                    if n_university==0:
                        print "N_UNIVERSITY ES 00000000000000000000000"
                        print "PONEMOS DONE EN TRUE PARA QUE SE GUARDE LA UNIVERSIDAD"     
                        nusers = 0

                        # Es una universidad nueva
                        if not warning:
                            print "WARNING FALSEEEEEEEE: LA UNIVERSIDAD NO ESTÁ REGISTRADA"
                            un = University(uni=uni, username=request.user.username, scholarship=scholarship, country=coun)
                            un.save()       
                            print "un.save()"

                            # Incrementamos el número de usuarios de esa universidad
                            nusers += 1
                            print "nusers: " + str(nusers)
                            
                            unu = UsersUniversity(uni=un, nusers=nusers)
                            print "unu.nusers: " + str(unu.nusers) 
                            unu.save()
                            
                            try:
                                unu_user = UsersUniversity.objects.get(uni=un)
                                unu_user.useuni.add(i.username)
                                unu_user.save()
                            except UsersUniversity.DoesNotExist:
                                unu_user=""
                           
                            #unu_user.useuni.add(i.username)
                            #une = UniErasmus(uni=uni, scholarship=scholarship) 
                            #une.save()
                            #print "une.save()"
                            #i.university.add(uni)
                            #print "i.university.add(un.uni)"
                            
                            
                            #unu.save()
                            #print "unu.save()"


                            print "GUARDAMOS EN LAS BASES DE DATOS"


                            print "SE SUPONE QUE MI USUARIO AHORA TIENE SU UNIVERSIDAD GUARDADA"
                            try:
                                uu_saved = University.objects.get(uni=uni)
                            except University.DoesNotExist:
                                uu_saved=""
                            done = True
                        # Es una universidad antigua, ya estaba registrada
                        else:
                            done = False 
                            unu = University.objects.get(uni=uni)
                            uss = UsersUniversity.objects.all()
                            for j in uss:
                                if str(j.uni)==(unu.uni):
                                    print "antes de incrementar: j.nusers: " + str(j.nusers)
                                    j.nusers += 1
                                    j.useuni.add(i.username)
                                    print "despues de incrementar: j.nusers: " + str(j.nusers)
                                    j.save()

                        
                        if done:
                            # Done es True, con lo cual acabamos de registrarla
                            print "ESTOY EN ALERTAS DE DONEEEEEEEEEEEEE"
                            ctx = {'alertdone':True, 'uni_name':uni, 'uni_id':uu_saved.id, 'saved':True, 'countries':countries, 'unis':unis, 'username':user, 'type_user':type_user}
                        else:
                            # La universidad ya existe, y no la hemos registrado
                            print "ESTOY EN ALERTAS DE WARNINGGGGGGGGGGGGGGGGGGGGGGGG"
                            ctx = {'alertwarning':True, 'uni_name':u_saved, 'uni_id':u_saved.id, 'saved':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                         

                        print "Guardo en la base de datos el valor de uni1"
                        i.uni1 = uni
                        i.save()
                           
                        
                        print "sin incrementarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr: " + str(n_university)
                        i.n_university += 1
                        if es:
                            i.sserasmus=scholarship
                        if ms:
                            i.ssmundus=scholarship
                        print "incrementadoooooooooooooooo: " + str(i.n_university)
                        i.save()
                        print "HEMOS INCREMENTADO LA VARIABLE N_UNIVERSITY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                         

                    # Tiene una universidad registrada
                    if n_university==1:
                        print "N_UNIVERSITY ES 11111111111111111111111"

                        # Comprobamos si la universidad que tiene es erasmus o mundus
                        # variable i es del for que se recorre "nu" que contiene todos los objetos de UserProfile
                        save=""
                        print "SSERASMUS: " + str(i.sserasmus)
                        print "SSMUNDUS: " + str(i.ssmundus)
                        if es:
                            if (i.sserasmus=="") or (i.sserasmus==None):
                                i.sserasmus=scholarship
                                i.save()
                                print "SSERAMUS ESTÁ VACÍOOOOOOOOOOOOOOOOOOOOOOOOOO    GUARDAMOS EN LAS BASES DE DATOS"
                                save=True
                            else:
                                print "YA TIENES LA UNIVERSIDAD ERASMUS REGISTRADA!!!!!!!!!!!!!!!!!!"
                                ctx = {'info':True, 'alertaerasmus':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                                return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request))
                        if ms:
                            if (i.ssmundus=="") or (i.ssmundus==None):
                                i.ssmundus=scholarship
                                i.save()
                                print "SSMUNDUS ESTÁ VACÍOOOOOOOOOOOO GUARDAMOS EN LAS BASES DE DATOS"
                                save=True
                            else:
                                print "YA TIENES LA UNIVERSIDAD MUNDUS REGISTRADA!!!!!!!!!!!!!!!!!!"
                                ctx = {'info':True, 'alertamundus':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                                return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request))


                        nusers = 0
                        # Es una universidad nueva
                        if not warning:
                            print "WARNING FALSEEEEEEEE: LA UNIVERSIDAD NO ESTÁ REGISTRADA"
                            un = University(uni=uni, username=request.user.username, scholarship=scholarship, country=coun)
                            un.save()
                            print "un.save()"
                            #une = UniErasmus(uni=uni, scholarship=scholarship) 
                            #une.save()
                            #print "une.save()"
                            #i.university.add(uni)
                            #print "i.university.add(un.uni)"


                            # Incrementamos el número de usuarios de esa universidad
                            nusers += 1
                            print "nusers: " + str(nusers)
                            unu = UsersUniversity(uni=un, nusers=nusers)
                            print "unu.nusers: " + str(unu.nusers) 
                            unu.save()
                            print "unu.save()"
                            # Incrementamos el número de usuarios de esa universidad
                            nusers += 1
                            print "nusers: " + str(nusers)

                            
                            try:
                                unu_user = UsersUniversity.objects.get(uni=un)
                                unu_user.useuni.add(i.username)
                                unu_user.save()
                            except UsersUniversity.DoesNotExist:
                                unu_user=""

                            print "GUARDAMOS EN LAS BASES DE DATOS"


                            print "SE SUPONE QUE MI USUARIO AHORA TIENE SU UNIVERSIDAD GUARDADA"
                            try:
                                uu_saved = University.objects.get(uni=uni)
                            except University.DoesNotExist:
                                uu_saved=""
                            done = True

                        # Es una universidad antigua, ya estaba registrada
                        else:
                            done = False 
                            unu = University.objects.get(uni=uni)
                            uss = UsersUniversity.objects.all()
                            for j in uss:
                                if str(j.uni)==(unu.uni):
                                    print "antes de incrementar: j.nusers: " + str(j.nusers)
                                    j.nusers += 1
                                    print "despues de incrementar: j.nusers: " + str(j.nusers)
                                    j.useuni.add(i.username)
                                    j.save()

                          

                        
                        if done:
                            # Done es True, con lo cual acabamos de registrarla
                            print "ESTOY EN ALERTAS DE DONEEEEEEEEEEEEE"
                            ctx = {'alertdone':True, 'uni_name':uni, 'uni_id':uu_saved.id, 'saved':True, 'countries':countries, 'unis':unis, 'username':user, 'type_user':type_user}
                        else:
                            # La universidad ya existe, y no la hemos registrado
                            print "ESTOY EN ALERTAS DE WARNINGGGGGGGGGGGGGGGGGGGGGGGG"
                            ctx = {'alertwarning':True, 'uni_name':u_saved, 'uni_id':u_saved.id, 'saved':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                       

                             
                        print "Guardo en la base de datos el valor de uni2"
                        i.uni2 = uni
                        i.save()
   
                        print "sin incrementarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr: " + str(n_university)
                        
                        if es and save:
                            i.sserasmus=scholarship
                            i.n_university += 1
                        if ms and save:
                            i.ssmundus=scholarship
                            i.n_university += 1
                        print "incrementadoooooooooooooooo: " + str(i.n_university)
                        i.save()
                        print "HEMOS INCREMENTADO LA VARIABLE N_UNIVERSITY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                         

                    # El usuario no puede registrar más universidades
                    if n_university>=2: 
                        print "N_UNIVERSITY ES 2222222222222222 O DISTINTO Y NO PODEMOS REGISTRAR NI SE GUARDAN UNIVERSIDADES"
                        # botuni es para mostrar el boton para ir a las universidades
                        ctx = {'info':True, 'alertamax':True, 'botuni':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}

                    return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request)) 

        else:
            print "METODO GET"
            ctx = {'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
            return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request))

        ctx = {'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
        return render_to_response('tuerasmus/uniregister.html', ctx, context_instance=RequestContext(request))

    else:
        # User no authenticated
        print "UNIREGISTER: el usuario no esta logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIVERSITIES
# All universities in
def universities(request):

    ctx={}
    ctx.update(csrf(request))

    if request.user.is_authenticated():
        print "UNIVERSITIES: el usuario esta logueado " + request.user.username
        
        ### User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()

        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # TENGO QUE ENCONTRAR DONDE METER ESTAS LINEAS PARA EL POST O GET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print "tt:" + str(tt)


        uniuser=""
        if request.method=="GET":              
            print "METODO GET"

            ### Show all universities in TuErasmus
            uniserasmus=""
            unismundus=""
            uems_msg=""

            print "UNISERASMUS ANTES DEL TRY: " + str(uniserasmus)
            print "UNISMUNDUS ANTES DEL TRY:" + str(unismundus)

        
            print "el numero de objectos en ue es: " + str(University.objects.all().filter(scholarship="erasmus").count())
            if (University.objects.all().filter(scholarship="erasmus").count())==0:
                uniserasmus=False
            else:
                uniserasmus=True
       
            print "el numero de objectos en um es: " + str(University.objects.all().filter(scholarship="mundus").count())
            if (University.objects.all().filter(scholarship="mundus").count())==0:
                unismundus=False
            else:
                unismundus=True   

            print "UNISERASMUS ES: " + str(uniserasmus)
            print "UNISMUNDUS ES: " + str(unismundus) 
            print "SE SUPONE QUE YA TENGO TODAS LAS UNIVERSIDADES DE ERASMUS!!!!!!!!!!!!!!!!!!!!!!"

            try:
                uems = University.objects.all()
                uems_ = True
            except University.DoesNotExist:
                uems_msg = "No hay universidades registradas"
                uems_ = False

            uall = University.objects.all
            
            # Porcentajes de la web:
            
            nusuarios = Users.objects.all().count()
            porcentaje_usuarios = nusuarios/float(50)
            nalumnos = Users.objects.all().filter(type_user="alumno").count()
            porcentaje_alumnos = nalumnos/float(nusuarios)
            nprofesores = Users.objects.all().filter(type_user="profesor").count()
            porcentaje_profesores = nprofesores/float(nusuarios)
            nchicos = Users.objects.all().filter(genero="male").count()
            porcentaje_chicos = nchicos/float(nusuarios)
            nchicas = Users.objects.all().filter(genero="female").count()
            porcentaje_chicas = nchicas/float(nusuarios)
            
            print "voy a imprimir los tres porcentajes que acabo de calcular"
            print nusuarios
            print str(porcentaje_usuarios)
            print nalumnos
            print str(porcentaje_alumnos)
            print nprofesores
            print str(porcentaje_profesores)
            print nchicos
            print str(porcentaje_chicos)
            print nchicas
            print str(porcentaje_chicas)            
            
            if uniserasmus and unismundus:
                ctx = {'curiosities':True, 'porcentaje_usuarios':porcentaje_usuarios, 'porcentaje_alumnos':porcentaje_alumnos, 'porcentaje_profesores':porcentaje_profesores, 'porcentaje_chicos':porcentaje_chicos, 'porcentaje_chicas':porcentaje_chicas, 'uall':uall, 'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}
 
            if uniserasmus and not unismundus:
                ctx = {'curiosities':True, 'porcentaje_usuarios':porcentaje_usuarios, 'porcentaje_alumnos':porcentaje_alumnos, 'porcentaje_profesores':porcentaje_profesores, 'porcentaje_chicos':porcentaje_chicos, 'porcentaje_chicas':porcentaje_chicas, 'uall':uall, 'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}
 
            if unismundus and not uniserasmus:
                ctx = {'curiosities':True, 'porcentaje_usuarios':porcentaje_usuarios, 'porcentaje_alumnos':porcentaje_alumnos, 'porcentaje_profesores':porcentaje_profesores, 'porcentaje_chicos':porcentaje_chicos, 'porcentaje_chicas':porcentaje_chicas, 'uall':uall, 'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user} 
 
            if not unismundus and not uniserasmus:
                ctx = {'curiosities':True, 'porcentaje_usuarios':porcentaje_usuarios, 'porcentaje_alumnos':porcentaje_alumnos, 'porcentaje_profesores':porcentaje_profesores, 'porcentaje_chicos':porcentaje_chicos, 'porcentaje_chicas':porcentaje_chicas, 'uall':uall, 'unisempty':True, 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}

            return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))  

        if request.method=="POST":              
            print "METODO POST"
            
            # Cuando elige una universidad del menú desplegable redirigir al perfil de esa universidad
            uniems = request.POST['uniems_selected']
            
            print "UNIEMS: " + uniems

            # Necesito obtener el id de esa universidad para la url de la universidaden concreto
            if not (uniems==""):
                print "HEMOS ELEGIDO UNA UNIVERSIDAD ERASMUS"
                uniems_id = University.objects.get(uni=uniems)
                ur = '/tuerasmus/university/' + str(uniems_id.id)
                return HttpResponseRedirect(ur)

                    
    else:
        # User no authenticated
        print "UNIVERSITIES: el usuario no esta logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIVERSITY
# Edit information about universities
def university(request, uni_name):
    if request.user.is_authenticated():
        print "UNIVERSITY: usuario logueado: " + request.user.username
        print "me han pasado UNI_NAME: " + uni_name


        # User is student or professor
        type_user=""
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)


        
        
            
   
        # In University we can get the name of the university
        uniobj=""
        uni_image=""
        nchicos = 0
        nchicas = 0
        nprofesores = 0
        nalumnos = 0
        
        try:
            uniname = University.objects.get(id=uni_name[0])
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            
            # Percents:
            print "444444444444444444444444444444444444444444444"
            nusuarios = Users.objects.all().count()
            print "5555555555555555555555555555555555555555555555555"
            try:
                uniname_users = UsersUniversity.objects.get(uni=uniname)
                # nuniname_user is the number of the students in this university
                nuniname_users = uniname_users.nusers
                print "vamos a imprimir el numero de usuarios de esa universidad"
                print nuniname_users
                users_list = uniname_users.useuni.all()
                for i in users_list:
                    print i.username
                    u = User.objects.get(username=i.username)
                    try:
                        userinfo = Users.objects.get(username=u)
                        if (userinfo.genero=="male"):
                            nchicos+=1
                        else:
                            nchicas+=1
                            
                        if (userinfo.type_user=="alumno"):
                            nalumnos+=1
                        else:
                            nprofesores+=1
                    except UserProfile.DoesNotExist:
                        print "No hay datos recogidos"                        
                
            except UsersUniversity.DoesNotExist:
                nuniname_users = 0 

            print "imprimo los datos recogidos despues de recorrer la base de datos"
            print nusuarios
            print nchicos
            print nchicas
            print nalumnos
            print nprofesores
            porcentaje_usuarios = nuniname_users/float(nusuarios)
            #nalumnos = Users.objects.all().filter(type_user="alumno").count()
            porcentaje_alumnos = nalumnos/float(nuniname_users)
            #nprofesores = Users.objects.all().filter(type_user="profesor").count()
            porcentaje_profesores = nprofesores/float(nuniname_users)
            #nchicos = Users.objects.all().filter(genero="male").count()
            porcentaje_chicos = nchicos/float(nuniname_users)
            #nchicas = Users.objects.all().filter(genero="female").count()
            porcentaje_chicas = nchicas/float(nuniname_users)
            
            #print "voy a imprimir los tres porcentajes que acabo de calcular"
            #print nusuarios
            print str(porcentaje_usuarios)
            #print nalumnos
            print str(porcentaje_alumnos)
            #print nprofesores
            print str(porcentaje_profesores)
            #print nchicos
            print str(porcentaje_chicos)
            #print nchicas
            print str(porcentaje_chicas)



            try:
                uniobj = InfoBasic.objects.get(uni=uniname)
                latitud = uniobj.latitud
                longitud = uniobj.longitud
                
                if (str(uniobj.name_image)=="") or (str(uniobj.name_image)=="None"):
                    path_image="tuerasmus/universidad.png"
                else:
                    path_image="universities/" + str(uniobj.name_image)
                print "imprimo el nombre de la imagen"
                print path_image
                print "vamos a imprimir los valores de latitud y longitud"
                print latitud
                print longitud
                
                
            except InfoBasic.DoesNotExist:
                path_image="tuerasmus/universidad.png"
                print "No se encontró el nombre de la universidad en la tabla InfoBasic"
                ctx = {'no_info':True, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                # Return the template
                return render_to_response('university/geouniversity.html', ctx, context_instance=RequestContext(request))
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id" 
            ctx = {'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
            return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))


        if request.method=="POST":
        
            print "se ha hecho un POST"
            
            newcomment = request.POST['newcomment']
            commentid = request.POST['commentid']
            
            # Se pueden borrar estas líneas #
            #print "vamos a imprimir el comentario nuevo que se ha hecho"
            #print newcomment
            #print "vamos a imprimir el id del comentario nuevo que se ha hecho"
            #print commentid
            #print "imprimo el id de la universidad que estoy usando ahora mismo"
            #print uniobj.id
            ###############################
            
            try: 
                newinfo = InfoBasic.objects.get(id=commentid)
                #print newinfo.description
                newinfo.description = newcomment
                newinfo.save()
                
                uniobj = InfoBasic.objects.get(uni=uniname)
            except InfoBasic.DoesNotExist:
                print "No hay informacionnnn con ese id"
                #return HttpResponseRedirect('/tuerasmus/')

            
        #print "Voy a imprimir el valor de la variable uniname"
        #print uniname
        ctx = {'porcentaje_usuarios':porcentaje_usuarios, 'porcentaje_alumnos':porcentaje_alumnos, 'porcentaje_profesores':porcentaje_profesores, 'porcentaje_chicos':porcentaje_chicos, 'porcentaje_chicas':porcentaje_chicas, 'uniobj':uniobj, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        # Return the template
        return render_to_response('university/geouniversity.html', ctx, context_instance=RequestContext(request))
    else:
        print "UNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNI INFORMATION
# To see the info of the university
def uninfo(request, uni_name, type_info):

    # User authenticated
    if request.user.is_authenticated():
        print "UNINFO: User authenticated " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        print "uni_name: " + str(uni_name)
        print "type_info: " + str(type_info)
        
        # With uni id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            #uni = uniname.uni
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus/" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur) 
            
            
        uni=""  
        path_image=""
        try:
            
            uni = InfoBasic.objects.get(uni=uniname)
            print str(uni.image)
            print uni.latitud
            print uni.longitud
            path_image = str(uni.image) 
            print path_image
            no_info = False
            
        except InfoBasic.DoesNotExist:
            # uniname.uni: uni's name
            # uni_name: id_uni
            # uni.image: url's image of uni
            path_image = "tuerasmus/universidad.png"
            no_info = True
            
            
                      
        
        # MÉTODO GET
        if request.method=="GET":
        
            
            list_empty=""
                           
            tmp = 'university/geouniversity.html'
            if type_info=="basic":
                print "muestro la info basica"
                info="basic"
                info_list = InfoGeneral.objects.filter(uni=uniname.uni)
                tmp = 'university/uni_info.html'

            elif type_info=="doc":
                print "muestro la info doc"
                info="doc"
                info_list = InfoGeneral.objects.filter(uni=uniname.uni)
                print "Acabamos de obtener nuestra info_list"
                print InfoGeneral.objects.all().count()
                tmp = 'university/uni_info.html'
                 
            elif type_info=="hotel":
                      
                print "muestro la info hotel"
                info="hotel"
                info_list = Place.objects.filter(uni=uniname.uni)
                matriz = []
                print "voy a imprimir el supuesto contenido de info_list"
                print info_list
                
                if len(info_list)==0:
                    print "INFO_LIST ESTA VACIAAAAAAAAAAAAAAAAAAAAAA NO HAY RESIDENCIASSSSSSSSSS"
                    list_empty = True
                    print list_empty
                else:
                    list_empty = False

                    #k=0
                    matriz = []
                    for i in info_list:
                        
                        
                        s=i.name
                        #s.encode("iso-8859-15")
                        
                        matriz.append([s, str(i.latitud), str(i.longitud)])

                            
                        #for j in range(numero_columnas):
                        #    print "printemaos j"
                        #    print j
                        #    if j==0:
                        #        matriz[k].append(i.name)
                        #    elif j==1:
                        #        matriz[k].append(str(i.latitud))
                        #    elif j==2:
                        #        matriz[k].append(str(i.longitud))
                
                        #+=1  
                    
                    print "························"
                    print matriz[0]   
                    print matriz[1]
                    print len(matriz)

                    ctx = {'mispuntos':matriz, 'longitud':len(matriz), 'list_empty': list_empty, 'uni':uni, 'info':info, 'info_list':info_list, 'path_image':path_image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/georesidence.html', ctx, context_instance=RequestContext(request))

            elif type_info=="subjects":
                print "muestro la info subjects"
                info="subjects"
                info_obj = InfoGeneral.objects.filter(uni=uniname.uni)
                info_list = Subjects.objects.filter(uni=uniname.uni)
                
                #info_list=Subjects.objects.filter(uni=uniname.uni)
                tmp = 'university/uni_info.html'    

            elif type_info=="city":
                print "muestro la info city"
                info="city"
                #info_city = InfoBasic.objects.get(uni=uniname)
                #print "88888888888888888888888888888888888888888la ciudad que quiero mostrar de la universidad es: " + str(info_city.city)
                info_list=City.objects.filter(uni=uniname)
                for i in info_list:
                    print i.cityname
                tmp = 'university/uni_info.html'

            elif type_info=="others":
                print "muestro la info others"
                info="others"
                info_list = Comment.objects.filter(tag=uniname.uni)
                tmp = 'university/uni_info.html'
                
            ctx = {'uni':uni, 'info':info, 'no_info': no_info, 'info_list':info_list, 'path_image':path_image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                


            # Return the template
            return render_to_response(tmp, ctx, context_instance=RequestContext(request))


                   

        elif request.method=="POST":
            newcomment=""
            rec_qualification=""
            rec_specialty=""
            rec_teachingequipment=""
            rec_library=""
            rec_lab=""
            rec_computerequipment=""
            rec_others=""
            rec_dinningroom=""
            rec_cafeteria=""
            rec_sportactivities=""
            rec_asociation=""
            rec_languagecourse=""
            rec_schoolyear=""
            rec_vacations=""
            rec_compteleco=""
            rec_teachers=""
            rec_teaching=""
            rec_studies=""
            rec_unidoc=""
            rec_residencelicence=""
            rec_getresidence=""
            rec_economicaid=""
            rec_bankaccount=""
            rec_costume=""
            rec_meetings=""
            rec_offices=""
            rec_prices=""
            rec_uniarea=""
            rec_studentlife=""
            rec_turism=""
            rec_party=""
            rec_culture=""
            rec_crime=""
            rec_shopping=""
            rec_erasmuslife=""
            rec_more=""
            rec_subname=""
            rec_credits=""
            rec_subnameout1=""
            rec_subnameout2=""
            rec_subnameout3=""
            rec_works=""
            rec_practices=""
            rec_difficult=""
            
            print "se ha hecho un POST"
            print "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
            #category = request.POST['category']
            commentid = request.POST['commentid']
            info = request.POST['info']            
            save = request.POST['button']
            
            if save=="qualification":
                new_qualification = request.POST['new_qualification']
                newcomment = new_qualification
                rec_qualification = True
            elif save=="specialty":
                new_specialty = request.POST['new_specialty']
                newcomment = new_specialty
                rec_specialty = True
            elif save=="teachingequipment":
                new_teachingequipment = request.POST['new_teachingequipment']
                newcomment = new_teachingequipment
                rec_teachingequipment = True
            elif save=="library":
                new_library = request.POST['new_library']
                newcomment = new_library
                rec_library = True
            elif save=="lab":
                new_lab = request.POST['new_lab']
                newcomment = new_lab
                rec_lab = True
            elif save=="computerequipment":
                new_computerequipment = request.POST['new_computerequipment']
                newcomment = new_computerequipment
                rec_computerequipment = True
            elif save=="others":
                new_others = request.POST['new_others']
                newcomment = new_others
                rec_others = True
            elif save=="dinningroom":
                new_dinningroom = request.POST['new_dinningroom']
                newcomment = new_dinningroom
                rec_dinningroom = True
            elif save=="cafeteria":
                new_cafeteria = request.POST['new_cafeteria']
                newcomment = new_cafeteria
                rec_cafeteria = True
            elif save=="sportactivities":
                new_sportactivities = request.POST['new_sportactivities']
                newcomment = new_sportactivities
                rec_sportactivities = True
            elif save=="asociation":
                new_asociation = request.POST['new_asociation']
                newcomment = new_asociation
                rec_asociation = True
            elif save=="languagecourse":
                new_languagecourse = request.POST['new_languagecourse']
                newcomment = new_languagecourse
                rec_languagecourse = True
            elif save=="schoolyear":
                new_schoolyear = request.POST['new_schoolyear']
                newcomment = new_schoolyear
                rec_schoolyear = True
            elif save=="vacations":
                new_vacations = request.POST['new_vacations']
                newcomment = new_vacations
                rec_vacations = True
            elif save=="compteleco":
                new_compteleco = request.POST['new_compteleco']
                newcomment = new_compteleco
                rec_compteleco = True
            elif save=="teachers":
                new_teachers = request.POST['new_teachers']
                newcomment = new_teachers
                rec_teachers = True
            elif save=="teaching":
                new_teaching = request.POST['new_teaching']
                newcomment = new_teaching
                rec_teaching = True
            elif save=="studies":
                new_studies = request.POST['new_studies']
                newcomment = new_studies
                rec_studies = True
            elif save=="unidoc":
                new_unidoc = request.POST['new_unidoc']
                newcomment = new_unidoc
                rec_unidoc = True   
            elif save=="residencelicence":
                new_residencelicence = request.POST['new_residencelicence']
                newcomment = new_residencelicence
                rec_residencelicence = True 
            elif save=="getresidence":
                new_getresidence = request.POST['new_getresidence']
                newcomment = new_getresidence
                rec_getresidence = True 
            elif save=="economicaid":
                new_economicaid = request.POST['new_economicaid']
                newcomment = new_economicaid
                rec_economicaid = True 
            elif save=="bankaccount":
                new_bankaccount = request.POST['new_bankaccount']
                newcomment = new_bankaccount
                rec_bankaccount = True 
            elif save=="costume":
                new_costume = request.POST['new_costume']
                newcomment = new_costume
                rec_costume = True 
            elif save=="meetings":
                new_meetings = request.POST['new_meetings']
                newcomment = new_meetings
                rec_meetings = True 
            elif save=="offices":
                new_offices = request.POST['new_offices']
                newcomment = new_offices
                rec_offices = True  
            elif save=="prices":
                new_prices = request.POST['new_prices']
                newcomment = new_prices
                rec_prices = True 
            elif save=="uniarea":
                new_uniarea = request.POST['new_uniarea']
                newcomment = new_uniarea
                rec_uniarea = True
            elif save=="studentlife":
                new_studentlife = request.POST['new_studentlife']
                newcomment = new_studentlife
                rec_studentlife = True
            elif save=="turism":
                new_turism = request.POST['new_turism']
                newcomment = new_turism
                rec_turism = True
            elif save=="party":
                new_party = request.POST['new_party']
                newcomment = new_party
                rec_party = True
            elif save=="culture":
                new_culture = request.POST['new_culture']
                newcomment = new_culture
                rec_culture = True
            elif save=="crime":
                new_crime = request.POST['new_crime']
                newcomment = new_crime
                rec_crime = True
            elif save=="shopping":
                new_shopping = request.POST['new_shopping']
                newcomment = new_shopping
                rec_shopping = True
            elif save=="erasmuslife":
                new_erasmuslife = request.POST['new_erasmuslife']
                newcomment = new_erasmuslife
                rec_erasmuslife = True
            elif save=="more":
                new_more = request.POST['new_more']
                newcomment = new_more
                rec_more = True
            elif save=="subname":
                new_subname = request.POST['new_subname']
                newcomment = new_subname
                rec_subname = True
            elif save=="credits":
                new_credits = request.POST['new_credits']
                newcomment = new_credits
                rec_credits = True
            elif save=="subnameout1":
                new_subnameout1 = request.POST['new_subnameout1']
                newcomment = new_subnameout1
                rec_subnameout1 = True
            elif save=="subnameout2":
                new_subnameout2 = request.POST['new_subnameout2']
                newcomment = new_subnameout2
                rec_subnameout2 = True
            elif save=="subnameout3":
                new_subnameout3 = request.POST['new_subnameout3']
                newcomment = new_subnameout3
                rec_subnameout3 = True
            elif save=="works":
                new_works = request.POST['new_works']
                newcomment = new_works
                rec_works = True
            elif save=="practices":
                new_practices = request.POST['new_practices']
                newcomment = new_practices
                rec_practices = True
            elif save=="difficult":
                new_difficult = request.POST['new_difficult']
                newcomment = new_difficult
                rec_difficult = True
                          
                 

                
            print "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
            #print category
            print commentid
            print info
            print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
            print newcomment
            #print new_teachingequipment
            #print new_library
            #print new_lab
            print  "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
            

            
            print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            print "imprimo el id de la universidad que estoy usando ahora mismo"
            print uni.id
            
            if (info=="basic") or (info=="doc"):
                try: 
                    newinfo = InfoGeneral.objects.get(id=commentid)
                    #search_fields = (category)
                    print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"
                    print "Se supone que ha buscado"
                    if rec_qualification:
                        newinfo.qualification = newcomment
                    elif rec_specialty:
                        newinfo.specialty = newcomment
                    elif rec_teachingequipment:
                        newinfo.teachingequipment = newcomment
                    elif rec_library:
                        newinfo.library = newcomment
                    elif rec_lab:
                        newinfo.lab = newcomment
                    elif rec_computerequipment:
                        newinfo.computerequipment = newcomment
                    elif rec_others:
                        newinfo.others = newcomment
                    elif rec_dinningroom:
                        newinfo.dinningroom = newcomment
                    elif rec_cafeteria:
                        newinfo.cafeteria = newcomment
                    elif rec_sportactivities:
                        newinfo.sportactivities = newcomment
                    elif rec_asociation:
                        newinfo.asociation = newcomment
                    elif rec_languagecourse:
                        newinfo.languagecourse = newcomment
                    elif rec_schoolyear:
                        newinfo.schoolyear = newcomment
                    elif rec_vacations:
                        newinfo.vacations = newcomment
                    elif rec_compteleco:
                        newinfo.compteleco = newcomment
                    elif rec_teachers:
                        newinfo.teachers = newcomment
                    elif rec_teaching:
                        newinfo.teaching = newcomment
                    elif rec_studies:
                        newinfo.studies = newcomment
                    elif rec_unidoc:
                        newinfo.unidoc = newcomment
                    elif rec_residencelicence:
                        newinfo.residencelicence = newcomment
                    elif rec_getresidence:
                        newinfo.getresidence = newcomment
                    elif rec_economicaid:
                        newinfo.economicaid = newcomment
                    elif rec_bankaccount:
                        newinfo.bankaccount = newcomment
                    elif rec_costume:
                        newinfo.costume = newcomment
                    elif rec_meetings:
                        newinfo.meetings = newcomment
                    elif rec_offices:
                        newinfo.offices = newcomment
                   
                    newinfo.save()
                    print "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"

                except InfoGeneral.DoesNotExist:
                    print "No hay informacionnnn con ese id"
            elif (info=="hotel"):
                try: 
                    newinfo = Place.objects.get(id=commentid)

                except Place.DoesNotExist:
                    print "No hay informacionnnn con ese id"
            
            elif (info=="subjects"):
                try: 
                    newinfo = Subjects.objects.get(id=commentid)

                    if rec_subname:
                        newinfo.subname = newcomment
                    elif rec_credits:
                        newinfo.credits = newcomment
                    elif rec_subnameout1:
                        newinfo.subnameout1 = newcomment
                    elif rec_subnameout2:
                        newinfo.subnameout2 = newcomment
                    elif rec_subnameout3:
                        newinfo.subnameout3 = newcomment
                    elif rec_works:
                        newinfo.works = newcomment
                    elif rec_practices:
                        newinfo.practices = newcomment
                    elif rec_difficult:
                        newinfo.difficult = newcomment
                    
                    newinfo.save()
                except Subjects.DoesNotExist:
                    print "No hay informacionnnn con ese id"
            
            elif (info=="city"):
                try: 
                    newinfo = City.objects.get(id=commentid)

                    if rec_prices:
                        newinfo.prices = newcomment
                    elif rec_uniarea:
                        newinfo.uniarea = newcomment
                    elif rec_studentlife:
                        newinfo.studentlife = newcomment
                    elif rec_turism:
                        newinfo.turism = newcomment
                    elif rec_party:
                        newinfo.party = newcomment
                    elif rec_culture:
                        newinfo.culture = newcomment
                    elif rec_crime:
                        newinfo.crime = newcomment
                    elif rec_shopping:
                        newinfo.shopping = newcomment
                    elif rec_erasmuslife:
                        newinfo.erasmuslife = newcomment
                    elif rec_more:
                        newinfo.more = newcomment
                    
                    newinfo.save()
                except City.DoesNotExist:
                    print "No hay informacionnnn con ese id"
                    
            elif (info=="others"):
                try: 
                    newinfo = Comment.objects.get(id=commentid)

                    if rec_text:
                        newinfo.text = newcomment
                    newinfo.save()
                    
                except Comment.DoesNotExist:
                    print "No hay informacionnnn con ese id"
            
            
            ur = "/tuerasmus/university/" + str(uni.id) + "/" + info
            return HttpResponseRedirect(ur)
            
            #ctx = {'uni':uni, 'no_info': no_info, 'path_image':path_image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
        
            # Return the template
            #return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))

    else:
        # User no authenticated
        print "UNINFO: el usuario no esta logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: MYUNIVERSITY
# User university/s
def myuniversity(request, user):


    if request.user.is_authenticated():
        if (request.user.username==user):

            print "MYUNIVERSITY: el usuario esta logueado " +  user

            # User is professor or student
            # User has a profile image
            type_user=""
            path_image=""
            description=""
            t = User.objects.get(username=user)
            tt = t.username
            tu = Users.objects.all()
            tp = UserProfile.objects.all()
            for i in tu:
                if (tt == str(i.username)):
                    type_user = str(i.type_user)
                    genero = str(i.genero)
            for j in tp:
                print "nombre de la imagen 7777777777777777777777777: " + str(j.name_image) + str(j.username)
                print "description 7777777777777777777777777: " + (j.description) + str(j.username)
                if (tt == str(j.username)):
                    if ((str(j.name_image)=="") or (str(j.name_image)=="None")) and ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Estudiante de la ETSIT"
                        
                    elif ((str(j.name_image)=="") or (str(j.name_image)=="None")) and not ((j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = (j.description)
                        
                    elif ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Estudiante de la ETSIT"
                    elif not ((j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = (j.description)
                        
                print "voy a imprimir path_image 7777777777777777777777777777777" + str(j.username)
                print path_image     
                       
            print "Vamos a hacer un try para ver como conseguimos los datos que queremos de user"
            try:
                reco1=""
                reco2=""
                u = User.objects.get(username=user)
                record = UserProfile.objects.get(username=u)
                

                try:
                    rec1 = University.objects.get(uni=record.uni1)
                
                    print "rec1.id: " + str(rec1.id)

                    print record.uni1

                    #if ("-" in record.uni1):
                    #    record.uni1=record.uni1.split(" - ")[1]
                    #else:
                    #    record.uni1=record.uni1

                    #print record.uni1
                    reco1 = True

                        
                except University.DoesNotExist:
                    pass
                   

                try:
                    rec2 = University.objects.get(uni=record.uni2)
                    print "rec2.id: " + str(rec2.id)

                    print record.uni2
                    
                    #if ("-" in record.uni2):
                    #    record.uni2=record.uni2.split(" - ")[1]
                    #else:
                    #    record.uni2=record.uni2

                    #print record.uni2
                    reco2 = True

                except University.DoesNotExist:
                    pass

                if reco1 and not reco2:                
                    ctx = {'reco1':reco1, 'uni1':record.uni1, 'uni1id':rec1.id, 'type_user':type_user, 'genero':genero, 'username': request.user.username, 'path_image':path_image, 'description':description}
                elif reco2 and not reco1:
                    ctx = {'reco2':reco2, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'genero':genero, 'username': request.user.username, 'path_image':path_image, 'description':description}
                elif reco1 and reco2:
                    print "reco1 y reco2 son True!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    ctx = {'reco1':reco1, 'reco2':reco2, 'uni1':record.uni1, 'uni1id':rec1.id, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'genero':genero, 'username': request.user.username, 'path_image':path_image, 'description':description}
                else:
                    ctx = {'type_user':type_user, 'genero':genero, 'username': request.user.username, 'path_image':path_image, 'description':description}
                
                    

            except UserProfile.DoesNotExist:
                print "universidades uni1 y uni2 están vacías!!!!!!!!1"
                ctx = {'type_user':type_user, 'genero':genero, 'username': request.user.username, 'path_image':path_image, 'description':description}    


            return render_to_response('tuerasmus/myuniversity.html', ctx, context_instance=RequestContext(request))
        else:
            # User no authenticated
            print "MYUNIVERSITY: Usuario logueado distinto del usuario solicitado"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User no authenticated
        print "MYUNIVERSITY: el usuario no esta logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIEDIT
# Edit the information of universities
def uniedit(request, uni_name):
    if request.user.is_authenticated():
        print "UNIEDIT: usuario logueado " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        print "uni_name: " + str(uni_name)

        # With uni_name.id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)  
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus/" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)
        
        url = "/tuerasmus/uniedit/" + uni_name + "/basic"
        return HttpResponseRedirect(url)

    else:
        print "UNIEDIT: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIEDITFORM
# To complete all the forms of the uni
def unieditform(request, uni_name, type_form):
    if request.user.is_authenticated():      
        print "UNIEDITFORM: usuario logueado: " + request.user.username
        ctx = {}
        tit=""
        tit1=""
        tit2=""
        tit3=""
        tit4=""
        tit5=""
        coor=""
        form=""
        form1=""
        form2=""
        form3=""
        form4=""
        form5=""
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        print "uni_name: " + str(uni_name)
        print "type_form: " + str(type_form)
        

        # With uni_id we can get the name
        path_image=""
        data_infobasic=""
        try:
            # he cambiado la variable un_obj por uniname
            uniname = University.objects.get(id=uni_name)
            print uniname.uni
            try:
                # uni_data es el objeto que corresponde con el item de esa universidad en la tabla InfoBasic
                uni_data = InfoBasic.objects.get(uni=uniname)
                data_infobasic = True
                print "Tiene info en InfoBAsic la universidad"
                print "imprimimos el nombre de la imagen"
                print str(uni_data.image)
                print uni_data.name_image

                if (uni_data.name_image=="") or (uni_data.name_image==None):
                    print "name_image es vacio en el usuario "
                    path_image = "tuerasmus/universidad.png"
                else:
                    path_image = "universities/" + str(uni_data.name_image)
                    print "name_image no es vacio asi que imprimimos el nombre de la imagen que tenemos actualmente en nuestra universidad"
                    print path_image
            except InfoBasic.DoesNotExist:
                print "EXCEPT del try de UNIEDIT FORM!!!!!!!!!!!!!!!!: no se encontro ningun item de l auniversidad en InfoBAisc"
                data_infobasic = False
                path_image = "tuerasmus/universidad.png"
                
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus/" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)
            
        
        # MÉTODO POST
        if request.method=="POST":
            alertdone=""
            alerterror="" 
            # un_obj es el objeto de la universidad(uni, username, scholarship y country)
            # un_obj = University.objects.get(uni=uniname.uni)
             
             
            # ya no uso el OBJETO UN_OBJ, AHORA ES UNINAME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            
            
            
            ###################### BASIC FORM ######################
            if type_form=="basic":
                tit = "Datos de la universidad"
                form = BasicForm(request.POST, request.FILES)
                
                if form.is_valid(): 
                    # Valid form
                    address = form.cleaned_data['address']
                    postalcode = form.cleaned_data['postalcode']
                    phone = form.cleaned_data['phone']
                    prefix = form.cleaned_data['prefix']
                    city = form.cleaned_data['city']
                    country = form.cleaned_data['country']
                    latitud = form.cleaned_data['latitud']
                    longitud = form.cleaned_data['longitud']
                    link = form.cleaned_data['link']
                    image = request.FILES['image']
                    description = form.cleaned_data['description']                    
                        
                    print "YA TENEMOSSSSSSSSSSSSSSSSSSSSSSSSS LOS DATOS DE L FORMULARIOOOOOOOOOOOOOOOOOOO"
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BASICA"
                    
                    no_user=""
                    name_image=""
                    user_infobasic=""
                    
                    if data_infobasic:
                    
                    #try: 
                        # This university is in DB_InfoBasic
                        print "Estoy en el try que ahora e sun if y he encontrado un item de la universidaddddddddddddddd en InfoBasic"
                        #un = InfoBasic.objects.get(uni=un_obj)
                        # el item de infobasic de esa universidad es UNI_DATA
                        
                        print "si habia en InfoBasic"
                        print "imprimimos el nombre de la imagen"
                        print str(image)
                        
                        print uni_data.username
                        
                        if (str(uni_data.username)==request.user.username):

                            if not (str(image)=="") or not (str(image)==None):
                                print "es name_image vacioooooooooooooooooooooooooooooooooooooooooo"
                                print uni_data.name_image
                            
                                if (uni_data.name_image=="") or (uni_data.name_image==None):
                                    print "name_image es vacio en el usuario "
                                    # Saving the name of the file image.xxx
                                    uni_data.image = image
                                    uni_data.name_image = str(image)
                                else:
                                
                                    im = "/tuerasmus/media/universities/" + str(uni_data.image)
                                    print "borramos esta imagen para guardar la nueva: " + im
                                    print "tengo la imagen antigua: " + im
                                    if not (im=="/tuerasmus/media/universities/"):
                                        uni_data.image.delete(im)
                                    print "esta es la nueva imagen: " + str(image)
                                    uni_data.image = image
                                    uni_data.name_image = str(image)
                                    print uni_data.image
                                    print "se supone que la he borrado y guardado la nueva"
                                
                            uni_data.description = uni_data.description + ". " + description
                            name_image = uni_data.name_image
                            description = uni_data.description
                            print "voy a intentar cambiar el valor d ela descripcion!!!!!!!!!!!!!!"
                            uni_data.save()
                        else:
                            no_user = True
                            user_infobasic = str(uni_data.username)
                            print "imprimimos un.username"
                            print str(un.username)

                    #except InfoBasic.DoesNotExist:
                    
                    else:
                    # El else de uni_infobasic=False
                    
                        # This university is not in DB_InfoBasic
                        print "Estoy en el except del try y no encontré ningun item de la universidad en InfoBaisc!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                        print "No hay nada en InfoBasic" 
                        
                        # Instanciamos la base de datos
                        uni_data = InfoBasic(uni=uniname, username=request.user.username, city=city, address=address, postalcode=postalcode, phone=phone, prefix=prefix, country=country, latitud=latitud, longitud=longitud, link=link, name_image=str(image), image=image, description=description)
                        
                        # Saving in DB
                        uni_data.save()
                        path_image = "universities/" + str(uni_data.name_image)
                    #form = BasicForm()
                    
                    ctx = {'no_user':no_user, 'user_infobasic':user_infobasic, 'alertdone':True, 'path_image':path_image, 'saved':True, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}      
                else:
                    # Invalid forms
                    
                    alerterror=True

                    ctx = {'coor':True, 'tit':tit, 'form':form, 'path_image':path_image, 'alertdone':alertdone, 'alerterror':alerterror, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            ###################### DOC FORM ######################
            elif type_form=="doc":

                form2 = CostumeServiceForm(request.POST)
                form1 = DocumentationForm(request.POST)
                form3 = AreaForm(request.POST)
                form4 = ResidenceForm(request.POST)
                form5 = WorkForm(request.POST)
                tit2 = "Documentación"
                tit1 = "Atención a los erasmus"
                tit3 = "Instalaciones de la universidad"
                tit4 = "Pisos compartidos"
                tit5 = "Prácticas, becas y trabajos en empresas"

                saved = ""
                
                if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid(): 
                    # Valid form
                    #DocumentationForm
                    unidoc = form1.cleaned_data['unidoc']
                    residencelicence = form1.cleaned_data['residencelicence']
                    getresidence = form1.cleaned_data['getresidence']
                    economicaid = form1.cleaned_data['economicaid']
                    bankaccount = form1.cleaned_data['bankaccount']
                    #CostumeServiceForm
                    costume = form2.cleaned_data['costume']
                    meetings = form2.cleaned_data['meetings']
                    offices = form2.cleaned_data['offices']
                    # AreaForm
                    qualification = form3.cleaned_data['qualification']
                    specialty = form3.cleaned_data['specialty']
                    teachingequipment = form3.cleaned_data['teachingequipment']
                    library = form3.cleaned_data['library']
                    lab = form3.cleaned_data['lab']
                    computerequipment = form3.cleaned_data['computerequipment']
                    others = form3.cleaned_data['others']
                    dinningroom = form3.cleaned_data['dinningroom']
                    cafeteria = form3.cleaned_data['cafeteria']
                    sportactivities = form3.cleaned_data['sportactivities']
                    asociation = form3.cleaned_data['asociation']
                    languagecourse = form3.cleaned_data['languagecourse']
                    schoolyear = form3.cleaned_data['schoolyear']
                    vacations = form3.cleaned_data['vacations']
                    compteleco = form3.cleaned_data['compteleco']
                    teachers = form3.cleaned_data['teachers']
                    teaching = form3.cleaned_data['teaching']
                    studies = form3.cleaned_data['studies']
                    #ResidenceForm
                    flatshare = form4.cleaned_data['flatshare']
                    linktoshare = form4.cleaned_data['linktoshare']
                    #WorkForm
                    scholarships = form5.cleaned_data['scholarships']
                    practices = form5.cleaned_data['practices']
                    contact = form5.cleaned_data['contact']
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO DOCUMENTACION"
                    print uniname.uni

                    # Instanciamos la base de datos
                    un_data = InfoGeneral(uni=uniname, username=request.user.username, unidoc=unidoc, residencelicence=residencelicence, getresidence=getresidence, economicaid=economicaid, bankaccount=bankaccount, costume=costume, meetings=meetings, offices=offices, qualification=qualification, specialty=specialty, teachingequipment=teachingequipment, library=library, lab=lab, computerequipment=computerequipment, others=others, dinningroom=dinningroom, cafeteria=cafeteria, sportactivities=sportactivities, asociation=asociation, languagecourse=languagecourse, schoolyear=schoolyear, vacations=vacations, compteleco=compteleco, teachers=teachers, teaching=teaching, studies=studies, flatshare=flatshare, linktoshare=linktoshare, scholarships=scholarships, practices=practices, contact=contact)
                    # Saving in DB
                    un_data.save()
                    form2 = CostumeServiceForm()
                    form1 = DocumentationForm()
                    form3 = AreaForm()
                    form4 = ResidenceForm()
                    form5 = WorkForm()
                    alertdone = True
                    saved = True
                else:
                    # Invalid forms
                    alerterror = True

                ctx = {'tit1':tit1, 'tit2':tit2, 'tit3':tit3, 'tit4':tit4, 'tit5':tit5, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'alerterror': alerterror, 'saved':saved, 'path_image':path_image, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### HOTEL FORM ######################
            elif type_form=="hotel":
                form1 = PlaceForm(request.POST)
                form2 = CommentForm(request.POST)
                tit1 = "Residencias universitarias"
                tit2 = "Comentarios de las residencias"                
                if form1.is_valid() and form2.is_valid():
                    # Valid form
                    #PlaceForm
                    name = form1.cleaned_data['name']
                    image = form1.cleaned_data['image']
                    address = form1.cleaned_data['address']
                    postalcode = form1.cleaned_data['postalcode']
                    city = form1.cleaned_data['city']
                    latitud = form1.cleaned_data['latitud']
                    longitud = form1.cleaned_data['longitud']
                    
                    #CommentForm
                    title = form2.cleaned_data['title']
                    text = form2.cleaned_data['text']
                    
                    
                    un_resi = Place(uni=uniname, username=request.user.username, name=name, address=address, postalcode=postalcode, city=city, latitud=latitud, longitud=longitud, image=image);
                    un_resi.save()
                                        
                    un_inforesi = InfoResidence(uni=uniname, username=request.user.username, residence=un_resi)
                    un_inforesi.save()
                    
                    un_com = Comment(username=request.user.username, uni=uniname.uni, tag=name, title=title, text=text, day_publicated=datetime.now())
                    un_com.save()
                    
                    # Saving just the resi names
                    try:
                        r = Resis.objects.get(resi=name)
                    except Resis.DoesNotExist:
                        r = Resis(resi=name)
                        r.save()
                                            
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO Residencia"
                    form1=PlaceForm()
                    form2=CommentForm()
                    alertdone=True

                else:
                    # Invalid forms
                    alerterror=True
                    
                ctx = {'coor':True, 'tit1':tit1, 'tit2':tit2, 'form1':form1, 'form2':form2, 'alerterror': alerterror, 'alertdone':alertdone, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### SUBJECTS FORM ######################
            elif type_form=="subjects":
                form1 = SubjectsForm(request.POST)
                tit1="Asignaturas impartidas fuera"
                if form1.is_valid(): 
                    # Valid form
                    #SubjectsForm
                    subname = form1.cleaned_data['subname']
                    credits = form1.cleaned_data['credits']
                    subnameout = form1.cleaned_data['subnameout']
                    subnameout2 = form1.cleaned_data['subnameout2']
                    subnameout3 = form1.cleaned_data['subnameout3']
                    works = form1.cleaned_data['works']
                    practices = form1.cleaned_data['practices']
                    difficult = form1.cleaned_data['difficult']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ASIGNATURAS"
                    
                    # Saving subject in DB's table "Subjects"
                    uni_subject = Subjects(uni=uniname, username=request.user.username, subname=subname, credits=credits, subnameout=subnameout, subnameout2=subnameout2, subnameout3=subnameout3, works=works, practices=practices, difficult=difficult)
                    


                    uni_subject.save()
                    # Saving just the subjects names
                    try:
                        s = Subjs.objects.get(subj=subname)
                    except Subjs.DoesNotExist:
                        s = Subjs(subj=subname)
                        s.save()
                                                
                    form1 = SubjectsForm()
                    alertdone=True
                else:
                    # Form not valid
                    alerterror = True
                
                ctx = {'tit1':tit1, 'form1':form1, 'alertdone': alertdone, 'alerterror':alerterror, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### CITY FORM ######################
            elif type_form=="city":
                form = CityForm(request.POST)
                if form.is_valid():
                    # Valid form
                    cityname = form.cleaned_data['cityname']
                    prices = form.cleaned_data['prices']
                    uniarea = form.cleaned_data['uniarea']
                    studentlife = form.cleaned_data['studentlife']
                    turism = form.cleaned_data['turism']
                    party = form.cleaned_data['party']
                    culture = form.cleaned_data['culture']
                    crime = form.cleaned_data['crime']
                    shopping = form.cleaned_data['shopping']
                    erasmuslife = form.cleaned_data['erasmuslife']
                    more = form.cleaned_data['more']

                    city_data = City(cityname=cityname, uni=uniname.uni, username=request.user.username, prices=prices, uniarea=uniarea, studentlife=studentlife, turism=turism, party=party, culture=culture, crime=crime, shopping=shopping, erasmuslife=erasmuslife, more=more)
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO CIUDAD"
                    city_data.save()
                    
                    # Saving just the cities
                    try:
                        c = Cities.objects.get(city=cityname)
                    except Cities.DoesNotExist:
                        c = Cities(city=cityname)
                        c.save()
                        
                    
                    form = CityForm()
                    alertdone=True
                    
                else:
                    # Invalid form
                    alerterror=True
                
                ctx = {'form':form, 'alertdone':alertdone, 'alerterror': alerterror, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### OTHERS FORM ######################
            elif type_form=="others":
                form = CommentForm(request.POST)
                tit = "Temas variados"
                if form.is_valid():
                    # Valid form
                    
                    title = form.cleaned_data['title']
                    text = form.cleaned_data['text']
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO VARIOS"
                    
                    data_others = Comment(uni=uniname.uni, username=request.user.username, tag=uniname.uni, tema=tema, title=title, text=text, day_publicated=datetime.now())
                    data_others.save()
                    
                    form = CommentForm()
                    alertdone = True
                else:
                    # Invalid form
                    alerterror = True
                    
                ctx = {'tit':tit, 'form':form, 'alerterror': alerterror, 'alertdone':alertdone, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname.uni, 'path_image':path_image, 'type_user': type_user, 'username':request.user.username}


                          
            # Return the template in method POST
            return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

        # MÉTODO GET
        if request.method=="GET":
            print "MéTODO GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"
            form0 = ImageForm(request.FILES)
            # Basic form
            if type_form=="basic":
                print "formulario basic!!!!!!!!!!!!!!!"
                form = BasicForm()
                tit = "Datos de la universidad"
                coor = True
                
            # Doc form
            elif type_form=="doc":
                form1 = CostumeServiceForm()
                form2 = DocumentationForm()
                form3 = AreaForm()
                form4 = ResidenceForm()
                form5 = WorkForm()
                tit1 = "Documentación"
                tit2 = "Atención a los erasmus"
                tit3 = "Instalaciones de la universidad"
                tit4 = "Pisos compartidos"
                tit5 = "Prácticas, becas y trabajos en empresas"
                print "formulario doooooooooooccccccccccc!!!!!!!!!!!!!!!"
                
            # Hotel form                  
            elif type_form=="hotel":
                form1 = PlaceForm()
                form2 = CommentForm()
                tit1="Residencias universitarias"
                tit2="Comentarios de las residencias"
                print "formulario hotelllllllllllllllll!!!!!!!!!!!!!!!"
                coor = True
                
            # Subjects form
            elif type_form=="subjects":
                form1 = SubjectsForm()
                tit1="Asignaturas cursadas en el extranjero"
                
            # City form
            elif type_form=="city":
                tit="Qué deben saber acerca de esta ciudad"
                form = CityForm()
                print "formulario cityyyyyyyyyyyyyyyyyyyyy!!!!!!!!!!!!!!!"
                
            # Others form
            elif type_form=="others":
                tit="Qué se nos olvida mencionar"
                form = CommentForm()
                print "Más cosas que debemos saber"

            else:
                ur = "/tuerasmus/uniedit/" + str(uniname.id)
                return HttpResponseRedirect(ur)
            
            ctx = {'coor':coor, 'tit':tit, 'form':form, 'tit1':tit1, 'form1':form1, 'tit2':tit2, 'form2':form2, 'tit3':tit3, 'tit4':tit4, 'tit5':tit5, 'form3':form3, 'form4':form4, 'form5':form5, 'path_image':path_image, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}   
            # Return the template in method GET    
            return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

    else:
        # User not authenticated
        print "UNIEDITFORM: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: MYERASMUS
# Users of your university
def myerasmus(request, user):
    if request.user.is_authenticated():
        if (request.user.username==user):

            print "MYERASMUS: usuario logueado " + user
            
            # User is student or professor
            t = User.objects.get(username=user)
            tt = t.username
            tu = Users.objects.all()
            for i in tu:
                if (tt == str(i.username)):
                    type_user = str(i.type_user)
                    
            uni1=""
            uni2=""
            uu1_list=""
            uu2_list=""
            uu1_list_empty=""
            uu2_list_empty=""
            tp = UserProfile.objects.all()
            for j in tp:
                if (tt==str(j.username)):
                    if (not (j.uni1=="")) and (not (j.uni2=="")):
                        uni1 = j.uni1
                        uni2 = j.uni2   
                    elif (not (j.uni1=="")) and (j.uni2==""):
                        uni1 = j.uni1
                    elif (j.uni1=="") and (not (j.uni2=="")):
                        uni2 = j.uni2
                    elif (j.uni1=="") and (j.uni2==""):
                        uni1=""
                        uni2=""                        
                                                               
            if (uni1=="") and (uni2==""):
                ctx = {'no_users':True, 'type_user': type_user, 'username':user}
                return render_to_response('tuerasmus/myerasmus.html', ctx, context_instance=RequestContext(request))
            else:       
                try:
                    u1 = University.objects.get(uni=uni1)
                    print "u1"
                    try:
                        nuu1 = UsersUniversity.objects.filter(uni=u1).count()
                        print "Campos con el nombre de esa universidad: " + str(nuu1)
                        uu1 = UsersUniversity.objects.get(uni=u1)
                        uu1_list = uu1.useuni.all().order_by('username')
                        if (uu1_list.count() == 0):
                            print "no hay alumnnos en uu1_list"
                            uu1_list_empty = True
                        else:
                            print "si hay alumnos"
                            uu1_list_empty = False
                            
                        for i in uu1.useuni.all():
                            print i.username
                        
                        
                        print "Imprimo el nombre del usuario que es de esa universidad1"
                    except UsersUniversity.DoesNotExist:
                        uu1 = ""
                except University.DoesNotExist:
                    u1=""
                    print "u1 vacio"
                    
                try:
                    u2 = University.objects.get(uni=uni2)
                    print "u2"
                    try:
                        nuu2 = UsersUniversity.objects.filter(uni=u2).count()
                        print "Campos con el nombre de esa universidad: " + str(nuu2)
                        uu2 = UsersUniversity.objects.get(uni=u2)
                        uu2_list = uu2.useuni.all().order_by('username')
                        
                        if (uu2_list.count() == 0):
                            print "no hay alumnnos en uu2_list"
                            uu2_list_empty = True
                        else:
                            print "si hay alumnos"
                            uu2_list_empty = False
                            
                            
                        for i in uu2.useuni.all():
                            print i.username
                        
                        
                        print "Imprimo el nombre del usuario que es de esa universidad2"
                    except UsersUniversity.DoesNotExist:
                        uu2 = ""
                except University.DoesNotExist:
                    u2=""
                    print "u2 vacio"

            print "Vamos a hacer un try para ver como conseguimos los datos que queremos de user"
            try:
                reco1=""
                reco2=""
                u = User.objects.get(username=user)
                record = UserProfile.objects.get(username=u)
                

                try:
                    rec1 = University.objects.get(uni=record.uni1)
                
                    print "rec1.id: " + str(rec1.id)

                    print record.uni1
                    reco1 = True
                except University.DoesNotExist:
                    pass
                   

                try:
                    rec2 = University.objects.get(uni=record.uni2)
                    print "rec2.id: " + str(rec2.id)

                    print record.uni2
                    reco2 = True

                except University.DoesNotExist:
                    pass

                if reco1 and not reco2:                
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco1':reco1, 'uni1':record.uni1, 'uni1id':rec1.id, 'uu1_list_empty':uu1_list_empty, 'uu2_list_empty':uu2_list_empty, 'type_user':type_user, 'username': request.user.username}
                elif reco2 and not reco1:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco2':reco2, 'uni2':record.uni2, 'uni2id':rec2.id, 'uu1_list_empty':uu1_list_empty, 'uu2_list_empty':uu2_list_empty, 'type_user':type_user, 'username': request.user.username}
                elif reco1 and reco2:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco1':reco1, 'reco2':reco2, 'uni1':record.uni1, 'uni1id':rec1.id, 'uni2':record.uni2, 'uni2id':rec2.id, 'uu1_list_empty':uu1_list_empty, 'uu2_list_empty':uu2_list_empty, 'type_user':type_user, 'username': request.user.username}
                else:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'uu1_list_empty':uu1_list_empty, 'uu2_list_empty':uu2_list_empty, 'type_user':type_user, 'username': request.user.username}
                
                    

            except UserProfile.DoesNotExist:
                print "universidades uni1 y uni2 están vacías!!!!!!!!1"
                ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'type_user':type_user, 'username': request.user.username}    

            return render_to_response('tuerasmus/myerasmus.html', ctx, context_instance=RequestContext(request))
        
        else:
            # User no authenticated
            print "MYERASMUS: Usuario logueado distinto del usuario solicitado"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User not authenticated
        print "MYERASMUS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')



# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: CITIES
# All the cities of the universities
def cities(request):
    if request.user.is_authenticated():
        print "CITIES: usuario logueado " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # Lists from DBs
        cits = Cities.objects.all().order_by('city')
        ncits = Cities.objects.all().count()
        cit = City.objects.all().order_by('cityname') 
        ncit = City.objects.all().count()           
        uall = University.objects.all().order_by('uni')       
        nuall = University.objects.all().count()  

        # Porcentajes de la web:
        # eESTOY HACIENDO ESTOS PORCENTAJES PARA LAS CIUDADES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
        #nuniversities = Universities.objects.all().count()
        #ncities = Cities.objects.all().count()
        #porcentaje_ciudades = ncities/nuniversities
        #nalumnos = Users.objects.all().filter(type_user="alumno").count()
        #porcentaje_alumnos = nalumnos/float(nusuarios)
        #nprofesores = Users.objects.all().filter(type_user="profesor").count()
        #porcentaje_profesores = nprofesores/float(nusuarios)
        #nchicos = Users.objects.all().filter(genero="male").count()
        #porcentaje_chicos = nchicos/float(nusuarios)
        #nchicas = Users.objects.all().filter(genero="female").count()
        #porcentaje_chicas = nchicas/float(nusuarios)
        
        #print "voy a imprimir los tres porcentajes que acabo de calcular"
        #print nusuarios
        #print str(porcentaje_usuarios)
        #print nalumnos
        #print str(porcentaje_alumnos)
        #print nprofesores
        #print str(porcentaje_profesores)
        #print nchicos
        #print str(porcentaje_chicos)
        #print nchicas
        #print str(porcentaje_chicas)    
            
                    
        #if request.method=="POST":
        #    city_menu = request.POST['city_selected']
        #    print city_menu
        #    try:
        #        city_data = City.objects.filter(cityname=city_menu)
        #        ctx = {'city_menu':city_menu, 'infoData':True, 'cityData':True, 'city_info':True, 'cits':cits, 'ncits':ncits, 'city_data':city_data, 'cits':cits, 'cit':cit, 'ncit':ncit, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
        #    except City.DoesNotExist:
        #        ctx = {'form_city':True, 'city_info':True, 'cit':cit, 'ncit':ncit, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
        #    return render_to_response('university/data_info.html', ctx, context_instance=RequestContext(request))
                        
        #else:                 
        #    ctx = {'city_info':True, 'cits':cits, 'ncits':ncits, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
        #    return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))
            
        if request.method=="POST":
            city_menu = request.POST['city_selected']
    
            print city_menu
            try:
                city_data = City.objects.filter(cityname=city_menu)
                city_uniid = City.objects.get(cityname=city_menu)
                print str(city_uniid.id)
                
                print "acabo de imprimir la universidad de la ciudad seleccionada en el menu"
                         

                     
                ctx = {'city_menu':city_menu, 'infoData':True, 'cityData':True, 'city_info':True, 'cits':cits, 'ncits':ncits, 'city_data':city_data, 'uni_id':city_uniid.id, 'cits':cits, 'cit':cit, 'ncit':ncit, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
            except City.DoesNotExist:
                ctx = {'form_city':True, 'city_info':True, 'cit':cit, 'ncit':ncit, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
            return render_to_response('university/data_info.html', ctx, context_instance=RequestContext(request))
                        
        else:                 
            ctx = {'city_info':True, 'cits':cits, 'ncits':ncits, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
            return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))            
        

    else:
        # User not authenticated
        print "CITIES: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')
        
        
# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: RESIDENCES
# All the residences of the universities
def residences(request):
    if request.user.is_authenticated():
        print "RESIDENCES: usuario logueado " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # Lists from DBs
        
        # uu: All the users of the universities
        uu = UsersUniversity.objects.all().order_by('username')
        
        # resis: the names of the residences (For the menu in universities.html)
        resis = Resis.objects.all().order_by('resi')
        nresis = Resis.objects.all().count()
        
        # res: Residence objects
        res = Place.objects.all().order_by('name')
        nres = Place.objects.all().count()           
        
        # All the universities
        uall = University.objects.all() .order_by('uni')      
        nuall = University.objects.all().count() 
        
        if request.method=="POST":
            resi_menu = request.POST['resi_selected']

            print resi_menu
            try:
                resi_data = Place.objects.filter(name=resi_menu)
                
                try:
                    resi_com = Comment.objects.filter(tag=resi_menu).order_by('day_publicated')
                except Comment.DoesNotExist:
                    resi_com=""
                ctx = {'infoData':True, 'resiData':True, 'resi_info':True, 'resi_menu':resi_menu, 'resis':resis, 'nresis':nresis, 'resi_data':resi_data, 'resi_com':resi_com, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
                
            except Place.DoesNotExist:
                ctx = {'form_resi':True, 'resi_info':True, 'resis':resis, 'nresis':nresis, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
            

            return render_to_response('university/data_info.html', ctx, context_instance=RequestContext(request))

        
        else:      
            ctx = {'infoData':True, 'resiData':True, 'resi_info':True, 'resis':resis, 'nresis':nresis, 'res':res, 'nres':nres, 'nuall':nuall, 'uu':uu, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
            return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))

    else:
        # User not authenticated
        print "RESIDENCES: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: SUBJECTS
# All the subjects of the universities
def subjects(request):
    if request.user.is_authenticated():
        print "SUBJECTS: usuario logueado " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)
        
        # Lists from DBs
        # subs: all the names of the subjects
        subs = Subjs.objects.all().order_by('subj')
        nsubs = Subjs.objects.all().count()
        
        # sub: all the subject objects
        
        sub = Subjects.objects.all().order_by('subname') 
        nsub = Subjects.objects.all().count()      
        if nsub==0:
            sub=""
        # All the universities     
        uall = University.objects.all().order_by('uni')       
        nuall = University.objects.all().count()   
        if nuall==0:
            uall="" 

        if request.method=="POST":
            print "ha elegido el usuario una asignatura!!!!!!!!!!!!!099999999999999999999999999999999999999"
            subj_menu = request.POST['subj_selected']
            
            if not (subj_menu==""):
                print subj_menu
                try:
                    # The subject selected exists in the DB Subjects
                    subj_data = Subjects.objects.filter(subname=subj_menu)
                    ctx = {'infoData':True, 'subjData':True, 'sub_info':True, 'subj_menu':subj_menu, 'sub':sub, 'nsub':nsub, 'subj_data':subj_data, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
                    
                except Subjects.DoesNotExist:
                    # The subject selected doesn't exist in the DB
                    ctx = {'form_resi':True, 'sub_info':True, 'sub':sub, 'nsub':nsub, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username} 
            
                return render_to_response('university/data_info.html', ctx, context_instance=RequestContext(request))
            # Option is empty
            else:
                ctx = {'sub_empty':True, 'sub_info':True, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))
        else:        
            # Method is not POST
                   
            ctx = {'infoData':True, 'subjData':True, 'sub_info':True, 'subs':subs, 'nsubs':nsubs, 'sub':sub, 'nsub':nsub, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
            return render_to_response('university/universities.html', ctx, context_instance=RequestContext(request))

    else:
        # User not authenticated
        print "SUBJECTS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')
        
# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: URERASMUS
# All the users of the website
def urerasmus(request):
    if request.user.is_authenticated():
        print "URERASMUS: usuario logueado " + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # Lists from DBs
        uu = UsersUniversity.objects.all() 
        nuu = UsersUniversity.objects.all().count()       
        uall = University.objects.all().order_by('uni')      
        nuall = University.objects.all().count()  
        
        # To show all the tuerasmus
        if nuu==0:
            ctx = {'nuu_msg':True, 'nuall':nuall, 'uu':uu, 'nuu':nuu, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
        else:
            ctx = {'nuall':nuall, 'uu':uu, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
                  
        return render_to_response('university/urerasmus.html', ctx, context_instance=RequestContext(request))

    else:
        # User not authenticated
        print "URERASMUS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


########################################################################
################# MÉTODO QUE NO SÉ SI USARÉ MÁS ADELANTE ###############
########################################################################

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : EDIT_PASSWORD
def edit_password(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):


            print "EDIT_PASSWORD: usuario logueado " + user 
                
            # Concatenate the URL with username
            ur = '/tuerasmus/' + user + '/edit_profile/'
            print "EDIT_PASSWORD: " + ur
            
            # User is professor or student
            # User has a profile image
            type_user=""
            path_image=""
            description=""
            t = User.objects.get(username=user)
            tt = t.username
            tu = Users.objects.all()
            tp = UserProfile.objects.all()
            for i in tu:
                if (tt == str(i.username)):
                    type_user = str(i.type_user)
                    genero = str(i.genero)
                    
            # Get the path of the image and the user description
            for j in tp:
                print "nombre de la imagen 555555555555555555555555: " + str(j.name_image) +" "+ str(j.username)
                print "description 5555555555555555555555555555: " + str(j.description) +" "+ str(j.username)
                if (tt == str(j.username)):
                    if ((str(j.name_image)=="") or (str(j.name_image)=="None")) and (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Estudiante de la ETSIT"
                        
                    elif ((str(j.name_image)=="") or (str(j.name_image)=="None")) and not (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = str(j.description)
                        
                    elif (str(j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Estudiante de la ETSIT"
                    elif not (str(j.description)=="") and (not (str(j.name_image)=="") or not (str(j.name_image)=="None")):
                        path_image = "profiles/" + str(j.name_image)
                        description = str(j.description)
                        
                print "voy a imprimir path_image 55555555555555555555555555555555555555555" + str(j.username)
                print path_image 

            alerterror=""
            alerterrorpass=""
            alertdone=""
            error_password=""
            msg_password=""
            
            # Method request POST
            if request.method=="POST":
                form = PasswordForm(request.POST) 
                
                # Valid form
                if form.is_valid():
                    
                    # Get the information form
                    password_one = form.cleaned_data['password_one']
                    password_two = form.cleaned_data['password_two']
                    
                    # Cheking the information
                    if (" " in password_one) or (password_one=="") or (len(password_one)<6):
                        error_password = "La contraseña no es válida"
                        msg_password = True
                        alerterrorpass= True
                        
                    else:
                        # Saving data in DB
                        try:
                            u = User.objects.get(username=user)
                            u.password=password_one
                            u.save()
                            alertdone = True
                        except User.DoesNotExist:
                            alerterror= True
                            
                    form = PasswordForm()    
                
                    # Return the template                                 
                    ctx = {'editpassword':True, 'form': form, 'error_password':error_password, 'msg_password':msg_password, 'alertdone':alertdone, 'alerterror':alerterror, 'alerterrorpass': alerterrorpass, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                    return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
    

                else:
                    # Invalid form
                    form = PasswordForm()
                    ctx = {'editpassword':True, 'form': form, 'alerterror': True, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}

                    return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))

            # Method request not POST
            else:
                form = PasswordForm()
                ctx = {'editpassword':True, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}

            # Return the template
            ctx = {'editpassword':True, 'form':form, 'username': user, 'type_user': type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))

        else:
            # User no authenticated
            print "EDIT_PASSWORD: Usuario logueado distinto del usuario solicitado"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User no authenticated
        print "EDIT_PASSWORD: usuario no logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')
        
# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: COMMENTS
# Users can comments about the website, what they like and what they don't
#def comments(request):
#    if request.user.is_authenticated():
#        print "COMMENTS: usuario logueado: " + request.user.username

        # User is student or professor
#        t = User.objects.get(username=request.user.username)
#        tt = t.username
#        tu = Users.objects.all()

#        for i in tu:
#            if (tt == str(i.username)):
#                type_user = str(i.type_user)

#        print "veamos si es método GET o POST"
#        alertsubmit=""
#        alerterror=""
#        date=""
#        time=""
#        if request.method=="POST":
#           print "método POST"
#            text = request.POST['comment']
#            print "El comentario que acaban de escribir es: " +  text
#            print "FECHA DE HOY: " + str(datetime.now())

            # Saving comment
#            if not text=="":
#               record = Comment(username=request.user.username, tag="comentarios", title="comentarios_web", text=text, day_publicated=datetime.now())
#                record.save()
#                alertsubmit=True
#            else:
#                alerterror=True       
                          
        # To show all the comments
#        comments = Comment.objects.filter(tag="comentarios")
#        if not comments.count()==0:
#            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'cmts': True, 'comments':comments, 'username':request.user.username, 'type_user': type_user}
#        else:
#            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'comments':comments, 'username':request.user.username, 'type_user': type_user}

#        return render_to_response('tuerasmus/comments.html', ctx, context_instance=RequestContext(request))
    
#    else:
        # User not authenticated
#        print "COMMENTS: el usuario no esta logueado"
#        return HttpResponseRedirect('/tuerasmus')


