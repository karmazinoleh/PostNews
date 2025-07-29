from django.shortcuts import render

# Create your views here.

def index(request):
    data = {
        'title': 'Home',
        'values': ['User1', 'User2', 'User3'],
        'user': {
            'name': 'Oleh',
            'email': 'oleh@gmail.com',
            'tel': '+88392181'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')