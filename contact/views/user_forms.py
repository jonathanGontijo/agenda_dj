from django.shortcuts import render
from contact.forms import RegisterForm

def register(request):
    form = RegisterForm()
    if request.method == 'Post':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )