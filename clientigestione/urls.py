#
from django.urls import path
from .views import ClientiGestione,NuovoClienteGestione,UpdateClienteGestione,TestLoadModal,RemoteautocompleteCliente


urlpatterns = [
        
        #path(r'',IndexHome.as_view()),
        #path(r'cantieri',GetCantieri.as_view()),
        path(r'list',ClientiGestione.as_view(),name='listclienti'),
        path(r'nuovo',NuovoClienteGestione.as_view()),
        path(r'update/<int:pk>',UpdateClienteGestione.as_view(), name='updatecliente'),
        path(r'testloadmodal',TestLoadModal.as_view()),
        path(r'remote',RemoteautocompleteCliente.as_view()),
        

]
