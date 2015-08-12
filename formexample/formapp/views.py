from django.shortcuts import render
from .forms import HelloWorldForm


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
