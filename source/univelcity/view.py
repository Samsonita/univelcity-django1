from django.shortcuts import render

#Landing Page View
def index(request):
    return render(
        request,
        'index.html'
    )