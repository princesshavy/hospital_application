from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webpage/index.html')

def contact(request):
    return render(request, 'webpage/contact.html')