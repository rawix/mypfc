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

# Database tables.  
from tuerasmus.models import Users, UniErasmus, University, Universities, UserProfile, UsersUniversity, Countries
from tuerasmus.forms import ProfileForm, UniversityForm, UniProfileForm



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

        ctx = {'username': user, 'type_user':type_user}
        return render_to_response('tuerasmus/profile2.html', ctx, context_instance=RequestContext(request))

    else:
        print "el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : MYPROFILE
def myprofile(request, user):
    if request.user.is_authenticated():
        print "MYPROFILE: usuario logueado " + user
        ur = '/tuerasmus/' + user + '/edit_profile'
        print "MYPROFILE: " + ur
        return HttpResponseRedirect(ur)
#       return render_to_response('tuerasmus/edit_profile.html', context_instance=RequestContext(request))
    else:
#        c = {}
#        c.update(csrf(request))
        print "MYPROFILE: usuario no logueado"
        return HttpResponseRedirect('/tuerasmus')
#        return render_to_response('registration/index.html', c, context_instance=RequestContext(request))

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Name : EDIT_PROFILE
def edit_profile(request, user):
    if request.user.is_authenticated():
        print "EDIT_PROFILE: usuario logueado " + user
        ur = '/tuerasmus/' + user + 'edit_profile/'
        print "EDIT_PROFILE: " + ur
        ctx = {'username': user}
        return render_to_response('tuerasmus/edit_profile.html', ctx, context_instance=RequestContext(request))
    else:
#        c = {}
#        c.update(csrf(request))
        print "EDIT_PROFILE: usuario no logueado"
        return HttpResponseRedirect('/tuerasmus')
#        return render_to_response('registration/index.html', c, context_instance=RequestContext(request))

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: MYUNIVERSITY
# User university
def myuniversity(request):


    if request.user.is_authenticated():
        print "MYUNIVERSITY: el usuario esta logueado " +  request.user.username

#        u = ""
#        try:
#            u = University.objects.(username=use)
#        except User.DoesNotExist:
#            print "quiero imprimir el campo universidad!!!! " + u.university
#            return username
             
        ctx = {'username': request.user.username}
        print "render al template de myuniversity!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        return render_to_response('tuerasmus/myuniversity.html', ctx, context_instance=RequestContext(request))
    else:
        print "MYUNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIREGISTER
# Register new university
def uniregister(request):
    
    ctx={}
    ctx.update(csrf(request))
    uni=""

    if request.user.is_authenticated():
        user = request.user.username
        print "UNIREGISTER: el usuario esta logueado: " + user

        ### User is student or professor
        t = User.objects.get(username=user)
        tt = t.username
        tu = Users.objects.all()

        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        ### Variable 'unis' is all the universities
        unis = Universities.objects.all()
        #unis = unis.extra(order_by=['noun'])
        unis = unis.extra(order_by=['country'])
                
        countries = Countries.objects.all()
        countries = countries.extra(order_by=['country'])

        print "Veamos si es metodo POST o GET"
#       form = UniRegisterForm()
        if request.method=="POST":              
            print "METODO POST"

            ### We get uni and scholarship
            uni = request.POST['uni_selected'] 
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
        print "UNIREGISTER: el usuario no esta logueado"
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

            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))  

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
        print "UNIVERSITIES: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')

# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIVERSITY
# Edit information about universities
def university(request, uni_name):
    if request.user.is_authenticated():
        print "UNIVERSITY: usuario logueado" + request.user.username
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


        ctx = {'uniname':uniname, 'type_user': type_user}
        #en este metodo debo sacar toda la informacion de las universidades que se vayan editando
        return render_to_response('tuerasmus/university.html', ctx, context_instance=RequestContext(request))
    else:
        print "UNIVERSITY: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')



# ----------------------------------------------------------------------
#-----------------------------------------------------------------------
# Name: UNIEDIT
# Edit the information of universities
def uniedit(request):
    if request.user.is_authenticated():
      
        print "UNIEDIT: usuario logueado" + request.user.username
        
        # User is student or professor
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        ctx = {'username':request.user.username, 'type_user': type_user}
        return render_to_response('tuerasmus/edit_university.html', ctx, context_instance=RequestContext(request))

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

        ctx = {'username':request.user.username, 'type_user': type_user}
        #en este metodo debo sacar toda la informacion de las universidades que se vayan editando
        return render_to_response('tuerasmus/foro.html', ctx, context_instance=RequestContext(request))

    else:
        print "el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')






