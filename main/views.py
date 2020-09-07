from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import TemplateView   

def index(request):
    return render(request, 'main/home.html', {})
    
class ContactView(TemplateView):
    template_name = 'main/contact_us.html'

    def get(self, request):
        form = ContactForm()
        args = {'form':form }

        return render(request, self.template_name, args)

    def post(self , request):
        form = ContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = ContactForm()
            return redirect('main:contact')

        args = {'form': form}
        return render(request, self.template_name, args)
