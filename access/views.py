from django.shortcuts import render
from django.views.generic  import View
from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Cantiere,Azienda,Cliente,UsersAzienda

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

class Authenticate(View):
    def post(self,request):
        username = request.POST.get('username') #.upper()
        password = request.POST.get('password')


        user = authenticate(request,username=username, password=password)
        if user:
            login(request, user)
            request.session['login'] = user.username
            #template = loader.get_template('index.html')
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

            #return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/access/nouserenabled')

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
        return HttpResponseRedirect('/access')