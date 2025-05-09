# import form class from django
from django import forms
 
# import GeeksModel from models.py
from home.models import ClientiGestioneCantieri
 
# create a ModelForm
class FormClientiGestione(forms.ModelForm):
    # specify the name of model to use
    
    class Meta:
        model = ClientiGestioneCantieri
        fields = "__all__"
        exclude = ('aziende','telefono')
    
    def __init__(self,*args,**kwargs):
        
        
        #super().__init__(*args, **kwargs)
        super(FormClientiGestione, self).__init__(*args, **kwargs)
        #if instance is None:
        self.fields['nome'] =  forms.CharField(label="Nome",
                                        widget=forms.TextInput(attrs={ 'required': True}))
        self.fields['cognome'] =  forms.CharField(label="Cognome",
                                        widget=forms.TextInput(attrs={ 'required': True}))
        self.fields['email'] =  forms.CharField(label="Email",
                                        widget=forms.EmailInput(attrs={ 'required': True}))


        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        