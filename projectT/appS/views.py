from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import User_req
from django.views.generic.edit import CreateView
from .forms import User_reqForm
from django.urls import reverse_lazy
# Create your views here.


class User_reqCreateView(CreateView):
    template_name = 'layouts/sign.html'
    form_class = User_reqForm
    success_url = reverse_lazy('base')

def qq(request):
    template = loader.get_template('layouts/base.html')
    return HttpResponse(template.render({}, request))

def sign(request):
    if request.method == 'POST':
        template = loader.get_template('layouts/base.html')
        return HttpResponse(template.render({}, request))

    else:
        template = loader.get_template('layouts/sign.html')
        return HttpResponse(template.render({}, request))
