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
from tuerasmus.models import City, Comment, Countries, Info, ResiComment, Residences, Subjects, UniComment, UniErasmus, Universities, University, UserProfile, Users, UsersUniversity

# Forms
from tuerasmus.forms import ProfileForm, BasicForm, CostumeServiceForm, DocumentationForm, AccommodationForm, SubjectsForm, WorkForm, CityForm, OthersForm



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
        print "HOME USER: Usuario logueado: " + user

        # User is professor or student
        type_user=""
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # Return the template
        ctx = {'username': user, 'type_user':type_user}
        return render_to_response('tuerasmus/profile.html', ctx, context_instance=RequestContext(request))

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
        print "MYPROFILE: usuario logueado " + user

        # Concatenate URL + username
        ur = '/tuerasmus/' + user + '/edit_profile'
        print "MYPROFILE: " + ur
        # Redirect url
        return HttpResponseRedirect(ur)

    else:
        # User no authenticated
        print "MYPROFILE: usuario no logueado"
        # Redirect to main URL
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : EDIT_PROFILE
def edit_profile(request, user):

    if request.user.is_authenticated():
        print "EDIT_PROFILE: usuario logueado " + user 
 
        # Concatenate the URL with username
        ur = '/tuerasmus/' + user + 'edit_profile/'
        print "EDIT_PROFILE: " + ur

        # Return the template
        ctx = {'username': user}
        return render_to_response('tuerasmus/edit_profile.html', ctx, context_instance=RequestContext(request))

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

        # User is student or professor
        type_user=""
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # Variable 'unis' is all the universities
        unis = Universities.objects.all()
        unis = unis.extra(order_by=['country'])
                
        countries = Countries.objects.all()
        countries = countries.extra(order_by=['country'])

        print "Veamos si es metodo POST o GET"
