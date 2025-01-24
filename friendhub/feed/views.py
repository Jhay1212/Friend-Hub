from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import  CreateView, DeleteView, FormView, UpdateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Chirp, Comments
from .forms import ChirpForm

class Feed(ListView):
    model = Chirp
    template_name = 'feed/home.html'
    context_object_name = 'object'
    # form_class = ChirpForm
    queryset = Chirp.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if 'form' not in context:
    #         context['form'] = self.get_form()
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():


    #         chirp = form.save()
    #         chirp.user = request.user  # Assuming Chirp has a 'user' field
    #         # chirp.save()
    #         return redirect('home')
        
    #     return self.render_to_response(self.get_context_data(form=form))
class ChirpDetail(DetailView):
    model = Chirp
    lookup_field = 'pk'
    lookup_field_kwarg = 'pk'



# class ChirpDetail(DetailView):
#     model = Chirp

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pk'] = 
class CreateChirp(LoginRequiredMixin, CreateView):
    model = Chirp
    fields = ['content']
    

    def form_valid(self, form, request, *args, **kwargs):
        form.user = request.user 
        form.save()
    

class UpdateChirp(LoginRequiredMixin, UpdateView):
    model = Chirp
    login_url  = 'user:login'
    redirect_field_name = 'user:login'
    lookup_field = 'pk'


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comments
    fields = []

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if not request.user:
            return HttpResponseForbidden('User not logged in')
        form.author = request.user


    


def collats(number):
    if number <= 1:
        return number
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    return collats(number)


print(collats(100))
