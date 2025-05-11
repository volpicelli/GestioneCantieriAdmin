# import form class from django
from django import forms
 
# import GeeksModel from models.py
from home.models import Azienda
 
# create a ModelForm
class FormAzienda(forms.ModelForm):
    # specify the name of model to use
    
    class Meta:
        model = Azienda
        fields = "__all__"
        #exclude = ('mestesso','magazzino',)
    
    def __init__(self,*args,**kwargs):
        
        
        #super().__init__(*args, **kwargs)
        super(FormAzienda, self).__init__(*args, **kwargs)
        #if instance is None:
        #self.fields['data_ordine'] = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
        
        #forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True})

        self.fields['nome'] =  forms.CharField(label="Nome",
                                        widget=forms.TextInput(attrs={ 'id':'nomeazienda','required': True}))
        self.fields['codcf'] =  forms.CharField(label="Codice Unico",required= True,
                                        widget=forms.TextInput(attrs={ 'id':'codcf','required': True}))

        self.fields['email']=forms.CharField(widget=forms.EmailInput(attrs={'id':'emailazienda', 'required':True})) #,label='', required=False)
        
        self.fields['cellulare']=forms.CharField(label="Cellulare",required=False,
                                    widget=forms.TextInput(attrs={'id':'cellulareazienda'})) #,label='', required=False)

        self.fields['descrizione'] =  forms.CharField(label="Descrizione", required=False,
                                                         widget=forms.Textarea(attrs={'style': 'max-width: 100%','rows':2,'required': False}))
        self.fields['fmemo'] =  forms.CharField(label="FMemo", required=False,
                                                         widget=forms.Textarea(attrs={'style': 'max-width: 100%','rows':2,'required': False}))
        #self.fields['codcf'] = forms.CharField(label="PIPPO")

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        