from django.shortcuts import render
from django.views.generic  import View,ListView,CreateView
from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.models import User, Group

from home.models import Cantiere,Azienda,Cliente,UsersAzienda,Azienda
from home.form_utenti import FormUtenti

"""
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
"""
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class RemoteautocompleteAzienda(View):
    def get(self,request):
        q = request.GET.get('q')
        resp=[]
        res = Azienda.objects.filter(nome__icontains=q).values_list('nome')
        for one in res:
            a={}
            a['nome']=one
            resp.append(a)


        return JsonResponse(resp,safe=False)


class UsersList(ListView):
    model = Azienda
    template_name = "usersList.html"
    def get(self,request):
        u = User.objects.filter(groups__name='Aziende')
        ua=[]

        #for one in u:
        #    one.userazienda.all()
        #    ua.append(one.azienda)



        context={"users":u}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))



class Authenticate(View):
    def post(self,request):
        username = request.POST.get('username') #.upper()
        password = request.POST.get('password')


        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            request.session['login'] = user.username
            #template = loader.get_template('index.html')
            """
            all = user.userazienda.all()
            az= []
            for one in all:
                az.append(one.azienda)
            token, created = Token.objects.get_or_create(user=user)
            
            if len(az) > 1:
                context={'aziende': az,'token':token.key}
                return render(request, 'listaziende.html', context)
            else:
                request.session['azienda'] = one.azienda.id
                request.session['token'] = token.key
                return HttpResponseRedirect('/home')
            """
            if user.is_superuser:

                return HttpResponseRedirect('/')
            else: 
                return HttpResponseRedirect('/access/nouserenabled')

            #return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/access/nouserenabled')


class CreateUserXAzienda(CreateView):
    template_name='createuser.html'
    model = User

    def get(self,request):
        if not request.user.is_authenticated:        
            return HttpResponseRedirect('/access/login')
            
        form = FormUtenti()
        az= Azienda.objects.all()
    
        return render(request, self.template_name, {'form': form,'aziende':az})
     

    def post(self,request):

        res = request.POST
        #az = request.POST('azienda')
        username = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')

        return JsonResponse(res,safe=False)

        user = User.objects.create_user(username=username, password=password)
        user.save()
        group_azienda = Group.objects.get(name="Azienda")
        user.groups.add(group_azienda)
        user.save()
        
        #res['az'] = az
        #for one in az:
        #a = Azienda.objects.get(id=one)
        #ua = UsersAzienda(azienda=a,user=user)
        #ua.save()
        res2={}
        res2['q']=res
        res2['a']=az
    
        return JsonResponse(res2,safe=False)


class SelectAzienda(View):
    def get(self,request,azienda_id)  :
        token, created = Token.objects.get_or_create(user=request.user)

        request.session['azienda'] = azienda_id
        request.session['token'] = token.key
        return HttpResponseRedirect('/')

"""
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        all = user.userazienda.all()
        az= []
        for one in all:
            az.append(one.azienda.id)
        token, created = Token.objects.get_or_create(user=user)
        request.session['azienda'] = one.azienda.id
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'azienda': az,
            'email': user.email
        })
"""

class Login(View):
    def get(self,request):
        c = Cantiere.objects.all()
        context={"cantiere":c}
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))


class Logout(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/access/login')