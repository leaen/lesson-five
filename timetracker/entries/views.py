from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, CreateView, RedirectView
from django.core.urlresolvers import reverse_lazy

from .forms import EntryForm, ProjectForm, ClientForm
from .models import Client, Entry, Project

class RootRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('client-list')

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'client_create.html'
    form_class = ClientForm

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'

class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project_create.html'
    form_class = ProjectForm

class EntryListView(ListView):
    model = Entry
    template_name = 'entry_list.html'

