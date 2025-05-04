from django.shortcuts import render
from django.http import HttpResponseRedirect

from home.models import Azienda,Fornitori
from home.form_aziende import FormAzienda
from django.views.generic.list import ListView,View
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

# Create your views here.

class AziendeList(ListView):
    model = Azienda
    template_name = "listAziende.html"

    def get(self,request):

        az = Azienda.objects.all()

        context={'aziende': az}
        

        return render(request, self.template_name, context)
       
class AziendaInsert(CreateView):
    model = Azienda
    template_name = "insertazienda.html"

    def get(self,request):
        form = FormAzienda()
    
        return render(request, self.template_name, {'form': form})
    

    def post(self,request):

        res = request.POST
        res2={}
        res2['post']= res
        filelogo = False
        if 'logo' in request.FILES:
            file = request.FILES.get('logo')
            res2['file']=file.name
            filelogo=True
        else:
            res2['file']='No File logo'

        codcf = request.POST.get('codcf')
        nome = request.POST.get('nome')
        ragione_sociale=request.POST.get('ragione_sociale',None)
        codfisc=request.POST.get('codfisc',None)
        descrizione =request.POST.get('descrizione',None)
        indirizzo=request.POST.get('indirizzo',None)
        cap=request.POST.get('cap',None)
        local=request.POST.get('local',None)
        prov=request.POST.get('prov',None)
        partiva=request.POST.get('partiva',None)
        telefono=request.POST.get('telefono',None)
        cellulare=request.POST.get('cellulare',None)
        pec=request.POST.get('pec',None)
        fax=request.POST.get('fax',None)
        email=request.POST.get('email',None)
        resprap=request.POST.get('resprap',None)
        fmemo=request.POST.get('fmemo',None)
        nome_pf=request.POST.get('nome_pf',None)
        cogn_pf=request.POST.get('cogn_pf',None)

        a= Azienda(codcf=codcf,nome=nome)
        a.save()
        if filelogo:
            a.logo=file
            a.save()
        az = Azienda.objects.filter(codcf=codcf)
        # Devo inserire l'azienda anche tra i fornitori.
        f = Fornitori(codcf=codcf,azienda=a,fmemo=" Azienda Fornitore di se stessa")
        f.save()
        al =list(az.values())[0]
        #s = serializers.serialize("json",az)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))      

        #return redirect('.')
