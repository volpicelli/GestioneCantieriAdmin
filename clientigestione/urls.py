#
from django.urls import path
from .views import ClientiGestione,NuovoClienteGestione,UpdateClienteGestione


urlpatterns = [
        
        #path(r'',IndexHome.as_view()),
        #path(r'cantieri',GetCantieri.as_view()),
        path(r'list',ClientiGestione.as_view()),
        path(r'nuovo',NuovoClienteGestione.as_view()),
        path(r'update/<int:pk>',UpdateClienteGestione.as_view()),
        #path(r'auth',Authenticate.as_view()),
        #path(r'selectazienda/<int:azienda_id>',SelectAzienda.as_view()),
        

]
