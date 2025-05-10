#
from django.urls import path
from .views import AziendeList,AziendaInsert,LoadFornitori,UpdateAzienda


urlpatterns = [
        
        path(r'loadfornitori',LoadFornitori.as_view()),
        #path(r'cantieri',GetCantieri.as_view()),
        path(r'list',AziendeList.as_view()),
        path(r'insert',AziendaInsert.as_view()),
        path(r'update/<int:pk>',UpdateAzienda.as_view()),
        #path(r'testloadmodal',TestLoadModal.as_view()),
        #path(r'selectazienda/<int:azienda_id>',SelectAzienda.as_view()),
        

]
