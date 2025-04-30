from django.urls import path
from .views import Login ,Authenticate,SelectAzienda,Logout#,GetCantieri


urlpatterns = [
        
        #path(r'',IndexHome.as_view()),
        #path(r'cantieri',GetCantieri.as_view()),
        path(r'',Login.as_view()),
        path(r'logout',Logout.as_view()),
        #path(r'auth',Authenticate.as_view()),
        #path(r'auth',Authenticate.as_view()),
        path(r'selectazienda/<int:azienda_id>',SelectAzienda.as_view()),
        

]
