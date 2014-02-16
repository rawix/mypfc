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
from tuerasmus.models import City, Comment, Countries, InfoBasic, InfoGeneral, InfoResidence, InfoStadistic, Place, Score, Subjects, Universities, University, UserProfile, Users, UsersUniversity

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

        # Variable 'unis' has all the universities
        unis = Universities.objects.all()
        unis = unis.extra(order_by=['country'])
                
        countries = Countries.objects.all()
        countries = countries.extra(order_by=['country'])

        print "Veamos si es metodo POST o GET"
        

        if request.method=="POST": 
            form = BasicForm(request.POST)       
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

            if uniserasmus and unismundus:
                ctx = {'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user}
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))

            if uniserasmus and not unismundus:
                ctx = {'uniserasmus':uniserasmus, 'ue':University.objects.all().filter(scholarship="erasmus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user}
#            return render_to_response('tuerasmus/universities.html', ctx, context_instance=RequestContext(request))

            if unismundus and not uniserasmus:
                ctx = {'unismundus':unismundus, 'um':University.objects.all().filter(scholarship="mundus"), 'uniuser':uniuser, 'uems':uems, 'uems_':uems_, 'uems_msg':uems_msg, 'username': user, 'type_user': type_user} 
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
        type_user=""
        t = User.objects.get(username=request.user.username)
        tt = t.username
        tu = Users.objects.all()
        for i in tu:
            if (tt == str(i.username)):
                type_user = str(i.type_user)

        # In University we can get the name of the university
        try:
            uniname = University.objects.get(id=uni_name[0])
            print "Se encontró el nombre de la universidad!!!!!!: " + str(uniname)
            try:
                uniobj = InfoBasic.objects.get(uni=uniname)
                latitud = uniobj.latitud
                longitud = uniobj.longitud
                print "vamos a imprimir los valores de latitud y longitud"
                print latitud
                print longitud
            except InfoBasic.DoesNotExist:
                latitud = 0.0
                longitud = 0.0
                
            
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"   
            return HttpResponseRedirect('/tuerasmus/universities')

        print "Voy a imprimir el valor de la variable uniname"
        print uniname
        ctx = {'uniobj':uniobj, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
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
            
        except University.DoesNotExist:
            print "No se han encontrado ningun objecto con ese id"  
            ur = "/tuerasmus" + tt + "/myuniversity" 
            return HttpResponseRedirect(ur)

        # MÉTODO GET
        if request.method=="GET":
             
            uni = InfoBasic.objects.get(uni=uniname)
            print str(uni.image)
            ur = "/tuerasmus/media/universities/"+str(uni.image) 
            print ur
            if type_info=="basic":
                print "muestro la info basica"
                info="basic"
                info_list = InfoGeneral.objects.filter(uni=uniname.uni)

            elif type_info=="doc":
                print "muestro la info doc"
                info="doc"
                info_list = InfoGeneral.objects.filter(uni=uniname.uni)
                print "Acabamos de obtener nuestra info_list"
                print InfoGeneral.objects.all().count()
                 
            elif type_info=="hotel":
                print "muestro la info hotel"
                info="hotel"
                info_list = Place.objects.filter(uni=uniname.uni)
                print "imprimiendo los nombres de residencias"
                for i in info_list:
                    print i.name
                    print i.latitud
                    print i.longitud

                ctx = {'uni':uni, 'ur':ur, 'info':info, 'info_list':info_list, 'uniimage':uni.image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

                # Return the template
                return render_to_response('university/georesidence.html', ctx, context_instance=RequestContext(request))


            elif type_info=="subjects":
                print "muestro la info subjects"
                info="subjects"

            elif type_info=="city":
                print "muestro la info city"
                info="city"

            elif type_info=="others":
                print "muestro la info others"
                info="others"
                
            ctx = {'uni':uni, 'ur':ur, 'info':info, 'info_list':info_list, 'uniimage':uni.image, 'uniname':uniname.uni,  'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            # Return the template
            return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))

        # OTRO MÉTODO
#        elif request.method=="POST":
            
#            op = request.POST['op']
#            print op
#            if op=="modqua":
#                print "la opcion es la de modificar"

#                ctx = {'texto':True, 'basic':True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
#            elif op=="delqua":
#                print "la opcion es la de eliminar"
#                ctx = {'texto':True, 'basic':True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
#            else:
#                ctx = {'basic':True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
            
        else:
            ctx = {'basic':True, 'uni_name':uni_name, 'uniname':uniname, 'type_user': type_user, 'username':request.user.username}
        
            # Return the template
            return render_to_response('university/uni_info.html', ctx, context_instance=RequestContext(request))

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
                print "reco1 y reco2 son True!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
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

        uni = uniname.uni
        
        # MÉTODO POST
        if request.method=="POST":
            alertdone=""
            alerterror=""
            
            un_obj = University.objects.get(uni=uni)
            
            ###################### BASIC FORM ######################
            if type_form=="basic":
                form = BasicForm(request.POST, request.FILES)
                if form.is_valid(): 
                    # Valid form
                    address = form.cleaned_data['address']
                    city = form.cleaned_data['city']
                    country = form.cleaned_data['country']
                    latitud = form.cleaned_data['latitud']
                    longitud = form.cleaned_data['longitud']
                    link = form.cleaned_data['link']
                    image = request.FILES['image']
                    description = form.cleaned_data['description']                    
                   
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO BASICA"
                    
                    
                    try: 
                        un = InfoBasic.objects.get(uni=un_obj)
                        print "si habia en InfoBasic"

                        un.image = image
                        un.description = un.description + ". " + description
                        print "voy a intentar cambiar el valor d ela descripcion!!!!!!!!!!!!!!"
                        un.save()

                    except InfoBasic.DoesNotExist:
                        print "No hay nada en InfoBasic" 
                        
                        # Instaciamos la base de datos
                        uni_data = InfoBasic(uni=un_obj, city=city, address=address, country=country, latitud=latitud, longitud=longitud, link=link, image=image, description=description)
                        # Saving in DB
                        uni_data.save()

                    form = BasicForm()
                    alertdone = True
                          
                else:
                    # Invalid forms
                    alerterror=True

                ctx = {'coor':True, 'form':form, 'alertdone':alertdone, 'alerterror':alerterror, 'uniname':uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}

            ###################### DOC FORM ######################
            elif type_form=="doc":

                form2 = CostumeServiceForm(request.POST)
                form1 = DocumentationForm(request.POST)
                form3 = AreaForm(request.POST)
                tit2 = "Documentación"
                tit1 = "Atención a los erasmus"
                tit3 = "Instalaciones de la universidad"
                
                if form1.is_valid() and form2.is_valid() and form3.is_valid(): 
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

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO DOCUMENTACION"
                    print uni

                    # Instanciamos la base de datos
                    un_data = InfoGeneral(uni=un_obj, username=request.user.username, unidoc=unidoc, residencelicence=residencelicence, getresidence=getresidence, economicaid=economicaid, bankaccount=bankaccount, costume=costume, meetings=meetings, offices=offices, qualification=qualification, specialty=specialty, teachingequipment=teachingequipment, library=library, lab=lab, computerequipment=computerequipment, others=others, dinningroom=dinningroom, cafeteria=cafeteria, sportactivities=sportactivities, asociation=asociation, languagecourse=languagecourse, schoolyear=schoolyear, vacations=vacations, compteleco=compteleco, teachers=teachers, teaching=teaching, studies=studies)
                    # Saving in DB
                    un_data.save()
                    form2 = CostumeServiceForm()
                    form1 = DocumentationForm()
                    form3 = AreaForm()
                    alertdone = True
                else:
                    # Invalid forms
                    alerterror = True

                ctx = {'tit1':tit1, 'tit2':tit2, 'tit3':tit3, 'form1':form1, 'form2':form2, 'form3':form3, 'alerterror': alerterror, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uni, 'type_user': type_user, 'username':request.user.username}

            ###################### HOTEL FORM ######################
            elif type_form=="hotel":
                form1 = PlaceForm(request.POST)
                form2 = ResidenceForm(request.POST)
                tit1 = "Residencias universitarias"
                tit2 = "Pisos compartidos"
                                
                if form1.is_valid() and form2.is_valid():
                    # Valid form

                    #PlaceForm
                    name = form1.cleaned_data['name']
                    image = form1.cleaned_data['image']
                    address = form1.cleaned_data['address']
                    latitud = form1.cleaned_data['latitud']
                    longitud = form1.cleaned_data['longitud']
                    #ResidenceForm
                    flatshare = form2.cleaned_data['flatshare']
                    linktoshare = form2.cleaned_data['linktoshare']
                    
                    un_resi = Place(uni=un_obj, name=name, address=address, latitud=latitud, longitud=longitud, image=image);
                    un_resi.save()
                    
                    un_data = InfoResidence(uni=un_obj, residence=un_resi, flatshare=flatshare, linktoshare=linktoshare)
                    un_data.save()
                    
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO Residencia"
                    form1=PlaceForm()
                    form2=ResidenceForm()
                    alertdone=True

                else:
                    # Invalid forms
                    alerterror=True
                    
                ctx = {'coor':True, 'tit1':tit1, 'tit2':tit2, 'form1':form1, 'form2':form2, 'alerterror': alerterror, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### SUBJECTS FORM ######################
            elif type_form=="subjects":
                form1 = SubjectsForm(request.POST)
                form2 = WorkForm(request.POST)
                tit1="Asignaturas impartidas fuera"
                tit2="Prácticas, becas y trabajos en empresas"
                if form1.is_valid() and form2.is_valid(): 
                    # Valid form
                    #SubjectsForm
                    subname = form1.cleaned_data['subname']
                    credits = form1.cleaned_data['credits']
                    subnameout = form1.cleaned_data['subnameout']
                    #WorkForm
                    scholarships = form2.cleaned_data['scholarships']
                    practices = form2.cleaned_data['practices']
                    contact = form2.cleaned_data['contact']

                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO ASIGNATURAS"
                    uni_uni = University.objects.get(uni=uni)
                    uni_subject = Subjects(uni=uni_uni, subname=subname, credits=credits, subnameout=subnameout)
                    uni_subject.save()
                    try:
                        un_data = University.objects.get(uni=uni)
                        un_data.scholarships = scholarships
                        un_data.practices = practices
                        un_data.contact = contact
                        un_data.save()
                    except University.DoesNotExist:
                        un_data = University(uni=uni, practices=practices, scholarships=scholarships, contact=contact)
                        un_data.save()

                    alertdone=True
                else:
                    # Form not valid
                    alerterror = True
                
                ctx = {'tit1':tit1, 'tit2':tit2, 'form1':form1, 'form2':form2, 'alertdone': alertdone, 'alerterror':alerterror, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

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

                    city_data = City(cityname=cityname, prices=prices, uniarea=uniarea, studentlife=studentlife, turism=turism, party=party, culture=culture, crime=crime, shopping=shopping, erasmuslife=erasmuslife, more=more)
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO CIUDAD"
                    city_data.save()
                    alertdone=True
                    form = CityForm()
                else:
                    # Invalid form
                    alerterror=True
                
                ctx = {'form':form, 'alertdone':alertdone, 'alerterror': alerterror, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            ###################### OTHERS FORM ######################
            elif type_form=="others":
                form = OthersForm(request.POST)
                if form.is_valid():
                    # Valid form
                    others = form.cleaned_data['general']
                    print "DEBO GUARDAR LOS DATOS RECOGIDOS DEL FORMULARIO VARIOS"
                    
                    alertdone = True
                else:
                    # Invalid form
                    alerterror = True
                    
                ctx = {'form':form, 'alerterror': alerterror, 'alertdone':alertdone, 'uni_name':uni_name, 'uniname':uniname.uni, 'type_user': type_user, 'username':request.user.username}

            # Return the template in method POST
            return render_to_response('university/uni_form.html', ctx, context_instance=RequestContext(request))

        # MÉTODO GET
        if request.method=="GET":
            # Basic form
            if type_form=="basic":
                print "formulario basic!!!!!!!!!!!!!!!"
                form = BasicForm()
                ctx = {'coor':True, 'form':form, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
            # Doc form
            elif type_form=="doc":
                form1 = CostumeServiceForm()
                form2 = DocumentationForm()
                form3 = AreaForm()
                tit1 = "Documentación"
                tit2 = "Atención a los erasmus"
                tit3 = "Instalaciones de la universidad"

                print "formulario doooooooooooccccccccccc!!!!!!!!!!!!!!!"
                ctx = {'tit1':tit1, 'tit2':tit2, 'tit3':tit3, 'form1':form1, 'form2':form2, 'form3':form3, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
            # Hotel form                  
            elif type_form=="hotel":
                form1 = PlaceForm()
                form2 = ResidenceForm()
                tit1="Residencias universitarias"
                tit2="Pisos compartidos"
                print "formulario hotelllllllllllllllll!!!!!!!!!!!!!!!"
                ctx = {'tit1':tit1, 'tit2':tit2, 'form1':form1, 'form2':form2, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
            # Subjects form
            elif type_form=="subjects":
                form1 = SubjectsForm()
                form2 = WorkForm()
                print "formulario subjects!!!!!!!!!!!!!!!"
                tit1="Asignaturas cursadas en el extranjero"
                tit2="Becas, prácticas y trabajo"
                print "formulario hotelllllllllllllllll!!!!!!!!!!!!!!!"
                ctx = {'tit1':tit1, 'tit2':tit2, 'form1':form1, 'form2':form2, 'uniname':uniname.uni, 'uni_name':uni_name, 'type_user': type_user, 'username':request.user.username}
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
      
        print "MYERASMUS: usuario logueado" + user
        
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
        # User not authenticated
        print "MYERASMUS: el usuario no esta logueado"
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
    
    else:
        # User not authenticated
        print "COMMENTS: el usuario no esta logueado"
        return HttpResponseRedirect('/tuerasmus')


