from django.shortcuts import render
from home.models import ClientiGestioneCantieri,Azienda
from django.views.generic.list import ListView,View
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView 
from django.urls import reverse_lazy
from .form_clientigestione import FormClientiGestione
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

#from .clientigestione_serializer import ClientiGestioneserializer
# Create your views here.
class TestLoadModal(View):
    def get(self,request):
        res={'pollo':'POLLO'}

        return JsonResponse(res,safe=False)

class ClientiGestione(ListView):
    model = ClientiGestioneCantieri
    template_name = "listClientiGestione.html"

    def get(self,request):
        if not request.user.is_authenticated:        
            return HttpResponseRedirect('/access/login')

        cgc  = ClientiGestioneCantieri.objects.all()
        az = Azienda.objects.all()

        context={'clientigestione':cgc,'aziende': az}
        

        return render(request, self.template_name, context)
       
class UpdateClienteGestione(UpdateView):
    model = ClientiGestioneCantieri
    template_name = "nuovocliente.html"
    form_class = FormClientiGestione
    success_url = reverse_lazy('listclienti')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Update Book'
        return context
    
    # Optional: You can customize the form before it's rendered
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Customize form here if needed
        return form
    
    # Optional: You can perform additional actions before saving
    def form_valid(self, form):
        # You can access the object being updated with self.object
        # or form.instance before it's saved
        return super().form_valid(form)

    #def get(self,request,pk):
    #    form = FormClientiGestione()
    
    #    return render(request, 'nuovocliente.html', {'form': form})
    

class RemoteautocompleteCliente(View):
    def get(self,request):
        q = request.GET.get('q')
        resp=[]
        res = ClientiGestioneCantieri.objects.filter(cognome__icontains=q)#.values_list('cognome')
        for one in res:
            a={}
            a['cognome']=one.cognome
            a['id']=one.id
            resp.append(a)


        return JsonResponse(resp,safe=False)


class NuovoClienteGestione(CreateView):
    model = ClientiGestioneCantieri
    template_name = "nuovocliente.html"

    def get(self,request):
        if not request.user.is_authenticated:        
            return HttpResponseRedirect('/access/login')
            
        form = FormClientiGestione()
    
        return render(request, 'nuovocliente.html', {'form': form})
    

    def post(self,request):

        res = request.POST
        cgc  = ClientiGestioneCantieri()
        cgc.cognome = request.POST.get('cognome')
        cgc.nome = request.POST.get('nome')
        cgc.telefono = request.POST.get('telefono')
        cgc.email = request.POST.get('email')
        cgc.cellulare = request.POST.get('cellulare')
        cgc.save()

        return JsonResponse(res,safe=False)

"""
>>> c = ClientiGestioneCantieri.objects.get(pk=2)


>>> a6=Azienda.objects.get(pk=6)
>>> a7=Azienda.objects.get(pk=7)
>>> c.aziende.add(a6,a7)
>>> 


"""