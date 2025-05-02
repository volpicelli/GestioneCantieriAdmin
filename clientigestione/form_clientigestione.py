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
        exclude = ('aziende',)
    
    def __init__(self,*args,**kwargs):
        
        
        #super().__init__(*args, **kwargs)
        super(FormClientiGestione, self).__init__(*args, **kwargs)
        #if instance is None:
       

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        