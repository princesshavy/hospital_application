from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webpage/index.html')

# def contact(request):
#     return render(request, 'webpage/contact.html')

# def about(request):
#     return render(request, 'webpage/about.html')

# def blog(request):
#     return render(request, 'webpage/ blog.html')

# def error(request):
#     return render(request, 'webpage/ error.html')