from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Profile

class ProfileView(DetailView):
    model = Profile 
    lookup_field = 'slug'
    template_name = 'users/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = self.get_context_data(kwargs=kwargs)
    #     context['profile'] = Profile.objects.get(username=self.kwargs['slug'])
    #     return context
    
    def get_object(self, queryset=None):
        return Profile.objects.get(username=self.kwargs['slug'])
# Create your views here.
