from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', {'name': 'Felippe Andrade'})


def about(request):
    return render(request, 'recipes/about.html')


def contact(request):
    return render(request, 'recipes/contact.html')
