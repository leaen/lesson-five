from django.shortcuts import render
from django.views.generic import CreateView, RedirectView
from django.core.urlresolvers import reverse

from .forms import HelloWorldForm
from .models import Person


def example(request):
    return render(request, 'form.html')


def django_example(request):
    if request.method == 'POST':
        form = HelloWorldForm(request.POST)
        if form.is_valid():
            return render(request, 'django_form.html', {
                'form': form,
                'name': form.cleaned_data['name']
            })
    else:
        form = HelloWorldForm()

    return render(request, 'django_form.html', {
        'form': form,
    })


class PersonCreateView(CreateView):
    """
    View to create aa Person instance every 
    time the form is submitted
    """
    model = Person
    template_name = 'django_form.html'
    form_class = HelloWorldForm
    context_object_name = 'person' # "object" is the default

    def get_success_url(self):
        """
        Just redirect to the same page if the form is valid
        """
        return reverse('django_form')

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context['people'] = self.model.objects.all()
        return context


class RootRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('django_form')