#       form = UniRegisterForm()
        
        if request.method=="POST":        
            uni=""
            print "METODO POST"

            ### We get uni and scholarship
            unimenu = request.POST['uni_selected'] 
            unitext = request.POST['uni_written']

            print "UNI_SELECTED: " + unimenu
            print "UNI_WRITTEN: " + unitext

            if unitext=="":
                uni=unimenu
            else:
                uni=unitext

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
                            un = University(uni=uni, scholarship=scholarship)
                            un.save()       
                            print "un.save()"
                            une = UniErasmus(uni=uni, scholarship=scholarship) 
                            une.save()
                            print "une.save()"
                            


                            #i.university.add(uni)
                            #print "i.university.add(un.uni)"


                            # Incrementamos el número de usuarios de esa universidad
                            nusers += 1
                            print "nusers: " + str(nusers)
                            unu = UsersUniversity(uni=un, nusers=nusers)
                            print "unu.nusers: " + str(unu.nusers) 
                            unu.save()
                            print "unu.save()"


                            print "GUARDAMOS EN LAS BASES DE DATOS"


                            print "SE SUPONE QUE MI USUARIO AHORA TIENE SU UNIVERSIDAD GUARDADA"
                            uu_saved = University.objects.get(uni=uni)
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
                                    j.save()

                        
                        if done:
                            # Done es True, con lo cual acabamos de registrarla
                            print "ESTOY EN ALERTAS DE DONEEEEEEEEEEEEE"
                            ctx = {'alertdone':True, 'uni_name':uni, 'uni_id':uu_saved.id, 'saved':True, 'countries':countries, 'unis':unis, 'username':user, 'type_user':type_user}
                        else:
                            # La universidad ya existe, y no la hemos registrado
                            print "ESTOY EN ALERTAS DE WARNINGGGGGGGGGGGGGGGGGGGGGGGG"
                            ctx = {'alertwarning':True, 'uni_name':u_saved, 'uni_id':u_saved.id, 'saved':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                         


                        print "meto en UserUniversity el nuevo usuario que se ha registrado en esa universidad"
                        unu = University.objects.get(uni=uni)
                        unuu = UsersUniversity.objects.all()
                        for k in unuu:
                            if str(k.uni)==(unu.uni):
                                k.useuni.add(i.username)
                                print "useu.useuni.add"
                        
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
                            un = University(uni=uni, scholarship=scholarship)
                            un.save()
                            print "un.save()"
                            une = UniErasmus(uni=uni, scholarship=scholarship) 
                            une.save()
                            print "une.save()"
                            #i.university.add(uni)
                            #print "i.university.add(un.uni)"


                            # Incrementamos el número de usuarios de esa universidad
                            nusers += 1
                            print "nusers: " + str(nusers)
                            unu = UsersUniversity(uni=un, nusers=nusers)
                            print "unu.nusers: " + str(unu.nusers) 
                            unu.save()
                            print "unu.save()"


                            print "GUARDAMOS EN LAS BASES DE DATOS"


                            print "SE SUPONE QUE MI USUARIO AHORA TIENE SU UNIVERSIDAD GUARDADA"
                            uu_saved = University.objects.get(uni=uni)
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
                                    j.save()

                          

                        
                        if done:
                            # Done es True, con lo cual acabamos de registrarla
                            print "ESTOY EN ALERTAS DE DONEEEEEEEEEEEEE"
                            ctx = {'alertdone':True, 'uni_name':uni, 'uni_id':uu_saved.id, 'saved':True, 'countries':countries, 'unis':unis, 'username':user, 'type_user':type_user}
                        else:
                            # La universidad ya existe, y no la hemos registrado
                            print "ESTOY EN ALERTAS DE WARNINGGGGGGGGGGGGGGGGGGGGGGGG"
                            ctx = {'alertwarning':True, 'uni_name':u_saved, 'uni_id':u_saved.id, 'saved':True, 'countries': countries, 'unis': unis, 'username': user, 'type_user': type_user}
                       

                        print "meto en UserUniversity el nuevo usuario que se ha registrado en esa universidad"
                        unu = University.objects.get(uni=uni)
                        unuu = UsersUniversity.objects.all()
                        for k in unuu:
                            if str(k.uni)==(unu.uni):
                                k.useuni.add(i.username)
                                print "useu.useuni.add"
                             
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
            #form = UniRegisterForm()
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
        user = request.user.username
        # EN ESTE MÉTODO TENGO QUE BUSCAR EN LA TABLA UNIERASMUS Y OBTENER TODAS LAS UNIVERSIDADES YA REGISTRADAS, PARA
        # PODER ACCEDER A LOS DISTINTOS PERFILES Y EDITAR LO QUE NECESITAMOS EDITAR.

        # DEBERÉ REALIZAR LAS OPERACIONES NECESARIOS PARA QUE SE MUESTREN LAS UNIVERSIDADES SEGÚN: tipo de beca, alumnos registrados en cada una, 
        # según el país, valoración de los alumnos... ESTOS DATOS SE MOSTRARAN EN LISTAS, BARRAS DE PORCENTAJES, ETC


        ### User is student or professor
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()

        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # TENGO QUE ENCONTRAR DONDE METER ESTAS LINEAS PARA EL POST O GET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print "tt:" + str(tt)


        # Checking if user can edit university's profile
        #print "VOY A HACER UN FORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
        #for k in (UsersUniversity.objects.all()):
        #    print "DENTRO DEL FOR FORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"
        #    if (tt == str(k.useuni)):
        #        print "ME HA SALIDO TRUE EL IFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
        #        uniuser=k.uni
        #        print "LA UNIVERSIDAD ES: " + str(k.uni)
        #    else:
        #        print "ME HA SALIDO FALSE EL IFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
        #        uniuser=""
        #try:
        #    print "ESTOY EN EL TRY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        #    uniuser = UsersUniversity.objects.get(useuni=str(tt))

        #except UsersUniversity.DoesNotExist:
        #    uniuser = ""

        uniuser=""
        if request.method=="GET":              
            print "METODO GET"

            ### Show all universities in TuErasmus
            uniserasmus=""
            unismundus=""
            uems_msg=""

            print "UNISERASMUS ANTES DEL TRY: " + str(uniserasmus)
            print "UNISMUNDUS ANTES DEL TRY:" + str(unismundus)

        
            print "el numero de objectos en ue es: " + str(UniErasmus.objects.all().filter(scholarship="erasmus").count())
            if (UniErasmus.objects.all().filter(scholarship="erasmus").count())==0:
                uniserasmus=False
            else:
                uniserasmus=True
       
            print "el numero de objectos en um es: " + str(UniErasmus.objects.all().filter(scholarship="mundus").count())
            if (UniErasmus.objects.all().filter(scholarship="mundus").count())==0:
                unismundus=False
            else:
                unismundus=True   

            print "UNISERASMUS ES: " + str(uniserasmus)
            print "UNISMUNDUS ES: " + str(unismundus) 
            print "SE SUPONE QUE YA TENGO TODAS LAS UNIVERSIDADES DE ERASMUS!!!!!!!!!!!!!!!!!!!!!!"

            try:
                uems = UniErasmus.objects.all()
                uems_ = True
            except UniErasmus.DoesNotExist:
                uems_msg = "No hay universidades registradas"
                uems_ = False

            if uniserasmus and unismundus:
                ctx = {'uniserasmus':uniserasmus, 'ue':UniErasmus.objects.all().filter(scholarship="erasmus"), 'unismundus':unismundus, 'um':UniErasmus.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user}
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))

            if uniserasmus and not unismundus:
                ctx = {'uniserasmus':uniserasmus, 'ue':UniErasmus.objects.all().filter(scholarship="erasmus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user}
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))

            if unismundus and not uniserasmus:
                ctx = {'unismundus':unismundus, 'um':UniErasmus.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user} 
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))      

            if not unismundus and not uniserasmus:
                ctx = {'unisempty':True, 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user}
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))    

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


