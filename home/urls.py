from django.urls import path
from .views import InsertAzienda,GetCantieri,CreateUserAzienda,InsertAziendaInit,CheckCODCF,\
                InsertNuovoCliente


urlpatterns = [
        
        path(r'',InsertAzienda.as_view()),
        path(r'cantieri',GetCantieri.as_view()),
        path(r'createuserazienda',CreateUserAzienda.as_view()),
        path(r'insertazienda',InsertAziendaInit.as_view()),
        path(r'checkcodcf/<slug:codcf>',CheckCODCF.as_view()),
        path(r'nuovocliente',InsertNuovoCliente.as_view()),
        

]