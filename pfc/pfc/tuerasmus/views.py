#encoding:utf-8
##########################################################################
# @Author : Rawan Nazmi-Issa Khozouz                                     #
# @Date : 18/09/13.                                                      #
# @Description : Views that handle the urls selected.                    #
##########################################################################

# Libraries.

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
from tuerasmus.models import City, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistic, Others, Place, Score, Subjects, Universities, University, UserProfile, Users, UsersUniversity

# Forms
from tuerasmus.forms import ProfileForm, BasicForm, AreaForm, CostumeServiceForm, DocumentationForm, ResidenceForm, PlaceForm, SubjectsForm, WorkForm, CityForm, OthersForm



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
            print "HOME USER: Usuario logueado: " + user

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
                print "nombre de la imagen 11111111111111111111: " + str(j.name_image) + str(j.username)
                print "description 111111111111111111111: " + str(j.description) + str(j.username)
                if (tt == str(j.username)):
                    if (str(j.name_image)=="") or (str(j.name_image)=="None") and (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Mi erasmus será genial"
                        
                    elif (str(j.name_image)=="") or (str(j.name_image)=="None") and not (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = str(j.description)
                        
                    elif (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Mi erasmus será genial"
                    elif not (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = str(j.description)
                        
                print "voy a imprimir path_image 111111111111111111111111111111111111111111" + str(j.username)
                print path_image      
            

            # Return the template
            ctx = {'username': user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/home.html', ctx, context_instance=RequestContext(request))
        else:
            # User no authenticated
            print "HOMEUSER: Usuario logueado distinto del usuario solicitado"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
              
    else:
        # User no authenticated
        print "HOME USER: el usuario no esta logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : MYPROFILE
def myprofile(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):
            print "HOME USER: Usuario logueado: " + user
            print "MYPROFILE: usuario logueado " + user
                       
            # Concatenate URL + username
            ur = '/tuerasmus/' + user + '/edit_profile'
            print "MYPROFILE: " + ur
            # Redirect url
            return HttpResponseRedirect(ur)
        else:
            # User no authenticated
            print "MYPROFILE: Usuario logueado distinto del usuario solicitado"
            ur = "/tuerasmus/" + user + "/profile"
            # Redirect to main URL
            return HttpResponseRedirect(ur)
    else:
        # User no authenticated
        print "MYPROFILE: usuario no logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : PROFILE
def profile(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):
            print "PROFILE: Usuario logueado: " + user
                       
            # Concatenate URL + username
            ur = '/tuerasmus/' + user + '/edit_profile'
            print "MYPROFILE: " + ur
            # Redirect url
            return HttpResponseRedirect(ur)
        else:
 
            print "PROFILE: usuario logueado " + request.user.username
            print "PROFILE: USUARIO SOLICITADO: " + user
                       
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
                print "nombre de la imagen 3333333333333333333: " + str(j.name_image) + str(j.username)
                print "description 3333333333333333333: " + str(j.description) + str(j.username)
                if (tt == str(j.username)):
                    if (str(j.name_image)=="") or (str(j.name_image)=="None") and (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Mi erasmus será genial"
                        
                    elif (str(j.name_image)=="") or (str(j.name_image)=="None") and not (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = str(j.description)
                        
                    elif (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Mi erasmus será genial"
                    elif not (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = str(j.description)
                        
                print "voy a imprimir path_image 3333333333333333333333333333333333333" + str(j.username)
                print path_image  

            # Return the template
            ctx = {'up_obj':j, 'see_profile':True, 'username': user, 'type_user': type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))

    else:
        # User no authenticated
        print "EDIT_PROFILE: usuario no logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')
        
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : EDIT_PROFILE
def edit_profile(request, user):

    if request.user.is_authenticated():
        if (request.user.username==user):


            print "EDIT_PROFILE: usuario logueado " + user 
                
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
            for j in tp:
                print "nombre de la imagen 555555555555555555555555: " + str(j.name_image) + str(j.username)
                print "description 5555555555555555555555555555: " + str(j.description) + str(j.username)
                if (tt == str(j.username)):
                    if (str(j.name_image)=="") or (str(j.name_image)=="None") and (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Mi erasmus será genial"
                        
                    elif (str(j.name_image)=="") or (str(j.name_image)=="None") and not (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = str(j.description)
                        
                    elif (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Mi erasmus será genial"
                    elif not (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = str(j.description)
                        
                print "voy a imprimir path_image 55555555555555555555555555555555555555555" + str(j.username)
                print path_image 

            if request.method=="POST":
                form = ProfileForm(request.POST, request.FILES) 
                if form.is_valid():
                    # Valid form
                    name = form.cleaned_data['name']
                    lastname = form.cleaned_data['lastname']
                    description = form.cleaned_data['description']
                    image = form.cleaned_data['image']
                    print str(image)
                    for u in tp:
                        if (str(u.username) == tt):
                            u.name = name
                            u.lastname = lastname
                            u.description = description
                            
                            if u.name_image=="":
                                u.name_image = str(image)
                                u.image = image
                            else:
                                
                                im = "/tuerasmus/media/profiles/" + str(u.image)
                                print "borramos esta imagen para guardar la nueva: " + im
                                u.image.delete(im)
                                print "esta es la nueva imagen: " + str(image)
                                u.name_image = str(image)
                                u.image = image
                                print "ya tenemos guardada la imagen nueva"
                                
                                
                            print "recogi la info del form"
                            u.save()
                            print "se han guardado los datos del perfil de usuario"
                            
                            form = ProfileForm()
                            ctx = {'alertdone':True, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
                        else:
                            print "No existe el usuario"
                            ctx = {'alerterror':True, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                else:
                    # Invalid form
                    form = ProfileForm()
                    ctx = {'alerterror':True, 'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}
                    
            else:
                form = ProfileForm()
                ctx = {'form': form, 'username':user, 'type_user':type_user, 'genero':genero, 'path_image':path_image, 'description':description}

            # Return the template
            ctx = {'form':form, 'username': user, 'type_user': type_user, 'genero':genero, 'path_image':path_image, 'description':description}
            return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))
        else:
            # User no authenticated
            print "EDIT_PROFILE: Usuario logueado distinto del usuario solicitado"
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
            if uniserasmus and unismundus:
                ctx = {'uall':uall, 'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}
 
            if uniserasmus and not unismundus:
                ctx = {'uall':uall, 'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}
 
            if unismundus and not uniserasmus:
                ctx = {'uall':uall, 'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user} 
 
            if not unismundus and not uniserasmus:
                ctx = {'uall':uall, 'unisempty':True, 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': request.user.username, 'type_user': type_user}

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
        try:
            uniname = University.objects.get(id=uni_name[0])
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            try:
                uniobj = InfoBasic.objects.get(uni=uniname)
                latitud = uniobj.latitud
                longitud = uniobj.longitud
                
                if (str(uniobj.name_image)==""):
                    path_image="tuerasmus/universidad.png"
                else:
                    path_image=str(uniobj.name_image)
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
            return HttpResponseRedirect('/tuerasmus/universities')

        print "Voy a imprimir el valor de la variable uniname"
        print uniname
        ctx = {'uniobj':uniobj, 'path_image':path_image, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
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
    if request.user.is_authenticated():
        print "UNINFO: usuario logueado: " + request.user.username
        
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
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        # MÉTODO POST
        if request.method=="POST":
            data = request.POST['qualification']
            
            if data=="mod":
                print "modificamos comentario"
                data_obj = InfoGeneral.objects.get(username=request.user.username)
                print str(data_obj.qualification)
                info_list = InfoGeneral.objects.all()
                
                ctx = {'no_info': True, 'basic':True, 'modqua':True, 'info_list':info_list, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}
                print "retornamos el template para modificar"

                return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))
                
            elif data=="delqua":
                print "eliminamos comentario"
            
                ctx = {'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}
            
                # Return the template
                return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))
            
            
        # MÉTODO GET
        if request.method=="GET":
            path_image=""
            try:
                uni = InfoBasic.objects.get(uni=uniname)
                print str(uni.image)
                print uni.latitud
                print uni.longitud
                path_image = str(uni.image) 
                print path_image
                if type_info=="basic":
                    print "muestro la info basica"
                    info="basic"
                    info_list = InfoGeneral.objects.filter(uni=uniname.uni)
                    
                    print "modificamos comentario en GET info basic" 
                    


                elif type_info=="doc":
                    print "muestro la info doc"
                    info="doc"
                    info_list = InfoGeneral.objects.filter(uni=uniname.uni)
                    print "Acabamos de obtener nuestra info_list"
                    print InfoGeneral.objects.all().count()
                     
                elif type_info=="hotel":
                    arr = []
                    print "muestro la info hotel"
                    info="hotel"
                    info_list = Place.objects.filter(uni=uniname.uni)
                    print "imprimiendo los nombres de residencias"
                    n = 0;
                    for i in info_list:
                        arr.append([str(i.name), str(i.latitud), str(i.longitud)])
                        print arr[n]
                        n+=1

                    ctx = {'mispuntos':arr, 'uni':uni, 'info':info, 'info_list':info_list, 'path_image':path_image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

                    # Return the template
                    return render_to_response('university/georesidence.html', ctx, context_instance=RequestContext(request))


                elif type_info=="subjects":
                    print "muestro la info subjects"
                    info="subjects"
                    info_list=Subjects.objects.all()

                elif type_info=="city":
                    print "muestro la info city"
                    info="city"
                    info_list=City.objects.all()

                elif type_info=="others":
                    print "muestro la info others"
                    info="others"
                    
                    
                ctx = {'uni':uni, 'info':info, 'info_list':info_list, 'path_image':path_image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
            except InfoBasic.DoesNotExist:
                # uniname.uni: uni's name
                # uni_name: id_uni
                # uni.image: url's image of uni
                path_image = "tuerasmus/universidad.png"
                ctx = {'no_info':True, 'path_image':path_image, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
               

            # Return the template
            return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))


            
        #else:
        #    ctx = {'basic':True, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}
        
            # Return the template
        #    return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))

    else:
        # User no authenticated
        print "UNIVERSITY: el usuario no esta logueado"
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
                print "description 7777777777777777777777777: " + str(j.description) + str(j.username)
                if (tt == str(j.username)):
                    if (str(j.name_image)=="") or (str(j.name_image)=="None") and (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"
                        description = "Mi erasmus será genial"
                        
                    elif (str(j.name_image)=="") or (str(j.name_image)=="None") and not (str(j.description)==""):
                        if genero=="male":
                            path_image ="tuerasmus/male.jpg"
                        elif genero=="female":
                            path_image="tuerasmus/female.jpg"               
                        description = str(j.description)
                        
                    elif (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = "Mi erasmus será genial"
                    elif not (str(j.description)=="") and not (str(j.name_image)=="") or not (str(j.name_image)=="None"):
                        path_image = "profiles/" + str(j.name_image)
                        description = str(j.description)
                        
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
        try:
            uniname = University.objects.get(id=uni_name)
            print uniname.uni
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus/" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)
        
        # MÉTODO POST
        if request.method=="POST":
            alertdone=""
            alerterror=""
            
            un_obj = University.objects.get(uni=uniname.uni)
            
            ###################### BASIC FORM ######################
            if type_form=="basic":
                tit = "Datos de la universidad"
                form = BasicForm(request.POST, request.FILES)
                if form.is_valid(): 
                    # Valid form
                    address = form.cleaned_data['address']
                    postalcode = form.cleaned_data['postalcode']
                    phone = form.cleaned_data['phone']
                    city = form.cleaned_data['city']
                    country = form.cleaned_data['country']
                    latitud = form.cleaned_data['latitud']
                    longitud = form.cleaned_data['longitud']
                    link = form.cleaned_data['link']
                    image = request.FILES['image']
                    description = form.cleaned_data['description']                    
                   
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BASICA"
                    
                    no_user=""
                    name_image=""
                    user_infobasic=""
                    try: 
                        un = InfoBasic.objects.get(uni=un_obj)
                        print "si habia en InfoBasic"
                        print "imprimimos el nombre de la imagen"
                        print str(image)
                        print un.username
                        if (str(un.username)==request.user.username):
                        
                            if (str(un.image)==""):
                                un.image = image
                                un.name_image = str(image)
                            else:
                            
                                im = "/tuerasmus/media/universities/" + str(un.image)
                                print "tengo la imagen antigua: " + im
                                un.image.delete(im)
                                un.image = image
                                un.name_image = str(image)
                                print un.image
                                print "se supone que la he borrado y guardado la nueva"
                            
                            un.description = un.description + ". " + description
                            name_image = str(un.name_image)
                            description = str(un.description)
                            print "voy a intentar cambiar el valor d ela descripcion!!!!!!!!!!!!!!"
                            un.save()
                        else:
                            no_user = True
                            user_infobasic = str(un.username)
                            print "imprimimos un.username"
                            print str(un.username)

                    except InfoBasic.DoesNotExist:
                        print "No hay nada en InfoBasic" 
                        
                        # Instanciamos la base de datos
                        uni_data = InfoBasic(uni=un_obj, username=request.user.username, city=city, address=address, postalcode=postalcode, phone=phone, country=country, latitud=latitud, longitud=longitud, link=link, name_image=name_image, image=image, description=description)
                        # Saving in DB
                        uni_data.save()

                    #form = BasicForm()
                    
                    ctx = {'no_user':no_user, 'user_infobasic':user_infobasic, 'alertdone':True, 'saved':True, 'uniname':uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}      
                else:
                    # Invalid forms
                    
                    alerterror=True

                    ctx = {'coor':True, 'tit':tit, 'form':form, 'alertdone':alertdone, 'alerterror':alerterror, 'uniname':uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

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
                    un_data = InfoGeneral(uni=un_obj, username=request.user.username, unidoc=unidoc, residencelicence=residencelicence, getresidence=getresidence, economicaid=economicaid, bankaccount=bankaccount, costume=costume, meetings=meetings, offices=offices, qualification=qualification, specialty=specialty, teachingequipment=teachingequipment, library=library, lab=lab, computerequipment=computerequipment, others=others, dinningroom=dinningroom, cafeteria=cafeteria, sportactivities=sportactivities, asociation=asociation, languagecourse=languagecourse, schoolyear=schoolyear, vacations=vacations, compteleco=compteleco, teachers=teachers, teaching=teaching, studies=studies, flatshare=flatshare, linktoshare=linktoshare, scholarships=scholarships, practices=practices, contact=contact)
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

                ctx = {'tit1':tit1, 'tit2':tit2, 'tit3':tit3, 'tit4':tit4, 'tit5':tit5, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'alerterror': alerterror, 'saved':saved, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### HOTEL FORM ######################
            elif type_form=="hotel":
                form1 = PlaceForm(request.POST)
                tit1 = "Residencias universitarias"
                                
                if form1.is_valid():
                    # Valid form
                    #PlaceForm
                    name = form1.cleaned_data['name']
                    image = form1.cleaned_data['image']
                    address = form1.cleaned_data['address']
                    postalcode = form1.cleaned_data['postalcode']
                    city = form1.cleaned_data['city']
                    latitud = form1.cleaned_data['latitud']
                    longitud = form1.cleaned_data['longitud']
                    
                    un_resi = Place(uni=un_obj, name=name, address=address, postalcode=postalcode, city=city, latitud=latitud, longitud=longitud, image=image);
                    un_resi.save()
                                        
                    un_inforesi = InfoResidence(uni=un_obj, username=request.user.username, residence=un_resi)
                    un_inforesi.save()
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO Residencia"
                    form1=PlaceForm()
                    alertdone=True

                else:
                    # Invalid forms
                    alerterror=True
                    
                ctx = {'coor':True, 'tit1':tit1, 'form1':form1, 'alerterror': alerterror, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

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
                    
                    uni_subject = Subjects(uni=un_obj, username=request.user.username, subname=subname, credits=credits, subnameout=subnameout, subnameout2=subnameout2, subnameout3=subnameout3, works=works, practices=practices, difficult=difficult)
                    uni_subject.save()

                        
                    form1 = SubjectsForm()
                    alertdone=True
                else:
                    # Form not valid
                    alerterror = True
                
                ctx = {'tit1':tit1, 'form1':form1, 'alertdone': alertdone, 'alerterror':alerterror, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

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

                    city_data = City(cityname=cityname, username=request.user.username, prices=prices, uniarea=uniarea, studentlife=studentlife, turism=turism, party=party, culture=culture, crime=crime, shopping=shopping, erasmuslife=erasmuslife, more=more)
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO CIUDAD"
                    city_data.save()
                    form = CityForm()
                    alertdone=True
                    
                else:
                    # Invalid form
                    alerterror=True
                
                ctx = {'form':form, 'alertdone':alertdone, 'alerterror': alerterror, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### OTHERS FORM ######################
            elif type_form=="others":
                form = OthersForm(request.POST)
                tit = "Temas variados"
                if form.is_valid():
                    # Valid form
                    tema = form.cleaned_data['tema']
                    title = form.cleaned_data['title']
                    body_text = form.cleaned_data['body_text']
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO VARIOS"
                    
                    data_others = Others(uni=uni_obj.uni, username=request.user.username, tema=tema, title=title, body_text=body_text)
                    data_others.save()
                    
                    form = OthersForm()
                    alertdone = True
                else:
                    # Invalid form
                    alerterror = True
                    
                ctx = {'tit':tit, 'form':form, 'alerterror': alerterror, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            # Return the template in method POST
            return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

        # MÉTODO GET
        if request.method=="GET":
            # Basic form
            if type_form=="basic":
                print "formulario basic!!!!!!!!!!!!!!!"
                form = BasicForm()
                tit = "Datos de la universidad"
                ctx = {'coor':True, 'tit':tit, 'form':form, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
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
                ctx = {'tit1':tit1, 'tit2':tit2, 'tit3':tit3, 'tit4':tit4, 'tit5':tit5, 'form1':form1, 'form2':form2, 'form3':form3, 'form4':form4, 'form5':form5, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
            # Hotel form                  
            elif type_form=="hotel":
                form1 = PlaceForm()
                tit1="Residencias universitarias"
                print "formulario hotelllllllllllllllll!!!!!!!!!!!!!!!"
                ctx = {'coor':True, 'tit1':tit1, 'form1':form1, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
            # Subjects form
            elif type_form=="subjects":
                form1 = SubjectsForm()
                tit1="Asignaturas cursadas en el extranjero"
                ctx = {'tit1':tit1, 'form1':form1, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
            # City form
            elif type_form=="city":
                tit="Qué deben saber acerca de esta ciudad"
                form = CityForm()
                print "formulario cityyyyyyyyyyyyyyyyyyyyy!!!!!!!!!!!!!!!"
                ctx = {'tit':tit, 'form':form, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
            # Others form
            elif type_form=="others":
                tit="Qué se nos olvida mencionar"
                form = OthersForm()
                print "Más cosas que debemos saber"
                ctx = {'tit':tit, 'form':form, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                
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
            tp = UserProfile.objects.all()
            for j in tp:
                if (tt==str(j.username)):
                    if not (j.uni1=="") and not (j.uni2==""):
                        uni1 = j.uni1
                        uni2 = j.uni2   
                    elif not (j.uni1=="") and (j.uni2==""):
                        uni1 = j.uni1
                    elif (j.uni1=="") and not (j.uni2==""):
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
                    try:
                        nuu1 = UsersUniversity.objects.filter(uni=u1).count()
                        print "Campos con el nombre de esa universidad: " + str(nuu1)
                        uu1 = UsersUniversity.objects.get(uni=u1)
                        uu1_list = uu1.useuni.all().order_by('username')
                        for i in uu1.useuni.all():
                            print i.username
                        
                        
                        print "Imprimo el nombre del usuario que es de esa universidad1"
                    except UsersUniversity.DoesNotExist:
                        uu1 = ""
                except University.DoesNotExist:
                    u1=""
                    
                try:
                    u2 = University.objects.get(uni=uni2)
                    try:
                        nuu2 = UsersUniversity.objects.filter(uni=u2).count()
                        print "Campos con el nombre de esa universidad: " + str(nuu2)
                        uu2 = UsersUniversity.objects.get(uni=u2)
                        uu2_list = uu2.useuni.all().order_by('username')
                        for i in uu2.useuni.all():
                            print i.username
                        
                        
                        print "Imprimo el nombre del usuario que es de esa universidad2"
                    except UsersUniversity.DoesNotExist:
                        uu2 = ""
                except University.DoesNotExist:
                    u2=""

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
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco1':reco1, 'uni1':record.uni1, 'uni1id':rec1.id, 'type_user':type_user, 'username': request.user.username}
                elif reco2 and not reco1:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco2':reco2, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'username': request.user.username}
                elif reco1 and reco2:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'reco1':reco1, 'reco2':reco2, 'uni1':record.uni1, 'uni1id':rec1.id, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'username': request.user.username}
                else:
                    ctx = {'uu1_list':uu1_list, 'uu2_list':uu2_list, 'type_user':type_user, 'username': request.user.username}
                
                    

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

        cit = City.objects.all().order_by('cityname') 
        ncit = City.objects.all().count()           
        uall = University.objects.all().order_by('uni')       
        nuall = University.objects.all().count()                    
        ctx = {'city_info':True, 'cit':cit, 'ncit':ncit, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
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

        uu = UsersUniversity.objects.all().order_by('username')
        res = Place.objects.all().order_by('cityname')
        nres = Place.objects.all().count()           
        uall = University.objects.all() .order_by('uni')      
        nuall = University.objects.all().count()                    
        ctx = {'resi_info':True, 'res':res, 'nres':nres, 'nuall':nuall, 'uu':uu, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
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

        sub = Subjects.objects.all().order_by('subname') 
        nsub = Subjects.objects.all().count()           
        uall = University.objects.all().order_by('uni')       
        nuall = University.objects.all().count()                    
        ctx = {'sub_info':True, 'sub':sub, 'nsub':nsub, 'nuall':nuall, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
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

        uu = UsersUniversity.objects.all()          
        uall = University.objects.all().order_by('uni')      
        nuall = University.objects.all().count()                    
        ctx = {'nuall':nuall, 'uu':uu, 'uall':uall, 'type_user': type_user, 'username':request.user.username}
        return render_to_response('university/urerasmus.html', ctx, context_instance=RequestContext(request))

    else:
        # User not authenticated
        print "URERASMUS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: COMMENTS
# Users can comments about the website, what they like and what they don't
def comments(request):
    if request.user.is_authenticated():
        print "COMMENTS: usuario logueado: " + request.user.username

        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()

        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        print "veamos si es método GET o POST"
        alertsubmit=""
        alerterror=""
        date=""
        time=""
        if request.method=="POST":
            print "método POST"
            text = request.POST['comment']
            print "El comentario que acaban de escribir es: " +  text
            print "FECHA DE HOY: " + str(datetime.now())

            # Saving comment
            if not text=="":
                record = Comment(username=request.user.username, tag="comentarios", title="comentarios_web", text=text, day_publicated=datetime.now())
                record.save()
                alertsubmit=True
            else:
                alerterror=True       
                          
        # To show all the comments
        comments = Comment.objects.filter(tag="comentarios")
        if not comments.count()==0:
            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'cmts': True, 'comments':comments, 'username':request.user.username, 'type_user': type_user}
        else:
            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'comments':comments, 'username':request.user.username, 'type_user': type_user}

        return render_to_response('tuerasmus/comments.html', ctx, context_instance=RequestContext(request))
    
    else:
        # User not authenticated
        print "COMMENTS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


