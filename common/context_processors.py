from home.models import Azienda
from django.conf import settings


def message_context(request):
        #if request.user.is_authenticated:

        if 'access' in request.path or \
            'selectazienda' in request.path or \
            'auth' in request.path  :
            return ""
        else:
            #if request.user.is_authenticated():
            azienda = Azienda.objects.get(pk=request.session['azienda'])
            token = request.session['token']
            return {'context_azienda': azienda ,'context_token':token}


