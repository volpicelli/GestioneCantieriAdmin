from django.shortcuts import render
from django.views.generic  import View,CreateView
from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from home.models import Azienda,UsersAzienda
from django.contrib.auth.models import User

"""
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login
from .form_aziende import FormAzienda
from .form_utenti import FormUtenti
#from .azienda_serializer import Aziendaserializer
from django.core import serializers
# Create your views here.


class CheckCODCF(View):
    def get(self,request,codcf):
        try:
            a=Azienda.objects.get(codcf=codcf)
            return JsonResponse({'success':False},safe=False)
        except:
            return JsonResponse({'success':True},safe=False)




class InsertAziendaInit(View):
    def post(self,request):
        
        res = request.POST
        file = request.FILES.get('logo')
        res2={}
        res2['post']= res
        res2['file']=file.name

        codcf = request.POST.get('codcf')
        nome = request.POST.get('nome')

        a= Azienda(codcf=codcf,nome=nome)
        a.save()
        a.logo=file
        a.save()
        az = Azienda.objects.filter(codcf=codcf)
        al =list(az.values())[0]
        #s = serializers.serialize("json",az)
        
        return JsonResponse(al,safe=False)


class CreateUserAzienda(View):
    def post(self,request):

        res = request.POST
        az = request.POST.getlist('azienda')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        #res['az'] = az
        for one in az:
            a = Azienda.objects.get(id=one)
            ua = UsersAzienda(azienda=a,user=user)
            ua.save()
        res2={}
        res2['q']=res
        res2['a']=az
    
        return JsonResponse(res2,safe=False)

class InsertAzienda(CreateView):
    model=Azienda
    form_class = FormAzienda
    success_url = '/'

    #create_form = Form.create(auto__model=Cantiere)
    #a_table = Table(auto__model=Cantiere)


    def get(self,request,cantiere_id=None):
        context ={}
        #context['form']= FormAzienda() 
        #context['ordini'] = a.getOrdini()
        az = Azienda.objects.all()

        context={'aziende':az,'form':FormAzienda(),'formutenti':FormUtenti()}
        

        return render(request, "listaziende.html", context)
    


    def post(self,request,cantiere_id=None):
        #id = request.POST.get['cliente']
        #
        #cl =Cliente.objects.get(pk=id) 
        ar=[]
        res = request.POST.getlist('prezzo_unitario')
        for one in res:
            ar.append(one)

        


        return JsonResponse(res,safe=False)

        form = FormOrdine(request.POST,azienda=request.session['azienda'])
        form.fields['fornitore'].queryset = Fornitori.objects.filter(azienda=request.session['azienda'])#.values_list('id', 'codcf')

        if form.is_valid():
            # create a new `Band` and save it to the db
            ordine = form.save(commit=False)
        #cl = Cliente.objects.get(pk=cantiere.cliente) 
        #cantiere.cliente = cl #instance.cliente)
            ordine.save()

        # redirect to the detail page of the band we just created
        # we can provide the url pattern arguments as arguments to redirect function
        return HttpResponseRedirect('/ordine/update/'+str(ordine.id))
        #return redirect('pollo')
  


class IndexHome(View):
    def get(self,request):
        if request.user.is_authenticated:
            """
            az = Azienda.objects.get(id=request.session['azienda'])
            clienti = az.azienda_cliente.all()
            #clienti=Cliente.objects.filter(azienda=az)
            tutticantieri = []
            for one in clienti:
                try:
                    cantieri = one.cliente_cantiere.all()
                    #cantiere = Cantiere.objects.filter(cliente=one)
                    for o in cantieri:
                        tutticantieri.append(o)
                except ObjectDoesNotExist:
                    pass
            #c = Cantiere.objects.all()
            """
            az = Azienda.objects.all()

            context={'aziende':az}
            template = loader.get_template('listaziende.html')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/access')


class GetCantieri(View):
    def get(self,request):
        #az = Azienda.objects.get(current=True)
        az = Azienda.objects.get(id=request.session['azienda'])

        fatture = az.GetFatture()
        clienti=Cliente.objects.filter(azienda=az)
        tutticantieri = []
        for one in clienti:
            try:
                cantiere = Cantiere.objects.filter(cliente=one)
                for o in cantiere:
                    tutticantieri.append(o)
            except ObjectDoesNotExist:
                pass
        #c = Cantiere.objects.all()
        context={"cantiere":tutticantieri,'azienda': request.session['azienda'],'fatture':fatture}
        template = loader.get_template('cantieri.html')
        return HttpResponse(template.render(context, request))

class SelectAzienda(View):
    def get(self,request,azienda_id)  :
        token, created = Token.objects.get_or_create(user=request.user)

        request.session['azienda'] = azienda_id
        request.session['token'] = token.key
        return HttpResponseRedirect('/')