#                ctx = {'username': user, 'type_user': type_user}
#                return render_to_response('tuerasmus/university.html', ctx, context_instance=RequestContext(request))
                
            
        
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
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()

        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # In UniErasmus we can get the name of the university
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"   
            return HttpResponseRedirect('/tuerasmus/universities')


        ctx = {'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        #en este metodo debo sacar toda la informacion de las universidades que se vayan editando
        #return render_to_response('tuerasmus/google_maps.html', ctx, context_instance=RequestContext(request))
        return render_to_response('university/geouniversity.html', ctx, context_instance=RequestContext(request))
        #return render_to_response('tuerasmus/googlemaps.html', ctx, context_instance=RequestContext(request))
        #return render_to_response('tuerasmus/university.html', ctx, context_instance=RequestContext(request))
        #return render_to_response('tuerasmus/googleprueba.html', ctx, context_instance=RequestContext(request))
        #return render_to_response('tuerasmus/googleversionprueba.html', ctx, context_instance=RequestContext(request))
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
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        # MÉTODO GET
        if request.method=="GET":
            if type_info=="basic":
                print "muestro la info basica"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            elif type_info=="doc":
                print "muestro la info doc"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                 
            elif type_info=="hotel":
                print "muestro la info hotel"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            elif type_info=="subjects":
                print "muestro la info subjects"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            elif type_info=="city":
                print "muestro la info city"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            elif type_info=="others":
                print "muestro la info others"
                ctx = {'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
            # EStamos probando, pero será uni_info.html el template que se muestre y heredará de university.html!!!
            return render_to_response('university/university.html', ctx, context_instance=RequestContext(request))

# AQUI DEBERIA HACER EL QUE PINCHASEN A UN BOTON PARQA EDITAR LA INFORMACION QUE DESEEN EN ESE MOMENTO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # MÉTODO POST
        if request.method=="POST":
            
            if type_form=="basic":
                print "type_form es basic!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                form = BasicForm(request.POST)
                if form.is_valid(): 
                    # Valid form
                    uni = uniname
                    print "uni: " + str(uni)
                    acronym = form.cleaned_data['acronym']
                    address = form.cleaned_data['address']
                    city = form.cleaned_data['city']
                    print "city: " + str(city)
                    country = form.cleaned_data['country']

                    # URLs 
                    #location = form.cleaned_data['location']
                    latitud = form.cleaned_data['latitud']
                    longitud = form.cleaned_data['longitud']
                    link = form.cleaned_data['link']
                    image = form.cleaned_data['image']

                    description = form.cleaned_data['description']
                    qualification = form.cleaned_data['qualification']
                    specialty = form.cleaned_data['specialty']
                    teachingequipment = form.cleaned_data['teachingequipment']

                    librariy = form.cleaned_data['librariy']
                    lab = form.cleaned_data['lab']
                    computerequipment = form.cleaned_data['computerequipment']

                    others = form.cleaned_data['others']

                    dinningroom = form.cleaned_data['dinningroom']
                    cafeteria = form.cleaned_data['cafeteria']
                    sportactivities = form.cleaned_data['sportactivities']
                    asociation = form.cleaned_data['asociation']
                    languagecourse = form.cleaned_data['languagecourse']
                    schoolyear = form.cleaned_data['schoolyear']
                    vacations = form.cleaned_data['vacations']
                    compteleco = form.cleaned_data['compteleco']
                    teachers = form.cleaned_data['teachers']
                    teaching = form.cleaned_data['teaching']
                    studies = form.cleaned_data['studies']
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BASICA"
                    uni_data = Info(uni=uni, acronym=acronym, city=city, address=address, country=country, link=link, image=image, description=description, latitud=latitud, longitud=longitud)
                    
                    #uni_data = UniversityInfo(uni=uni, acronym=acronym, address=address, city=city, country=country, link=link, image=image, description=description, qualification=qualification, specialty, specialty, teachingequipment=teachingequipment, library=library, lab=lab, computerequipment=computerequipment, others=others, dinningroom=dinningroom, cafeteria=cafeteria, sportactivities=sportactivities, asociation=asociation, languagecourse=languagecourse, schoolyear=schoolyear, vacations=vacations, compteleco=compteleco, teachers=teachers, teaching=teaching, studies=studies)

                    uni_data.save()

                    ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'alertdone':True, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

                else:
                    # Form not valid
                    ctx = {'form': form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_form':type_form, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))


            elif type_form=="doc":

                form1 = CostumeServiceForm(request.POST)
                form2 = DocumentationForm(request.POST)
                if form1.is_valid(): 
                    # Valid form
                    unidoc = form1.cleaned_data['unidoc']
                    residencelicence = form1.cleaned_data['residencelicence']
                    getresidence = form1.cleaned_data['getresidence']
                    economicaid = form1.cleaned_data['economicaid']
                    bankaccount = form1.cleaned_data['bankaccount']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO DOCUMENTACION"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

                if form2.is_valid():
                    # Valid form
                    costume = form2.cleaned_data['costume']
                    meetings = form2.cleaned_data['meetings']
                    offices = form2.cleaned_data['offices']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ATENCION"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

              

            elif type_form=="hotel":

                form = AccommodationForm(request.POST)
                if form.is_valid():
                    # Valid form
                    residencehall = form.cleaned_data['residencehall']
                    flatshare = form.cleaned_data['flatshare']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO Residencia"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="subjects":
                form1 = SubjectsForm(request.POST)
                form2 = WorkForm(request.POST)
                if form1.is_valid(): 
                    # Valid form
                    subjects = form1.cleaned_data['subjects']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ASIGNATURAS"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

                if form2.is_valid():
                    # Valid form
                    scholarships = form2.cleaned_data['scholarships']
                    practices = form2.cleaned_data['practices']
                    contact = form2.cleaned_data['contact']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BECAS"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="city":
                form = CityForm(request.POST)
                if form.is_valid():
                    # Valid form
                    general = form.cleaned_data['general']
                    prices = form.cleaned_data['prices']
                    theuniversity = form.cleaned_data['theuniversity']
                    studentlife = form.cleaned_data['studentlife']
                    turism = form.cleaned_data['turism']
                    goingout = form.cleaned_data['goingout']
                    culture = form.cleaned_data['culture']
                    crime = form.cleaned_data['crime']
                    shopping = form.cleaned_data['shopping']
                    erasmuslife = form.cleaned_data['erasmuslife']
                    more = form.cleaned_data['more']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO CIUDAD"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="others":
                form = OthersForm(request.POST)
                if form.is_valid():
                    # Valid form
                    others = form.cleaned_data['general']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO VARIOS"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))


        # With uni id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        
        ctx = {'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

    else:
        print "UNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: MYUNIVERSITY
# User university/s
def myuniversity(request, user):


    if request.user.is_authenticated():
        print "MYUNIVERSITY: el usuario esta logueado " +  user

        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        
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

                if ("-" in record.uni1):
                    record.uni1=record.uni1.split(" - ")[1]
                else:
                    record.uni1=record.uni1

                print record.uni1
                reco1 = True
 
            except University.DoesNotExist:
                pass
               

            try:
                rec2 = University.objects.get(uni=record.uni2)
                print "rec2.id: " + str(rec2.id)

                print record.uni2
                
                if ("-" in record.uni2):
                    record.uni2=record.uni2.split(" - ")[1]
                else:
                    record.uni2=record.uni2

                print record.uni2
                reco2 = True

            except University.DoesNotExist:
                pass

            if reco1 and not reco2:                
                ctx = {'reco1':reco1, 'uni1':record.uni1, 'uni1id':rec1.id, 'type_user':type_user, 'username': request.user.username}
            elif reco2 and not reco1:
                ctx = {'reco2':reco2, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'username': request.user.username}
            elif reco1 and reco2:
                ctx = {'reco1':reco1, 'reco2':reco2, 'uni1':record.uni1, 'uni1id':rec1.id, 'uni2':record.uni2, 'uni2id':rec2.id, 'type_user':type_user, 'username': request.user.username}
            else:
                ctx = {'type_user':type_user, 'username': request.user.username}
            
                

        except UserProfile.DoesNotExist:
            print "universidades uni1 y uni2 están vacías!!!!!!!!1"
            ctx = {'type_user':type_user, 'username': request.user.username}    


        return render_to_response('tuerasmus/myuniversity.html', ctx, context_instance=RequestContext(request))

    else:
        print "MYUNIVERSITY: el usuario no esta logueado"
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

        # With uni id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)  
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)
        
        ctx = {'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

    else:
        print "UNIVERSITY: el usuario no esta logueado"
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

        # With uni id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        # MÉTODO GET
        if request.method=="GET":
            if type_form=="basic":
                print "type_form es basic!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                form = BasicForm(request.POST)
                ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

            elif type_form=="doc":
                form1 = CostumeServiceForm(request.POST)
                form2 = DocumentationForm(request.POST)
                ctx = {'form1':form1, 'form2':form2, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))
                 
            elif type_form=="hotel":
                form = AccommodationForm(request.POST)
                ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

            elif type_form=="subjects":
                form1 = SubjectsForm(request.POST)
                form2 = WorkForm(request.POST)
                ctx = {'form1':form1, 'form2':form2, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

            elif type_form=="city":
                form = CityForm(request.POST)
                ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

            elif type_form=="others":
                form = OthersForm(request.POST)
                ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
                return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))




        # MÉTODO POST
        if request.method=="POST":
            
            if type_form=="basic":
                print "type_form es basic!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                form = BasicForm(request.POST)
                if form.is_valid(): 
                    # Valid form
                    uni = uniname
                    print "uni: " + str(uni)
                    acronym = form.cleaned_data['acronym']
                    address = form.cleaned_data['address']
                    city = form.cleaned_data['city']
                    print "city: " + str(city)
                    country = form.cleaned_data['country']

                    # URLs 
                    #location = form.cleaned_data['location']
                    latitud = form.cleaned_data['latitud']
                    longitud = form.cleaned_data['longitud']
                    link = form.cleaned_data['link']
                    image = form.cleaned_data['image']

                    description = form.cleaned_data['description']
                    qualification = form.cleaned_data['qualification']
                    specialty = form.cleaned_data['specialty']
                    teachingequipment = form.cleaned_data['teachingequipment']

                    librariy = form.cleaned_data['librariy']
                    lab = form.cleaned_data['lab']
                    computerequipment = form.cleaned_data['computerequipment']

                    others = form.cleaned_data['others']

                    dinningroom = form.cleaned_data['dinningroom']
                    cafeteria = form.cleaned_data['cafeteria']
                    sportactivities = form.cleaned_data['sportactivities']
                    asociation = form.cleaned_data['asociation']
                    languagecourse = form.cleaned_data['languagecourse']
                    schoolyear = form.cleaned_data['schoolyear']
                    vacations = form.cleaned_data['vacations']
                    compteleco = form.cleaned_data['compteleco']
                    teachers = form.cleaned_data['teachers']
                    teaching = form.cleaned_data['teaching']
                    studies = form.cleaned_data['studies']
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BASICA"
                    uni_data = Info(uni=uni, acronym=acronym, city=city, address=address, country=country, link=link, image=image, description=description, latitud=latitud, longitud=longitud)
                    
                    #uni_data = UniversityInfo(uni=uni, acronym=acronym, address=address, city=city, country=country, link=link, image=image, description=description, qualification=qualification, specialty, specialty, teachingequipment=teachingequipment, library=library, lab=lab, computerequipment=computerequipment, others=others, dinningroom=dinningroom, cafeteria=cafeteria, sportactivities=sportactivities, asociation=asociation, languagecourse=languagecourse, schoolyear=schoolyear, vacations=vacations, compteleco=compteleco, teachers=teachers, teaching=teaching, studies=studies)

                    uni_data.save()

                    ctx = {'form':form, 'uniname':uniname, 'uni_name':uni_name, 'alertdone':True, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

                else:
                    # Form not valid
                    ctx = {'form': form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_form':type_form, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))


            elif type_form=="doc":

                form1 = CostumeServiceForm(request.POST)
                form2 = DocumentationForm(request.POST)
                if form1.is_valid(): 
                    # Valid form
                    unidoc = form1.cleaned_data['unidoc']
                    residencelicence = form1.cleaned_data['residencelicence']
                    getresidence = form1.cleaned_data['getresidence']
                    economicaid = form1.cleaned_data['economicaid']
                    bankaccount = form1.cleaned_data['bankaccount']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO DOCUMENTACION"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

                if form2.is_valid():
                    # Valid form
                    costume = form2.cleaned_data['costume']
                    meetings = form2.cleaned_data['meetings']
                    offices = form2.cleaned_data['offices']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ATENCION"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

              

            elif type_form=="hotel":

                form = AccommodationForm(request.POST)
                if form.is_valid():
                    # Valid form
                    residencehall = form.cleaned_data['residencehall']
                    flatshare = form.cleaned_data['flatshare']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO Residencia"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="subjects":
                form1 = SubjectsForm(request.POST)
                form2 = WorkForm(request.POST)
                if form1.is_valid(): 
                    # Valid form
                    subjects = form1.cleaned_data['subjects']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ASIGNATURAS"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

                if form2.is_valid():
                    # Valid form
                    scholarships = form2.cleaned_data['scholarships']
                    practices = form2.cleaned_data['practices']
                    contact = form2.cleaned_data['contact']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BECAS"
                else:
                    # Form not valid
                    ctx = {'form1':form1, 'form2':form2, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="city":
                form = CityForm(request.POST)
                if form.is_valid():
                    # Valid form
                    general = form.cleaned_data['general']
                    prices = form.cleaned_data['prices']
                    theuniversity = form.cleaned_data['theuniversity']
                    studentlife = form.cleaned_data['studentlife']
                    turism = form.cleaned_data['turism']
                    goingout = form.cleaned_data['goingout']
                    culture = form.cleaned_data['culture']
                    crime = form.cleaned_data['crime']
                    shopping = form.cleaned_data['shopping']
                    erasmuslife = form.cleaned_data['erasmuslife']
                    more = form.cleaned_data['more']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO CIUDAD"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))

            elif type_form=="others":
                form = OthersForm(request.POST)
                if form.is_valid():
                    # Valid form
                    others = form.cleaned_data['general']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO VARIOS"

                else:
                    # Form not valid
                    ctx = {'form':form, 'alerterror': True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
                    return render_to_response('university/edit_university.html', ctx, context_instance=RequestContext(request))


        # With uni id we can get the name
        try:
            uniname = University.objects.get(id=uni_name)
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        
        ctx = {'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

    else:
        print "UNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: MYERASMUS
# Users of your university
def myerasmus(request, user):
    if request.user.is_authenticated():
      
        print "URERASMUS: usuario logueado" + user
        
        # User is student or professor
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        ctx = {'type_user': type_user, 'username':user}
        return render_to_response('tuerasmus/myerasmus.html', ctx, context_instance=RequestContext(request))

    else:
        print "UNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: URERASMUS
# All the users of the website
def urerasmus(request):
    if request.user.is_authenticated():
      
        print "URERASMUS: usuario logueado" + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        ctx = {'type_user': type_user, 'username':request.user.username}
        return render_to_response('tuerasmus/urerasmus.html', ctx, context_instance=RequestContext(request))

    else:
        print "UNIVERSITY: el usuario no esta logueado"
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
            comment = request.POST['comment']
            print "El comentario que acaban de escribir es: " +  comment
            print "FECHA DE HOY: " + str(datetime.now())

            # Saving comment
            if not comment=="":
                record = Comment(username=request.user.username, comment=comment, day=datetime.now())
                record.save()
                alertsubmit=True

            else:
                alerterror=True       

            
        # To show all the comments
        comments = Comment.objects.all()
        if not comments.count()==0:
            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'cmts': True, 'comments':comments, 'username':request.user.username, 'type_user': type_user}
        else:
            ctx = {'alertsubmit':alertsubmit, 'alerterror':alerterror, 'comments':comments, 'username':request.user.username, 'type_user': type_user}

        return render_to_response('tuerasmus/comments.html', ctx, context_instance=RequestContext(request))
            
    # User not authenticated
    else:
        print "COMMENTS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


