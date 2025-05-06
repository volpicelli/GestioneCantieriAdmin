from django.urls import path
from .views import Login,Authenticate,SelectAzienda,Logout,UsersList,CreateUserXAzienda,\
                        RemoteautocompleteAzienda #,GetCantieri


urlpatterns = [
        
        #path(r'',IndexHome.as_view()),
        path(r'remote',RemoteautocompleteAzienda.as_view()),
        path(r'login',Login.as_view()),
        path(r'logout',Logout.as_view()),
        path(r'auth',Authenticate.as_view()),
        path(r'list',UsersList.as_view()),
        path(r'nuovoutente',CreateUserXAzienda.as_view()),
        path(r'selectazienda/<int:azienda_id>',SelectAzienda.as_view()),
        

]
